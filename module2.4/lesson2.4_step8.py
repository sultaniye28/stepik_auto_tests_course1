import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()

try:
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    driver.find_element(By.ID, "book").click()
    driver.implicitly_wait(2)
    driver.execute_script("window.scrollBy(0, 100);")

    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    field = driver.find_element(By.ID, "answer")
    field.send_keys(y)
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
    time.sleep(2)
    driver.quit()

