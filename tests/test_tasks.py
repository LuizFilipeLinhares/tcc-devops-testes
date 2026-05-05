from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def _login(driver, base_url):
    driver.get(f"{base_url}/login.html")
    driver.find_element(By.ID, "email").send_keys("admin@test.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 5).until(EC.url_contains("index.html"))


def test_adicionar_tarefa_aparece_na_lista(driver, http_server):
    _login(driver, http_server)

    driver.find_element(By.ID, "task-input").send_keys("Estudar DevOps")
    driver.find_element(By.ID, "add-task-button").click()

    tasks = driver.find_elements(By.CSS_SELECTOR, ".task-item")
    texts = [t.find_element(By.CLASS_NAME, "task-text").text for t in tasks]

    assert "Estudar DevOps" in texts


def test_adicionar_tarefa_vazia_exibe_erro(driver, http_server):
    _login(driver, http_server)

    driver.find_element(By.ID, "add-task-button").click()

    error = driver.find_element(By.ID, "task-error").text
    assert "Digite o nome da tarefa" in error


def test_marcar_tarefa_como_concluida(driver, http_server):
    _login(driver, http_server)

    driver.find_element(By.ID, "task-input").send_keys("Tarefa para concluir")
    driver.find_element(By.ID, "add-task-button").click()

    checkbox = driver.find_element(By.CSS_SELECTOR, ".task-item input[type='checkbox']")
    checkbox.click()

    task_item = driver.find_element(By.CSS_SELECTOR, ".task-item")
    assert "done" in task_item.get_attribute("class")


def test_deletar_tarefa_remove_da_lista(driver, http_server):
    _login(driver, http_server)

    driver.find_element(By.ID, "task-input").send_keys("Tarefa para deletar")
    driver.find_element(By.ID, "add-task-button").click()

    driver.find_element(By.CSS_SELECTOR, ".btn-delete").click()

    tasks = driver.find_elements(By.CSS_SELECTOR, ".task-item")
    assert len(tasks) == 0


def test_lista_vazia_exibe_empty_state(driver, http_server):
    _login(driver, http_server)

    empty = driver.find_element(By.ID, "empty-state")
    assert empty.is_displayed()
    assert "Nenhuma tarefa" in empty.text
