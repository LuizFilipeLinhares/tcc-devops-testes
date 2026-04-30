from http.server import SimpleHTTPRequestHandler
from socketserver import ThreadingTCPServer
from functools import partial
from pathlib import Path
import threading
import pytest

@pytest.fixture(scope="session", autouse=True)
def http_server():
    app_dir = Path(__file__).resolve().parent.parent / "app"
    handler = partial(SimpleHTTPRequestHandler, directory=str(app_dir))

    class ReuseHTTPServer(ThreadingTCPServer):
        allow_reuse_address = True

    server = ReuseHTTPServer(("127.0.0.1", 0), handler)
    port = server.server_address[1]

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    yield f"http://127.0.0.1:{port}"

    server.shutdown()
    server.server_close()
    thread.join(timeout=1)