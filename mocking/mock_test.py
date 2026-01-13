from unittest.mock import patch, MagicMock
from functions import greet_user

def test_greetfunction():
    fake_response = MagicMock()
    fake_response.json.return_value = {"name": "Ei Phyu Sinn"}

    with patch("functions.requests.get", return_value=fake_response):
        assert greet_user(1) == "Hello Ei Phyu Sinn"
