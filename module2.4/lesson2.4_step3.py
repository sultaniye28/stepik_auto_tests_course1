from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# try:
#     driver.implicitly_wait(5)
#     driver.get("https://suninjuly.github.io/wait1.html")
#     driver.find_element(By.ID, "verify").click()
#
#     message = driver.find_element(By.ID, "verify_message")
#     assert "successful" in message.text
# finally:
#     driver.quit()

driver.get("http://suninjuly.github.io/cats.html")
driver.find_element(By.ID, "button")
