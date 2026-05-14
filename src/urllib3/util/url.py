from urllib.parse import urlparse

def parse_url(url: str):
    return urlparse(url)
