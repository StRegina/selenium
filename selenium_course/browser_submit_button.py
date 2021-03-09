#1
#from selenium import webdriver

#browser = webdriver.Chrome()
#browser.get("http://suninjuly.github.io/simple_form_find_task.html")
#button = browser.find_element_by_id("submit_button")

#2
#from selenium import webdriver
#from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
#browser.get("http://suninjuly.github.io/simple_form_find_task.html")
#button = browser.find_element(By.ID, "submit_button")

#3
#from selenium import webdriver
#from selenium.webdriver.common.by import By

#link = "http://suninjuly.github.io/simple_form_find_task.html"
#browser = webdriver.Chrome()
#browser.get(link)
#button = browser.find_element(By.ID, "submit_button")
#button.click()

# закрываем браузер после всех манипуляций
#browser.quit()

#4 Для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()