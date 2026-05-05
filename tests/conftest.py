from http.server import SimpleHTTPRequestHandler
from socketserver import ThreadingTCPServer
from functools import partial
from pathlib import Path
import threading
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


@pytest.fixture(scope="session")
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


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280,720")

    chromedriver_path = os.environ.get("CHROMEDRIVER_PATH")
    if chromedriver_path:
        service = Service(executable_path=chromedriver_path)
        browser = webdriver.Chrome(service=service, options=options)
    else:
        browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()