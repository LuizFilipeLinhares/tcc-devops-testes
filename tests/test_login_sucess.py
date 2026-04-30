from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_login_com_sucesso(driver):
    driver.get("http://127.0.0.1:8000/login.html")

    driver.find_element(By.ID, "email").send_keys("admin@test.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 5).until(EC.url_contains("index.html"))

    assert "index.html" in driver.current_url
