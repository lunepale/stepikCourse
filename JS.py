import time
import math
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()
browser.get("https://suninjuly.github.io/execute_script.html")
x1 = browser.find_element_by_css_selector("span#input_value.nowrap")
x = x1.text
result = calc(x)
form = browser.find_element_by_css_selector("form")
browser.execute_script("return arguments[0].scrollIntoView(true);", form)

answer = browser.find_element_by_css_selector("input#answer.form-control")
answer.send_keys(result)
check = browser.find_element_by_css_selector("input#robotCheckbox.form-check-input").click()
radio = browser.find_element_by_css_selector("input#robotsRule.form-check-input").click()
button = browser.find_element_by_css_selector("button.btn.btn-primary").click()


