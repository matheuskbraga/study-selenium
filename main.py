from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


driver = webdriver.Firefox()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

text_box = driver.find_element(by=By.NAME, value="my-text")
text_box.send_keys("Selenium")

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button.click()


sleep(30)