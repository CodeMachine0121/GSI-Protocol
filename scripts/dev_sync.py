#!/usr/bin/env python3
"""
🔧 開發測試工具 - 本地同步腳本

⚠️  此腳本僅供 repo 維護者在本地開發測試使用
⚠️  終端用戶不需要使用此腳本，請使用官方安裝器

功能：將 scripts/templates/ 中的模板同步到三個目標位置
用法：python3 scripts/dev_sync.py

使用場景：
1. 修改模板後快速預覽轉換結果
2. 本地測試各平台命令是否正常
3. 提交前驗證佔位符轉換正確性
"""

import os
from pathlib import Path
import shutil


def transform_template_for_claude(content: str) -> str:
    """轉換為 Claude Code 格式"""
    # 替換佔位符為 Claude Code 格式
    result = content.replace('__PROMPT__', '{{prompt}}')
    result = result.replace('__CMD_PREFIX__', '/')
    return result


def transform_template_for_codex(content: str, filename: str) -> str:
    """轉換為 Codex 格式"""
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
    """轉換為 GitHub Copilot 格式"""
    # 替換佔位符為 GitHub Copilot 格式
    result = content.replace('__PROMPT__', '{{ARG}}')
    result = result.replace('__CMD_PREFIX__', '@workspace /')

    return result


def sync_commands():
    """同步模板到三個目標位置"""
    # 獲取專案根目錄
    root_dir = Path(__file__).parent.parent
    templates_dir = root_dir / "scripts" / "templates"

    if not templates_dir.exists():
        print(f"❌ 模板目錄不存在: {templates_dir}")
        print("請先創建 scripts/templates/ 目錄並放入模板文件")
        return

    # 定義三個目標位置
    targets = {
        "Claude Code": {
            "dir": root_dir / ".claude" / "commands",
            "transform": transform_template_for_claude,
            "extension": ".md"
        },
        "Codex": {
            "dir": root_dir / ".codex" / "prompts",
            "transform": transform_template_for_codex,
            "extension": ".md"
        },
        "GitHub Copilot": {
            "dir": root_dir / ".github" / "prompts",
            "transform": transform_template_for_github,
            "extension": ".prompt.md"
        }
    }

    print("🔧 開發模式：本地同步工具")
    print("⚠️  此工具僅供開發測試使用\n")
    print("🔄 開始同步命令模板...\n")

    # 處理每個目標
    for name, config in targets.items():
        target_dir = config["dir"]
        transform_func = config["transform"]
        extension = config["extension"]

        # 創建目標目錄
        target_dir.mkdir(parents=True, exist_ok=True)

        # 清空目標目錄中的舊文件
        for old_file in target_dir.glob("sdd-*"):
            old_file.unlink()

        # 複製並轉換模板
        count = 0
        for template_file in templates_dir.glob("sdd-*.md"):
            content = template_file.read_text(encoding='utf-8')

            # 應用轉換
            if name == "Codex":
                transformed = transform_func(content, template_file.name)
            else:
                transformed = transform_func(content)

            # 確定輸出文件名
            if extension == ".prompt.md":
                output_filename = template_file.stem + extension
            else:
                output_filename = template_file.name

            output_file = target_dir / output_filename
            output_file.write_text(transformed, encoding='utf-8')
            count += 1

        print(f"✅ {name}: 已同步 {count} 個文件到 {target_dir}")

    print("\n✨ 本地同步完成！")
    print("\n💡 開發者提示：")
    print("  - 📝 模板來源: scripts/templates/")
    print("  - 🔄 修改模板後運行此腳本即可同步到三個位置")
    print("  - 🤖 Claude Code: .claude/commands/")
    print("  - 🔷 Codex: .codex/prompts/")
    print("  - 🐙 GitHub Copilot: .github/prompts/")
    print("\n⚠️  注意：此腳本僅供本地開發測試，終端用戶請使用官方安裝器")


if __name__ == "__main__":
    sync_commands()
