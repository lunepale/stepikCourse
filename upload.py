import os
import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
input1 = browser.find_elements_by_css_selector("input.form-control")
for element in input1:
    element.send_keys("123")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element = browser.find_element_by_css_selector("[type='file']")
element.send_keys(file_path)
time.sleep(1)

button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()


