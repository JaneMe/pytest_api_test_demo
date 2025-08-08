import allure
import requests


@allure.feature("Test example API")
class TestPytestAllureDemo:

    @allure.story("Test example get endpoint")
    @allure.title("验证 get 请求")
    @allure.description("验证 get 请求的响应状态码和响应数据")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_get_example_endpoint_allure(self, env_config, env_request_data, env_response_data):
        host = env_config["host"]
        get_api = env_config["getAPI"]
        get_api_request_data = env_request_data["getAPI"]
        get_api_response_data = env_response_data["getAPI"]
        # send get request
        response = requests.get(host + get_api)
        # assert
        print("响应状态码是" + str(response.status_code))
        assert response.status_code == 200
        print("响应数据是" + str(response.json()))
        assert response.json() == get_api_response_data

    @allure.story("测试 POST 请求")
    @allure.title("验证 POST 请求")
    @allure.description("验证 POST 请求的响应状态码和响应数据")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_post_example_endpoint_allure(self, env_config, env_request_data, env_response_data):
        host = env_config["host"]
        post_api = env_config["postAPI"]
        post_api_request_data = env_request_data["postAPI"]
        post_api_response_data = env_response_data["postAPI"]
        # send request
        response = requests.post(host + post_api, post_api_request_data)
        # assert
        print("response status code is" + str(response.status_code))
        assert response.status_code == 201
        print("response data is" + str(response.json()))
        # assert response.json() == post_api_response_data
        print(response.json())