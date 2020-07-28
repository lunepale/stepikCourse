import time
import math
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")
xtreasure=browser.find_element_by_css_selector("img#treasure")
tresuarex=xtreasure.get_attribute("valuex")
x=tresuarex

y=calc(x)

input=browser.find_element_by_css_selector("input#answer")
input.send_keys(y)

check=browser.find_element_by_css_selector("input#robotCheckbox.check-input")
check.click()

radio=browser.find_element_by_css_selector("[id='robotsRule']")
radio.click()


button=browser.find_element_by_css_selector("button.btn.btn-default")
button.click()

time.sleep(10)

