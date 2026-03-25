# GSI-Protocol Development Workflow

[中文版本](./README.zh-TW.md) | **English**

## Problem
When modifying GSI command content, you need to maintain three locations:
- `.claude/commands/` (Claude Code)
- `.codex/prompts/` (Codex)
- `.github/prompts/` (GitHub Copilot)

## Solution
Single source + automatic sync script

## Directory Structure
```
scripts/
  ├── templates/        # 📝 Single source of truth for templates
  │   ├── sdd-spec.md
  │   ├── sdd-arch.md
  │   ├── sdd-impl.md
  │   ├── sdd-verify.md
  │   ├── sdd-unit-test.md
  │   └── sdd-auto.md
  ├── dev_sync.py       # 🔧 Local development testing tool (for developers only)
  └── README.md         # 📖 This file
```

## Development Workflow

### 1. Edit Templates
Only need to modify files in `scripts/templates/`, using generic placeholders:

```markdown
## User Requirements

__PROMPT__

## Next Steps
- Use command: `__CMD_PREFIX__sdd-arch features/xxx.feature`
```

**Placeholder Explanation:**
- `__PROMPT__` - User input parameter
- `__CMD_PREFIX__` - Command prefix (automatically converted per platform)

### 2. Sync to Three Platforms
Run the development sync tool:

```bash
python3 scripts/dev_sync.py
```

⚠️ **Note**: This tool is for development testing only, end users don't need it

This will automatically convert placeholders and sync:
- Convert and sync to `.claude/commands/`: `__PROMPT__` → `{{prompt}}`, `__CMD_PREFIX__` → `/`
- Convert and sync to `.codex/prompts/`: `__PROMPT__` → `$1`, `__CMD_PREFIX__` → `/`
- Convert and sync to `.github/prompts/`: `__PROMPT__` → `{{ARG}}`, `__CMD_PREFIX__` → `@workspace /`

### 3. Test
Test commands on each platform locally

### 4. Commit
Commit all changes to Git

## User Installation Flow

When users run:
```bash
uvx --from gsi-protocol-installer gsi-install
```

`gsi_installer.py` will:
1. Download the repo from GitHub
2. Read templates from `scripts/templates/`
3. Automatically convert and install based on user's platform choice

## Placeholder Conversion Table

| Platform | `__PROMPT__` converts to | `__CMD_PREFIX__` converts to | File Extension |
|----------|-------------------------|------------------------------|----------------|
| Template | `__PROMPT__` | `__CMD_PREFIX__` | `.md` |
| Claude Code | `{{prompt}}` | `/` | `.md` |
| Codex | `$1` | `/` | `.md` |
| GitHub Copilot | `{{ARG}}` | `@workspace /` | `.prompt.md` |

## Benefits

✅ Only maintain one location (`scripts/templates/`)
✅ Automatically handle platform differences
✅ Reduce maintenance cost
✅ Minimize human errors
