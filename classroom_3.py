from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://exemplo.com")


# Aguarda até que o elemento esteja visível por no máximo 10 segundos
elemento = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "meuBotao"))
)

elemento.click()
