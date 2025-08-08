import requests


class TestPytestDemo:

    def test_get_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"
        # SEND REQUEST
        response = requests.get(f"{base_url}/posts/1")
        # ASSERT
        assert response.status_code == 200
        assert response.json()['userId'] == 1
        assert response.json()['id'] == 1

    def test_post_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"
        requests_data = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        # SEND REQUEST
        response = requests.post(f"{base_url}/posts", requests_data)
        # ASSERT
        assert response.status_code == 201
        print(response.json())
        assert response.json()['userId'] == '1'
        assert response.json()['id'] == 101