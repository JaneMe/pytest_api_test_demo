# Pytest API 测试框架 Demo

一个基于 Pytest 的 API 自动化测试框架，支持多环境配置、数据驱动测试和 Allure 报告生成。

## 📋 项目特性

- 🚀 **多环境支持**：dev/test/prod 环境配置切换
- 📊 **数据驱动**：支持外部数据文件驱动测试
- 📋 **Allure 报告**：美观的测试报告生成
- 🔄 **并行执行**：支持多线程测试执行
- 🛠️ **自动化工具**：Makefile 快速操作命令
- 📁 **隐藏目录**：测试报告存储在隐藏目录中

## 🏗️ 项目结构

```
pytest_api_test_demo/
├── config/                     # 环境配置文件
│   ├── dev_config.json        # 开发环境配置
│   ├── test_config.json       # 测试环境配置
│   └── prod_config.json       # 生产环境配置
├── data/                       # 测试数据文件
│   ├── dev_request_data.json   # 开发环境请求数据
│   ├── dev_response_data.json  # 开发环境响应数据
│   ├── test_request_data.json  # 测试环境请求数据
│   ├── test_response_data.json # 测试环境响应数据
│   ├── prod_request_data.json  # 生产环境请求数据
│   └── prod_response_data.json # 生产环境响应数据
├── tests/                      # 测试用例目录
│   ├── test_demo.py           # 基础测试示例
│   ├── test_demo_allure.py    # Allure 报告测试
│   ├── test_demo_data_driving.py # 数据驱动测试
│   ├── test_demo_multi_environment.py # 多环境测试
│   ├── test_login.py          # 登录接口测试
│   ├── test_order.py          # 订单接口测试
│   └── test_jane.py           # 自定义测试
├── utils/                      # 工具类
│   └── config_manager.py      # 配置管理工具
├── conftest.py                # Pytest 配置和固件
├── pytest.ini                # Pytest 配置文件
├── requirements.txt           # 项目依赖
├── Makefile                   # 自动化命令
├── run_allure.py             # Allure 运行脚本
├── run_allure_tests.sh       # Allure 测试脚本
└── demoAPI.md                # API 接口文档
```

## 🔧 环境准备

### 系统要求

- Python 3.7+
- pip (Python 包管理器)

### 安装依赖

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

### 安装 Allure

```bash
# macOS
brew install allure

# Windows (需要 Java 环境)
# 下载 allure-commandline 并配置环境变量
```

## 🚀 快速开始

### 基础测试运行

```bash
# 运行所有测试
pytest

# 运行指定测试文件
pytest tests/test_demo.py

# 运行指定测试类
pytest tests/test_demo.py::TestPytestDemo

# 运行指定测试方法
pytest tests/test_demo.py::TestPytestDemo::test_get_demo
```

### 多环境测试

```bash
# 测试环境（默认）
ENV=test pytest tests/

# 开发环境
ENV=dev pytest tests/

# 生产环境
ENV=prod pytest tests/
```

### Allure 报告

```bash
# 使用 Makefile 快速操作
make test              # 运行测试生成数据
make allure-generate   # 生成 HTML 报告
make allure-open       # 打开报告
make allure-test       # 一键完成所有步骤
make clean             # 清理生成的文件
make help              # 显示帮助信息
```

### 并行测试

```bash
# 使用 pytest-xdist 并行执行
pytest -n auto  # 自动检测 CPU 核心数
pytest -n 4     # 指定 4 个进程
```

## 📊 测试报告

项目支持多种测试报告格式：

- **HTML 报告**：生成在 `.report-html/` 目录
- **Allure 报告**：生成在 `.allure-report/` 目录
- **终端输出**：实时显示测试结果

### 报告目录说明

根据项目规范，所有测试报告都存储在隐藏目录中：

```
.allure-results/    # Allure 原始数据
.allure-report/     # Allure HTML 报告
.report-html/       # Pytest HTML 报告
.reports/           # 其他报告文件
```

## 🛠️ 配置说明

### pytest.ini 配置

```ini
[pytest]
addopts = -vs -rf --html=.report-html/pytest_report.html --self-contained-html --alluredir=.allure-results
```

- `-v`：详细输出
- `-s`：显示 print 输出
- `-rf`：显示失败的测试摘要
- `--html`：生成 HTML 报告
- `--alluredir`：指定 Allure 数据目录

### 环境配置

在 `config/` 目录下的 JSON 文件用于配置不同环境的参数：

```json
{
  "host": "https://jsonplaceholder.typicode.com",
  "getAPI": "/posts/1",
  "postAPI": "/posts"
}
```

## 📝 编写测试用例

### 基础测试示例

```python
import requests

class TestAPI:
    def test_get_posts(self, env_config):
        url = f"{env_config['host']}{env_config['getAPI']}"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json()['userId'] == 1
```

### 使用数据驱动

```python
def test_with_data(self, env_request_data, env_response_data):
    # 使用外部数据文件进行测试
    request_data = env_request_data['test_case_1']
    expected_response = env_response_data['test_case_1']
    # 测试逻辑...
```

## 🔍 API 接口文档

详细的 API 接口文档请参考 [demoAPI.md](demoAPI.md)

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

该项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 📞 联系方式

如有问题或建议，欢迎提交 Issue 或联系项目维护者。

---

**Happy Testing! 🎉**
# pytest_api_test_demo
