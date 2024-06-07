
from Socket import Socket

if __name__ == "__main__":
    server = Socket("localhost", 12345)
    server.start_server()
