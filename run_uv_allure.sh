#!/bin/bash

# uv + Allure 一键测试脚本
# 使用 uv 管理依赖，运行测试并生成 Allure 报告

set -e

# 颜色输出
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 uv + Allure 测试运行脚本${NC}"

# 1. 同步依赖
echo -e "${YELLOW}📦 同步 uv 依赖...${NC}"
uv sync --group reports

# 2. 清理旧报告
echo -e "${YELLOW}🧹 清理旧报告...${NC}"
rm -rf .report/

# 3. 运行测试（支持传入参数）
echo -e "${YELLOW}🧪 运行测试...${NC}"
if [ $# -eq 0 ]; then
    # 无参数时运行所有测试
    ENV=dev uv run pytest tests/
else
    # 有参数时运行指定测试
    ENV=dev uv run pytest "$@"
fi

# 4. 生成 Allure 报告
echo -e "${YELLOW}📊 生成 Allure 报告...${NC}"
allure generate .report/allure-results -o .report/allure-report --clean

# 5. 打开报告
echo -e "${GREEN}✅ 测试完成！正在打开 Allure 报告...${NC}"
allure open .report/allure-report

echo -e "${GREEN}🎉 所有任务完成！${NC}"
