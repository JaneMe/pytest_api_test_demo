# conftest.py 集中管理固件
    - 根据环境加载配置文件
    - 根据环境加载请求数据
    - 根据环境加载响应文件

## 根据不同环境运行测试用例命令
    ```
    ENV=dev pytest test_case/test_demo_multi_environment.py
    ENV=test pytest test_case/test_demo_multi_environment.py
    ENV=prod pytest test_case/test_demo_multi_environment.py
    ```
## 执行时序
    固件阶段：pytest 先执行所有需要的固件（conftest.py），加载配置和数据文件
    注入阶段：将固件返回的数据作为参数传递给测试函数
    测试阶段：测试函数开始执行，直接使用已经准备好的数据

## 测试分层执行
    冒烟测试：只执行 blocker 和 critical 级别
    pytest --allure-severities=blocker,critical

    回归测试：执行 blocker、critical、normal 级别  
    pytest --allure-severities=blocker,critical,normal

    完整测试：执行所有级别
    pytest

## Allure 装饰器 @allure.severity 应使用常量传参而非字符串
    使用枚举常量方式的优势：
        1. 类型安全和错误检测
        2. 智能提示和自动补全
        3. 重构安全
        4. 代码可读性高
        5. 避免魔法字符串
    团队规范建议：
        统一使用 @allure.severity(allure.severity_level.XXX) 格式
        禁用字符串 方式避免拼写错误
        配置 IDE 启用静态检查和自动补全
        代码审查时检查是否使用了正确的枚举方式

## 执行用例并生成 Allure 测试报告
    bash run_allure_tests.sh 脚本运行：
        ./run_allure_tests.sh 
        sh run_allure_tests.sh
        bash run_allure_tests.sh 
    
