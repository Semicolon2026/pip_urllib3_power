from urllib3.connectionpool import HTTPConnectionPool

def test_pool_creation():
    pool = HTTPConnectionPool()
    assert pool.pools == {}
