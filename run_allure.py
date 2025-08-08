#!/usr/bin/env python3
"""
Allure 测试自动化脚本
"""
import os
import subprocess
import sys
import argparse


def run_command(command, description):
    """执行命令并处理错误"""
    print(f"🔄 {description}")
    print(f"   执行命令: {command}")
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ {description} - 成功")
        if result.stdout:
            print(f"   输出: {result.stdout.strip()}")
    else:
        print(f"❌ {description} - 失败")
        print(f"   错误: {result.stderr.strip()}")
        return False
    return True


def run_tests(env="dev", test_file="tests/test_demo_allure.py"):
    """运行 pytest 测试"""
    command = f"ENV={env} pytest {test_file}"
    return run_command(command, "运行 pytest 测试")


def generate_report(results_dir=".allure-results", report_dir=".allure-report"):
    """生成 Allure HTML 报告"""
    command = f"allure generate {results_dir} -o {report_dir} --clean"
    return run_command(command, "生成 Allure HTML 报告")


def open_report(report_dir=".allure-report"):
    """打开 Allure 报告"""
    command = f"allure open {report_dir}"
    print(f"🌐 打开 Allure 报告")
    print(f"   执行命令: {command}")
    subprocess.Popen(command, shell=True)
    print("✅ 报告服务器已启动，请在浏览器中查看")


def clean_reports(results_dir=".allure-results", report_dir=".allure-report"):
    """清理生成的文件"""
    print("🧹 清理 Allure 文件")
    for directory in [results_dir, report_dir]:
        if os.path.exists(directory):
            run_command(f"rm -rf {directory}", f"删除 {directory}")


def main():
    parser = argparse.ArgumentParser(description="Allure 测试自动化工具")
    parser.add_argument("--env", default="dev", help="测试环境 (默认: dev)")
    parser.add_argument("--test-file", default="tests/test_demo_allure.py", help="测试文件路径")
    parser.add_argument("--no-open", action="store_true", help="不自动打开报告")
    parser.add_argument("--clean", action="store_true", help="只清理文件，不运行测试")
    
    args = parser.parse_args()
    
    if args.clean:
        clean_reports()
        return
    
    print("🚀 开始 Allure 测试自动化流程")
    print("=" * 50)
    
    # 1. 运行测试
    if not run_tests(args.env, args.test_file):
        print("❌ 测试失败，停止执行")
        sys.exit(1)
    
    # 2. 生成报告
    if not generate_report():
        print("❌ 报告生成失败，停止执行")
        sys.exit(1)
    
    # 3. 打开报告
    if not args.no_open:
        open_report()
    
    print("=" * 50)
    print("✅ Allure 测试流程完成")


if __name__ == "__main__":
    main() 