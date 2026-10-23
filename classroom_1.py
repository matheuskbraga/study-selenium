from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


#driver_browser = webdriver.Chrome()
driver_browser = webdriver.Firefox() # identificar e abrir browser
driver_browser.get("https://www.selenium.dev/selenium/web/web-form.html") # acessar site

text_box = driver_browser.find_element(by=By.NAME, value="my-text") # encontrar elemento html
text_box.send_keys("Selenium") # interagir com o elemento

submit_button = driver_browser.find_element(by=By.CSS_SELECTOR, value="button") # encontrar elemento html
submit_button.click() # interagir com o elemento


sleep(30)