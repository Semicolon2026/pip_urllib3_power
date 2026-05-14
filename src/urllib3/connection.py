import socket

class HTTPConnection:
    def __init__(self, host, port=80, timeout=5):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None

    def connect(self):
        self.sock = socket.create_connection(
            (self.host, self.port),
            timeout=self.timeout
        )

    def send(self, data: str):
        if not self.sock:
            self.connect()
        self.sock.sendall(data.encode())

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None
