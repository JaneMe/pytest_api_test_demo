#!/bin/bash

# 统一测试运行脚本
# 使用 uv 管理依赖，运行测试并生成 Allure 报告
# 用法: ./run_test.sh [env] [pytest_args...]
# 例如: ./run_test.sh dev
#       ./run_test.sh prod -m smoke
#       ./run_test.sh test tests/test_demo.py

set -e

# 颜色输出
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 统一测试运行脚本${NC}"

# 1. 同步依赖，确保所有依赖都被安装
echo -e "${YELLOW}📦 同步 uv 依赖...${NC}"
uv sync --all-groups

# 2. 清理旧报告
echo -e "${YELLOW}🧹 清理旧报告...${NC}"
rm -rf .report/

# 3. 确定测试环境和参数
ENV=${1:-dev}  # 第一个参数作为环境，默认为 dev
shift 2>/dev/null || true  # 移除第一个参数，剩余的作为 pytest 参数

echo -e "${YELLOW}🧪 运行测试 (环境: ${ENV})...${NC}"

# 根据环境设置不同的测试策略
case $ENV in
    "dev"|"development")
        echo -e "${BLUE}📋 开发环境: 运行所有测试${NC}"
        if [ $# -eq 0 ]; then
            ENV=dev uv run pytest tests/ -v
        else
            ENV=dev uv run pytest "$@" -v
        fi
        ;;
    "test"|"testing")
        echo -e "${BLUE}📋 测试环境: 运行回归测试${NC}"
        if [ $# -eq 0 ]; then
            ENV=test uv run pytest tests/ -m "regression or api" -v
        else
            ENV=test uv run pytest "$@" -v
        fi
        ;;
    "prod"|"production")
        echo -e "${BLUE}📋 生产环境: 只运行冒烟测试${NC}"
        if [ $# -eq 0 ]; then
            ENV=prod uv run pytest tests/ -m smoke -v --tb=short
        else
            ENV=prod uv run pytest "$@" -v --tb=short
        fi
        ;;
    "ci")
        echo -e "${BLUE}📋 CI环境: 并行运行所有测试${NC}"
        if [ $# -eq 0 ]; then
            ENV=test uv run pytest tests/ -n auto -v --tb=short
        else
            ENV=test uv run pytest "$@" -n auto -v --tb=short
        fi
        ;;
    "parallel"|"fast")
        echo -e "${BLUE}📋 快速模式: 并行运行测试${NC}"
        if [ $# -eq 0 ]; then
            ENV=dev uv run pytest tests/ -n auto -v
        else
            ENV=dev uv run pytest "$@" -n auto -v
        fi
        ;;
    *)
        echo -e "${BLUE}📋 自定义环境 (${ENV}): 运行指定测试${NC}"
        if [ $# -eq 0 ]; then
            ENV=$ENV uv run pytest tests/ -v
        else
            ENV=$ENV uv run pytest "$@" -v
        fi
        ;;
esac

# 4. 生成 Allure 报告
echo -e "${YELLOW}📊 生成 Allure 报告...${NC}"
allure generate .report/allure-results -o .report/allure-report --clean

# 5. 打开报告
echo -e "${GREEN}✅ 测试完成！正在打开 Allure 报告...${NC}"
allure open .report/allure-report

echo -e "${GREEN}🎉 所有任务完成！${NC}"
