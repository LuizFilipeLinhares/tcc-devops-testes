from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_campos_vazios_exibe_erro(driver, http_server):
    driver.get(f"{http_server}/login.html")

    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(By.ID, "error-message").text

    assert "Preencha todos os campos" in error_message


def test_apenas_email_exibe_erro(driver, http_server):
    driver.get(f"{http_server}/login.html")

    driver.find_element(By.ID, "email").send_keys("admin@test.com")
    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(By.ID, "error-message").text

    assert "Preencha todos os campos" in error_message


def test_apenas_senha_exibe_erro(driver, http_server):
    driver.get(f"{http_server}/login.html")

    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(By.ID, "error-message").text

    assert "Preencha todos os campos" in error_message


def test_acesso_direto_index_sem_login_redireciona(driver, http_server):
    driver.get(f"{http_server}/index.html")

    WebDriverWait(driver, 5).until(EC.url_contains("login.html"))

    assert "login.html" in driver.current_url
