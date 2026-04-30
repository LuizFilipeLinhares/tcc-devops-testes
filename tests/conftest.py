
import os
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PORT = 8000

@pytest.fixture(scope="session", autouse=True)
def http_server():
    app_dir = Path(__file__).resolve().parent.parent / "app"
    handler = partial(SimpleHTTPRequestHandler, directory=str(app_dir))
    server = ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    yield

    server.shutdown()
    thread.join()

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    yield driver
    driver.quit()
