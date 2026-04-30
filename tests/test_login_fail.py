from selenium.webdriver.common.by import By


def test_login_com_falha(driver):
    driver.get("http://127.0.0.1:8000/login.html")
    driver.get(f"{http_server}/login.html")

    driver.find_element(By.ID, "email").send_keys("erro@test.com")
    driver.find_element(By.ID, "password").send_keys("senha_errada")
    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(By.ID, "error-message").text

    assert "Email ou senha inválidos" in error_message

