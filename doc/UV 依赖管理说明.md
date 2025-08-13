# UV 依赖管理说明

## 📦 项目依赖管理策略

本项目使用 **uv** 作为现代 Python 依赖管理工具，替代传统的pip+requirements.txt方式。

### 🔧 本地开发

```bash
# 1. 同步所有依赖组
uv sync --group test --group reports

# 2. 运行测试
ENV=dev uv run pytest

# 3. 添加新依赖
uv add requests>=2.32.4

# 4. 添加开发依赖
uv add --group test pytest>=8.4.1
```

### 🚀 CI/CD

GitHub Actions 已配置使用 uv ：

```yaml
- name: ⚡ 安装 uv
  uses: astral-sh/setup-uv@v4
  with:
    enable-cache: true
    cache-dependency-glob: "uv.lock"

- name: 📦 同步依赖
  run: uv sync --group test --group reports

- name: 🧪 运行测试
  run: ENV=dev uv run pytest
```

### 📝 依赖组说明

- **test**: 测试框架相关依赖 (pytest, pytest-cov, pytest-xdist)
- **reports**: 测试报告相关依赖 (allure-pytest, pytest-html)
- **lint**: 代码质量工具 (暂时注释)
- **api**: API测试专用工具 (暂时注释)
- **dev**: 开发工具 (暂时注释)

### ⚠️ 注意事项

1. **不再使用requirements.txt** == 所有依赖管理通过 pyproject.toml 和 uv.lock
2. **使用uv.lock** == 确保依赖版本锁定，保证环境一致性
3. **分组管理** == 按功能分组依赖，按需安装
