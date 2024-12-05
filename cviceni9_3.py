from unittest.mock import MagicMock
import requests

class Result:
    def __init__(self, content):
        self.content = content
def stahuj(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.content
    
def test_stahuj():
    requests.get = MagicMock(return_value=Result("abc"))
    assert stahuj("https://python.cz") == "abc"