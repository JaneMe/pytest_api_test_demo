# run_test.sh 脚本执行示例

```bash
# 默认开发环境
./run_test.sh

# 生产环境冒烟测试
./run_test.sh prod

# 测试环境回归测试
./run_test.sh test

# CI环境并行测试
./run_test.sh ci

# 自定义参数
./run_test.sh dev -m smoke
./run_test.sh prod tests/test_demo.py
```

> 💡 详细使用指南请参考：[测试运行指南.md](./测试运行指南.md)