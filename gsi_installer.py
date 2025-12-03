"""
GSI-Protocol Installer

A simple CLI tool to install GSI-Protocol workflow commands for Claude Code and/or Codex.

Usage:
    uvx gsi-protocol-installer
    # or
    pipx run gsi-protocol-installer
"""

import os
import sys
from pathlib import Path
from typing import Optional
import shutil
import tempfile
import subprocess


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
    except FileNotFoundError:
        print_error("Git is not installed. Please install git first.")
        sys.exit(1)


def install_commands(source_dir: Path, platform: str, location: str) -> int:
    """Install commands to the specified location."""
    installed_count = 0
    
    if location == "global":
        if platform in ["claude", "both"]:
            target_dir = Path.home() / ".claude" / "commands"
            target_dir.mkdir(parents=True, exist_ok=True)
            
            source = source_dir / ".claude" / "commands"
            for file in source.glob("sdd-*.md"):
                shutil.copy2(file, target_dir / file.name)
                installed_count += 1
            
            print_success(f"Installed {installed_count} Claude Code commands to {target_dir}")
        
        if platform in ["codex", "both"]:
            target_dir = Path.home() / ".codex" / "commands"
            target_dir.mkdir(parents=True, exist_ok=True)
            
            source = source_dir / ".codex" / "commands"
            for file in source.glob("sdd-*.md"):
                shutil.copy2(file, target_dir / file.name)
                installed_count += 1
            
            print_success(f"Installed {len(list((target_dir).glob('sdd-*.md')))} Codex commands to {target_dir}")
    
    else:  # project
        if platform in ["claude", "both"]:
            target_dir = Path.cwd() / ".claude" / "commands"
            
            if target_dir.exists():
                if not prompt_yes_no(f"⚠️  {target_dir} already exists. Overwrite?", default=False):
                    print_warning("Skipping Claude Code installation")
                else:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    source = source_dir / ".claude" / "commands"
                    for file in source.glob("sdd-*.md"):
                        shutil.copy2(file, target_dir / file.name)
                        installed_count += 1
                    print_success(f"Installed {installed_count} Claude Code commands to {target_dir}")
            else:
                target_dir.mkdir(parents=True, exist_ok=True)
                source = source_dir / ".claude" / "commands"
                for file in source.glob("sdd-*.md"):
                    shutil.copy2(file, target_dir / file.name)
                    installed_count += 1
                print_success(f"Installed {installed_count} Claude Code commands to {target_dir}")
        
        if platform in ["codex", "both"]:
            target_dir = Path.cwd() / ".codex" / "commands"
            
            if target_dir.exists():
                if not prompt_yes_no(f"⚠️  {target_dir} already exists. Overwrite?", default=False):
                    print_warning("Skipping Codex installation")
                else:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    source = source_dir / ".codex" / "commands"
                    for file in source.glob("sdd-*.md"):
                        shutil.copy2(file, target_dir / file.name)
                        installed_count += 1
                    print_success(f"Installed {len(list((target_dir).glob('sdd-*.md')))} Codex commands to {target_dir}")
            else:
                target_dir.mkdir(parents=True, exist_ok=True)
                source = source_dir / ".codex" / "commands"
                for file in source.glob("sdd-*.md"):
                    shutil.copy2(file, target_dir / file.name)
                    installed_count += 1
                print_success(f"Installed {len(list((target_dir).glob('sdd-*.md')))} Codex commands to {target_dir}")
    
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


def main():
    """Main installation flow."""
    print_header()
    
    # Step 1: Choose platform
    platform_choice = prompt_choice(
        "Select AI platform(s) to install:",
        [
            "Claude Code only",
            "Codex (OpenAI) only",
            "Both Claude Code and Codex"
        ],
        default=3
    )
    
    platform_map = {1: "claude", 2: "codex", 3: "both"}
    platform = platform_map[platform_choice]
    
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
    
    # Step 3: Download
    print()
    source_dir = download_commands()
    
    # Step 4: Install
    print()
    installed_count = install_commands(source_dir, platform, location)
    
    # Step 5: Cleanup
    shutil.rmtree(source_dir.parent)
    
    # Step 6: Success message
    print()
    print("=" * 60)
    print_success(f"Installation complete! Total files installed: {installed_count}")
    print()
    print("You can now use SDD commands:")
    print("  /sdd-auto <requirement>")
    print("  /sdd-spec <requirement>")
    print("  /sdd-arch <feature.feature>")
    print("  /sdd-impl <feature.feature>")
    print("  /sdd-verify <feature.feature>")
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
