# conftest.py 集中管理固件
import pytest
import json
import os


# 获取当前文件的目录，这就是项目根目录
project_root = os.path.dirname(os.path.abspath(__file__))

# 获取配置文件
@pytest.fixture(scope="session")
def env_config(request):
    # 获取不同环境的配置文件
    env = os.getenv('ENV', 'test')
    with open(f'{project_root}/config/{env}_config.json', 'r') as config_file:
        config = json.load(config_file)
    return config


@pytest.fixture(scope="session")
def env_request_data(request):
    # 获取不同环境的请求数据文件
    env = os.getenv('ENV', 'test')
    with open(f'{project_root}/data/{env}_request_data.json', 'r') as request_data_file:
        request_data = json.load(request_data_file)
    return request_data


@pytest.fixture (scope="session")
def env_response_data(request):
    # 获取不同环境的响应数据文件
    env = os.getenv('ENV', 'test')
    with open(f'{project_root}/data/{env}_response_data.json', 'r') as response_data_file:
        response_data = json.load(response_data_file)
    return response_data