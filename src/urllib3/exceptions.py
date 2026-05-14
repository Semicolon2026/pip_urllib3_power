class HTTPError(Exception):
    """Base exception for urllib3-style errors"""

class TimeoutError(HTTPError):
    pass

class ConnectionError(HTTPError):
    pass
