import pytest
import requests

class TestJane:

    def test_jane(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status_code == 200
        # assert response.json()['userId'] == 1
        assert response.json()['id'] == 1
        assert response.json()['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
        assert response.json()['body'] == 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'