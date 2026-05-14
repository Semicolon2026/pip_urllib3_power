from urllib3.request import request

def test_request_callable():
    assert callable(request)
