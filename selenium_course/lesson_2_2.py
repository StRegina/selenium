from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("select").click()
    #browser.find_element_by_css_selector("[value='85']").click()

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(int(num1) + int(num2)))

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()