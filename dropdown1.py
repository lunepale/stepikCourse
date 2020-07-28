import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects2.html")

number1 = browser.find_element_by_css_selector("[id='num1']")
number1 = number1.text

number2 = browser.find_element_by_css_selector("[id='num2']")
number2 = number2.text
result=int(number1) + int(number2)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(result))

button=browser.find_element_by_css_selector("button.btn.btn-default").click()

