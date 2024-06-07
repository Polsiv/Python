# pylint: skip-file
import util.log
from Socket import Socket

if __name__ == "__main__":
    util.log.log()
    server = Socket("localhost", 12345)
    server.start_server()
