import time
import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x1 = browser.find_element_by_css_selector("span#input_value.nowrap")
x = x1.text
result = calc(x)

input1 = browser.find_element_by_css_selector("input#answer.form-control")
input1.send_keys(result)
browser.find_element_by_css_selector("button.btn.btn-primary").click()

