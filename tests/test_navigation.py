from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_logout_redireciona_para_login(driver, http_server):
    driver.get(f"{http_server}/login.html")

    driver.find_element(By.ID, "email").send_keys("admin@test.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 5).until(EC.url_contains("index.html"))

    driver.find_element(By.ID, "logout-button").click()

    WebDriverWait(driver, 5).until(EC.url_contains("login.html"))

    assert "login.html" in driver.current_url
