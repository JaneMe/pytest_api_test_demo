# Makefile for Allure testing automation

.PHONY: test allure-generate allure-open allure-test clean help

# 运行测试并生成 Allure 数据
test:
	@echo "🚀 运行测试生成 Allure 数据..."
	ENV=dev pytest tests/test_demo_allure.py

# 生成 Allure HTML 报告
allure-generate:
	@echo "📋 生成 Allure HTML 报告..."
	allure generate allure-results -o allure-report --clean

# 打开 Allure 报告
allure-open:
	@echo "🌐 打开 Allure 报告..."
	allure open allure-report

# 一键执行：测试 + 生成报告 + 打开
allure-test: test allure-generate allure-open

# 清理生成的文件
clean:
	@echo "🧹 清理 Allure 文件..."
	rm -rf allure-results allure-report

# 显示帮助信息
help:
	@echo "可用命令："
	@echo "  make test          - 运行测试生成数据"
	@echo "  make allure-generate - 生成 HTML 报告"
	@echo "  make allure-open   - 打开报告"
	@echo "  make allure-test   - 一键完成所有步骤"
	@echo "  make clean         - 清理生成的文件" 