from .connectionpool import HTTPConnectionPool

_pool = HTTPConnectionPool()

def request(host, path="/", method="GET"):
    conn = _pool.get_conn(host)

    req = (
        f"{method} {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "Connection: keep-alive\r\n\r\n"
    )

    conn.send(req)

    try:
        response = conn.sock.recv(4096).decode()
    finally:
        _pool.release(conn)

    return response
