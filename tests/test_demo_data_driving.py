import requests
import json
import os

# 获取当前文件的目录，然后构建到项目根目录的路径
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)  # 上一级目录（项目根目录）

# 从配置文件中获取测试配置信息
config_path = os.path.join(project_root, "config", "test_config.json")
with open(config_path, "r") as json_file:
    config = json.load(json_file)

# 从测试数据文件中获取请求数据
request_data_path = os.path.join(project_root, "data", "test_request_data.json")
with open(request_data_path, 'r') as json_file:
    request_data = json.load(json_file)

# 从测试数据文件中获取响应数据
response_data_path = os.path.join(project_root, "data", "test_response_data.json")
with open(response_data_path, 'r') as json_file:
    response_data = json.load(json_file)


class TestPytestDemo:

    def test_get_demo(self):
        host = config.get("host")
        get_api = config.get("getAPI")
        get_api_response_data = response_data.get("getAPI")
        # send request
        response = requests.get(host+get_api)
        # assert
        assert response.status_code == 200
        assert response.json() == get_api_response_data

    def test_post_demo(self):
        # 获取配置信息
        host = config.get("host")
        # 获取请求数据
        post_api = config.get("postAPI")
        post_api_request_data = request_data.get("postAPI")
        # 获取响应数据
        post_api_response_data = response_data.get("postAPI")
        # 发送请求
        response = requests.post(host + post_api, post_api_request_data)
        
        """ 检查响应状态码 """
        assert response.status_code == 201
        
        """ 检查响应耗时 """
        assert response.elapsed.total_seconds() < 3

        """ 检查响应 URL """    
        # 检查响应 URL 是否包含 postAPI 字符串
        assert post_api in response.url
        # 检查响应 URL 是否以 host 开头
        assert response.url.startswith(host)
        # 检查响应 URL 是否以 postAPI 结尾
        assert response.url.endswith(post_api)
        
        """ 检查响应头 """
        # 检查响应头是否包含特定字段
        # print(response.headers)
        assert 'Content-Type' in response.headers
        assert 'Content-Length' in response.headers
        assert 'Date' in response.headers
        assert 'Server' in response.headers
        # 检查响应头字段值是否与预期数据一致
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        assert response.headers['Content-Length'] == str(len(response.text))
        assert response.headers['Date'] == response.headers['Date']
        assert response.headers['Server'] == 'cloudflare'


        """ 检查响应体 """
        # 检查响应体是否包含 title、body、userId、id 字段
        assert 'title' in response.json()
        assert 'body' in response.json()
        assert 'userId' in response.json()
        assert 'id' in response.json()
        # 检查响应体字段值是否与预期数据一致
        assert response.json()['title'] == post_api_response_data['title']
        assert response.json()['body'] == post_api_response_data['body']
        # assert response.json()['userId'] == post_api_response_data['userId']
        assert response.json()['id'] == post_api_response_data['id']

        """ 检查响应内容编码 """
        # 检查响应内容编码是否为utf-8
        assert response.encoding == 'utf-8'

        """ 检查响应内容长度 """
        # 检查响应内容长度是否小于1000
        assert len(response.text) < 1000