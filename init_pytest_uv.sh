#!/usr/bin/env bash
set -euo pipefail

PYTHON_SPEC=""
NO_PIP=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --python)
      PYTHON_SPEC="$2"
      shift 2
      ;;
    --no-pip)
      NO_PIP=true
      shift
      ;;
    *)
      echo "Unknown option: $1"; exit 1
      ;;
  esac
done

# 1) 检查 uv
if ! command -v uv >/dev/null 2>&1; then
  echo "uv not found. Install: curl -LsSf https://astral.sh/uv/install.sh | sh"
  exit 1
fi

# 2) 创建 .venv（可指定 Python 版本/路径）
if [[ -d ".venv" ]]; then
  read -r -p ".venv exists. Recreate? [y/N] " ans
  if [[ "${ans:-N}" =~ ^[Yy]$ ]]; then rm -rf .venv; else echo "Abort."; exit 1; fi
fi
if [[ -n "$PYTHON_SPEC" ]]; then
  uv venv --python "$PYTHON_SPEC"
else
  uv venv
fi

# 3) （可选）卸载基础包，得到“极简环境”
#    卸载后就不要再用 pip 了，后续统一用 uv 安装/同步。
if $NO_PIP; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
  python -m pip uninstall -y pip setuptools wheel || true
fi

# 4) 基本的 .gitignore
if [[ ! -f ".gitignore" ]]; then
  cat > .gitignore <<'EOF'
.venv
.pytest_cache
.coverage
dist/
build/
reports/
__pycache__/
.DS_Store
EOF
fi

# 5) 最小 pyproject（空依赖，可后续用 uv add）
if [[ ! -f "pyproject.toml" ]]; then
  cat > pyproject.toml <<'EOF'
[project]
name = "pytest-api-demo"
version = "0.1.0"
requires-python = ">=3.10"

# 留空依赖；需要时使用：
# uv add requests httpx pydantic
# 开发依赖示例：
# uv add --dev pytest pytest-cov

[tool.pytest.ini_options]
addopts = "-ra -q"
testpaths = ["tests"]
EOF
fi

# 6) 生成锁文件（当前为空依赖）
uv lock

echo "Done.
• 激活环境：source .venv/bin/activate
• 查看包：   python -m pip list  （若 --no-pip 则跳过）
• 安装依赖： uv add httpx pydantic
• 开发依赖： uv add --dev pytest pytest-cov
• 复现环境： uv sync
"
