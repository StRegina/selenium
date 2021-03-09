from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не станет 100$
element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button1 = browser.find_element_by_css_selector("button.btn")
button1.click()

# скроллим страницу
button2 = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)

# Посчитаетт математическую функцию от x
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

# Ваш код, который заполняет обязательные поля
input = browser.find_element_by_id("answer")
input.send_keys(y)

# Отправляем заполненную форму
button2.click()

# закрываем браузер после всех манипуляций
browser.quit()