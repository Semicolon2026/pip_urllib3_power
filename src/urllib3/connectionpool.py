from collections import defaultdict
from .connection import HTTPConnection

class HTTPConnectionPool:
    def __init__(self):
        self.pools = defaultdict(list)

    def get_conn(self, host, port=80):
        key = (host, port)

        if self.pools[key]:
            return self.pools[key].pop()

        return HTTPConnection(host, port)

    def release(self, conn):
        key = (conn.host, conn.port)
        self.pools[key].append(conn)
