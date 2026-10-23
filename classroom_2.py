from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Inicializa o navegador Chrome
driver = webdriver.Chrome()

try:
    # 2. Abre a página desejada
    driver.get("https://google.com")
    
    # Dá tempo para a página carregar
    time.sleep(5)
    
    # 3. Localiza a barra de pesquisa usando XPATH relativo
    # Procuramos uma tag <textarea> que possui o atributo name='q'
    barra_pesquisa = driver.find_element(By.XPATH, "//textarea[@name='q']")
    
    # 4. Interage com o elemento encontrado
    barra_pesquisa.send_keys("Selenium WebDriver")
    
    # Pressiona Enter para realizar a busca
    barra_pesquisa.send_keys(Keys.ENTER)
    
    # Aguarda 5 segundos para você ver o resultado da busca
    time.sleep(5)

finally:
    # 5. Fecha o navegador e encerra o processo do driver
    driver.quit()
