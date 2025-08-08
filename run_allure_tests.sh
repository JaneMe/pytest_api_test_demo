#!/bin/bash
# 一键生成并打开 Allure 报告

# 运行测试并生成 Allure 数据
ENV=dev pytest tests 
# 生成 Allure HTML 报告
allure generate .allure-results -o .allure-report --clean
# 打开 Allure 报告的两种方式： server or open
# allure server .allure-report 
allure open .allure-report 