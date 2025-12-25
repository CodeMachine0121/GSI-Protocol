"""
GSI-Protocol Installer

A simple CLI tool to install GSI-Protocol workflow commands for Claude Code and/or Codex.

Usage:
    uvx --from gsi-protocol-installer gsi-install
    # or
    pipx run gsi-protocol-installer

    # 本地同步模式（用於開發）：
    python gsi_installer.py --sync
"""

import os
import sys
from pathlib import Path
from typing import Optional
import shutil
import tempfile
import subprocess
import argparse


class Colors:
    """ANSI color codes for terminal output."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_header():
    """Print installation header."""
    print(f"\n{Colors.BOLD}🚀 GSI-Protocol Installer{Colors.ENDC}")
    print("=" * 60)
    print()


def print_success(message: str):
    """Print success message."""
    print(f"{Colors.OKGREEN}✓{Colors.ENDC} {message}")


def print_error(message: str):
    """Print error message."""
    print(f"{Colors.FAIL}✗{Colors.ENDC} {message}")


def print_warning(message: str):
    """Print warning message."""
    print(f"{Colors.WARNING}⚠{Colors.ENDC} {message}")


def print_info(message: str):
    """Print info message."""
    print(f"{Colors.OKCYAN}ℹ{Colors.ENDC} {message}")


def prompt_multi_choice(question: str, choices: list[str], default: list[int] = None) -> list[int]:
    """Prompt user for multiple choices."""
    print(f"\n{Colors.BOLD}{question}{Colors.ENDC}")
    for i, choice in enumerate(choices, 1):
        print(f"{i}) {choice}")
    
    default_str = ",".join(map(str, default)) if default else "all"
    while True:
        try:
            response = input(f"Enter choices (comma-separated, e.g., 1,2,3) or 'all' (default: {default_str}): ").strip().lower()
            if not response:
                return default if default else list(range(1, len(choices) + 1))
            if response == 'all':
                return list(range(1, len(choices) + 1))
            
            selected = [int(x.strip()) for x in response.split(',')]
            if all(1 <= x <= len(choices) for x in selected):
                return selected
            print_error(f"Please enter numbers between 1 and {len(choices)}")
        except ValueError:
            print_error("Please enter valid numbers separated by commas")
        except KeyboardInterrupt:
            print("\n\nInstallation cancelled.")
            sys.exit(0)


def prompt_choice(question: str, choices: list[str], default: int = 1) -> int:
    """Prompt user for a choice."""
    print(f"\n{Colors.BOLD}{question}{Colors.ENDC}")
    for i, choice in enumerate(choices, 1):
        print(f"{i}) {choice}")
    
    while True:
        try:
            response = input(f"Enter choice [1-{len(choices)}] (default: {default}): ").strip()
            if not response:
                return default
            choice = int(response)
            if 1 <= choice <= len(choices):
                return choice
            print_error(f"Please enter a number between 1 and {len(choices)}")
        except ValueError:
            print_error("Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\nInstallation cancelled.")
            sys.exit(0)


def prompt_yes_no(question: str, default: bool = False) -> bool:
    """Prompt user for yes/no."""
    default_str = "Y/n" if default else "y/N"
    while True:
        try:
            response = input(f"{question} [{default_str}]: ").strip().lower()
            if not response:
                return default
            if response in ['y', 'yes']:
                return True
            if response in ['n', 'no']:
                return False
            print_error("Please enter 'y' or 'n'")
        except KeyboardInterrupt:
            print("\n\nInstallation cancelled.")
            sys.exit(0)


def download_commands(repo_url: str = "https://github.com/CodeMachine0121/GSI-Protocol.git") -> Path:
    """Download command files from GitHub."""
    print_info("Downloading GSI-Protocol from GitHub...")
    
    temp_dir = Path(tempfile.mkdtemp())
    
    try:
        # Clone the repository
        result = subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, str(temp_dir / "gsi-protocol")],
            capture_output=True,
            text=True,
            check=True
        )
        print_success("Downloaded successfully")
        return temp_dir / "gsi-protocol"
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to download: {e.stderr}")
        sys.exit(1)


def transform_template_for_claude(content: str) -> str:
    """Transform template for Claude Code format."""
    # 替換佔位符為 Claude Code 格式
    result = content.replace('__PROMPT__', '{{prompt}}')
    result = result.replace('__CMD_PREFIX__', '/')
    return result


def transform_template_for_codex(content: str, filename: str) -> str:
    """Transform template for Codex format."""
    # 替換佔位符為 Codex 格式
    result = content.replace('__PROMPT__', '$1')
    result = result.replace('__CMD_PREFIX__', '/')

    # 在 frontmatter 中加入 argument-hint
    if content.startswith('---\n'):
        parts = result.split('---\n')
        if len(parts) >= 3:
            # 根據不同的指令設置不同的 argument-hint
            hint = ''
            if 'arch' in filename:
                hint = 'argument-hint: <feature_file_path>\n'
            elif 'impl' in filename:
                hint = 'argument-hint: <feature_file_path>\n'
            elif 'verify' in filename:
                hint = 'argument-hint: <feature_file_path>\n'
            elif 'integration-test' in filename:
                hint = 'argument-hint: <feature_file_path>\n'

            parts[1] = hint + parts[1]
            result = '---\n'.join(parts)

    return result


def transform_template_for_github(content: str) -> str:
    """Transform template for GitHub Copilot format."""
    # 替換佔位符為 GitHub Copilot 格式
    result = content.replace('__PROMPT__', '{{ARG}}')
    result = result.replace('__CMD_PREFIX__', '@workspace /')

    return result


def install_commands(source_dir: Path, platforms: list[str], location: str, claude_type: str = "both") -> int:
    """Install commands to the specified location."""
    installed_count = 0

    # 模板目錄
    templates_dir = source_dir / "scripts" / "templates"

    if not templates_dir.exists():
        print_error(f"Templates directory not found: {templates_dir}")
        sys.exit(1)

    if location == "global":
        if "claude" in platforms:
            # Install commands if requested
            if claude_type in ["commands", "both"]:
                target_dir = Path.home() / ".claude" / "commands"
                target_dir.mkdir(parents=True, exist_ok=True)

                # 從模板轉換並安裝
                for template_file in templates_dir.glob("sdd-*.md"):
                    content = template_file.read_text(encoding='utf-8')
                    transformed = transform_template_for_claude(content)

                    output_file = target_dir / template_file.name
                    output_file.write_text(transformed, encoding='utf-8')
                    installed_count += 1

                print_success(f"Installed {len(list((target_dir).glob('sdd-*.md')))} Claude Code commands to {target_dir}")

            # Install agents if requested
            if claude_type in ["agents", "both"]:
                target_dir = Path.home() / ".claude" / "agents"
                target_dir.mkdir(parents=True, exist_ok=True)

                source = source_dir / ".claude" / "agents"
                if source.exists():
                    for file in source.glob("*.md"):
                        shutil.copy2(file, target_dir / file.name)
                        installed_count += 1

                    print_success(f"Installed {len(list((target_dir).glob('*.md')))} Claude Code agents to {target_dir}")
        
        if "codex" in platforms:
            target_dir = Path.home() / ".codex" / "prompts"
            target_dir.mkdir(parents=True, exist_ok=True)

            # 從模板轉換並安裝
            for template_file in templates_dir.glob("sdd-*.md"):
                content = template_file.read_text(encoding='utf-8')
                transformed = transform_template_for_codex(content, template_file.name)

                output_file = target_dir / template_file.name
                output_file.write_text(transformed, encoding='utf-8')
                installed_count += 1

            print_success(f"Installed {len(list((target_dir).glob('sdd-*.md')))} Codex prompts to {target_dir}")
        
        if "copilot" in platforms:
            target_dir = Path.home() / ".github" / "prompts"
            target_dir.mkdir(parents=True, exist_ok=True)

            # 從模板轉換並安裝
            for template_file in templates_dir.glob("sdd-*.md"):
                content = template_file.read_text(encoding='utf-8')
                transformed = transform_template_for_github(content)

                # GitHub Copilot 使用 .prompt.md 擴展名
                output_filename = template_file.stem + '.prompt.md'
                output_file = target_dir / output_filename
                output_file.write_text(transformed, encoding='utf-8')
                installed_count += 1

            print_success(f"Installed {len(list((target_dir).glob('sdd-*.prompt.md')))} GitHub Copilot prompts to {target_dir}")
    
    else:  # project
        if "claude" in platforms:
            # Install commands if requested
            if claude_type in ["commands", "both"]:
                target_dir = Path.cwd() / ".claude" / "commands"

                if target_dir.exists():
                    if not prompt_yes_no(f"⚠️  {target_dir} already exists. Overwrite?", default=False):
                        print_warning("Skipping Claude Code commands installation")
                    else:
                        target_dir.mkdir(parents=True, exist_ok=True)
                        # 從模板轉換並安裝
                        for template_file in templates_dir.glob("sdd-*.md"):
                            content = template_file.read_text(encoding='utf-8')
                            transformed = transform_template_for_claude(content)

                            output_file = target_dir / template_file.name
                            output_file.write_text(transformed, encoding='utf-8')
                            installed_count += 1
                        print_success(f"Installed {len(list((target_dir).glob('sdd-*.md')))} Claude Code commands to {target_dir}")
                else:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    # 從模板轉換並安裝
                    for template_file in templates_dir.glob("sdd-*.md"):
                        content = template_file.read_text(encoding='utf-8')
                        transformed = transform_template_for_claude(content)

                        output_file = target_dir / template_file.name
                        output_file.write_text(transformed, encoding='utf-8')
                        installed_count += 1
                    print_success(f"Installed {len(list((target_dir).glob('sdd-*.md')))} Claude Code commands to {target_dir}")

            # Install agents if requested
            if claude_type in ["agents", "both"]:
                target_dir = Path.cwd() / ".claude" / "agents"

                if target_dir.exists():
                    if not prompt_yes_no(f"⚠️  {target_dir} already exists. Overwrite?", default=False):
                        print_warning("Skipping Claude Code agents installation")
                    else:
                        target_dir.mkdir(parents=True, exist_ok=True)
                        source = source_dir / ".claude" / "agents"
                        if source.exists():
                            for file in source.glob("*.md"):
                                shutil.copy2(file, target_dir / file.name)
                                installed_count += 1
                            print_success(f"Installed {len(list((target_dir).glob('*.md')))} Claude Code agents to {target_dir}")
                else:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    source = source_dir / ".claude" / "agents"
                    if source.exists():
                        for file in source.glob("*.md"):
                            shutil.copy2(file, target_dir / file.name)
                            installed_count += 1
                        print_success(f"Installed {len(list((target_dir).glob('*.md')))} Claude Code agents to {target_dir}")
        
        if "codex" in platforms:
            target_dir = Path.cwd() / ".codex" / "prompts"

            if target_dir.exists():
                if not prompt_yes_no(f"⚠️  {target_dir} already exists. Overwrite?", default=False):
                    print_warning("Skipping Codex installation")
                else:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    # 從模板轉換並安裝
                    for template_file in templates_dir.glob("sdd-*.md"):
                        content = template_file.read_text(encoding='utf-8')
                        transformed = transform_template_for_codex(content, template_file.name)

                        output_file = target_dir / template_file.name
                        output_file.write_text(transformed, encoding='utf-8')
                        installed_count += 1
                    print_success(f"Installed {len(list((target_dir).glob('sdd-*.md')))} Codex prompts to {target_dir}")
            else:
                target_dir.mkdir(parents=True, exist_ok=True)
                # 從模板轉換並安裝
                for template_file in templates_dir.glob("sdd-*.md"):
                    content = template_file.read_text(encoding='utf-8')
                    transformed = transform_template_for_codex(content, template_file.name)

                    output_file = target_dir / template_file.name
                    output_file.write_text(transformed, encoding='utf-8')
                    installed_count += 1
                print_success(f"Installed {len(list((target_dir).glob('sdd-*.md')))} Codex prompts to {target_dir}")
        
        if "copilot" in platforms:
            target_dir = Path.cwd() / ".github" / "prompts"

            if target_dir.exists():
                if not prompt_yes_no(f"⚠️  {target_dir} already exists. Overwrite?", default=False):
                    print_warning("Skipping GitHub Copilot installation")
                else:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    # 從模板轉換並安裝
                    for template_file in templates_dir.glob("sdd-*.md"):
                        content = template_file.read_text(encoding='utf-8')
                        transformed = transform_template_for_github(content)

                        # GitHub Copilot 使用 .prompt.md 擴展名
                        output_filename = template_file.stem + '.prompt.md'
                        output_file = target_dir / output_filename
                        output_file.write_text(transformed, encoding='utf-8')
                        installed_count += 1
                    print_success(f"Installed {len(list((target_dir).glob('sdd-*.prompt.md')))} GitHub Copilot prompts to {target_dir}")
            else:
                target_dir.mkdir(parents=True, exist_ok=True)
                # 從模板轉換並安裝
                for template_file in templates_dir.glob("sdd-*.md"):
                    content = template_file.read_text(encoding='utf-8')
                    transformed = transform_template_for_github(content)

                    # GitHub Copilot 使用 .prompt.md 擴展名
                    output_filename = template_file.stem + '.prompt.md'
                    output_file = target_dir / output_filename
                    output_file.write_text(transformed, encoding='utf-8')
                    installed_count += 1
                print_success(f"Installed {len(list((target_dir).glob('sdd-*.prompt.md')))} GitHub Copilot prompts to {target_dir}")
    
    return installed_count


def detect_installation_type() -> str:
    """Detect if we're in a git repository."""
    try:
        subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            capture_output=True,
            check=True
        )
        return "project"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def check_git_available() -> bool:
    """Check if git is available."""
    try:
        subprocess.run(
            ["git", "--version"],
            capture_output=True,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def main():
    """Main installation flow."""
    print_header()
    
    # Step 1: Choose platforms
    platform_choices = prompt_multi_choice(
        "Select AI platform(s) to install:",
        [
            "Claude Code",
            "Codex (OpenAI)",
            "GitHub Copilot"
        ],
        default=[1, 2, 3]
    )
    
    platform_map = {1: "claude", 2: "codex", 3: "copilot"}
    platforms = [platform_map[choice] for choice in platform_choices]

    # Step 1.5: If Claude is selected, choose what to install
    claude_type = "both"
    if "claude" in platforms:
        claude_choice = prompt_choice(
            "What would you like to install for Claude Code?",
            [
                "Commands only",
                "Sub-agents only",
                "Both commands and sub-agents"
            ],
            default=3
        )
        claude_type_map = {1: "commands", 2: "agents", 3: "both"}
        claude_type = claude_type_map[claude_choice]

    # Step 2: Choose installation location
    detected = detect_installation_type()
    
    if detected == "project":
        print_success("Git repository detected")
        location_choice = prompt_choice(
            "Choose installation type:",
            [
                "Install to current project",
                "Install globally to home directory"
            ],
            default=1
        )
    else:
        print_info("Not in a git repository")
        location_choice = prompt_choice(
            "Choose installation type:",
            [
                "Install to current directory",
                "Install globally to home directory"
            ],
            default=2
        )
    
    location = "project" if location_choice == 1 else "global"
    
    # Step 3: Check git availability (only needed for downloading)
    if not check_git_available():
        print_error("Git is not installed. Please install git first.")
        print_info("You can download git from: https://git-scm.com/downloads")
        sys.exit(1)
    
    # Step 4: Download
    print()
    source_dir = download_commands()
    
    # Step 5: Install
    print()
    installed_count = install_commands(source_dir, platforms, location, claude_type)
    
    # Step 6: Cleanup
    shutil.rmtree(source_dir.parent)
    
    # Step 7: Success message
    print()
    print("=" * 60)
    print_success(f"Installation complete! Total files installed: {installed_count}")
    print()
    
    # Platform-specific usage instructions
    if "claude" in platforms or "codex" in platforms:
        print("Claude Code / Codex usage:")
        print("  /sdd-auto <requirement>")
        print("  /sdd-spec <requirement>")
        print("  /sdd-arch <feature.feature>")
        print("  /sdd-impl <feature.feature>")
        print("  /sdd-verify <feature.feature>")
        print()
    
    if "copilot" in platforms:
        print("GitHub Copilot usage:")
        print("  @workspace /sdd-auto <requirement>")
        print("  @workspace /sdd-spec <requirement>")
        print("  @workspace /sdd-arch <feature.feature>")
        print("  @workspace /sdd-impl <feature.feature>")
        print("  @workspace /sdd-verify <feature.feature>")
        print()
    
    print(f"📖 Documentation: {Colors.OKCYAN}https://github.com/CodeMachine0121/GSI-Protocol{Colors.ENDC}")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInstallation cancelled.")
        sys.exit(0)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)
