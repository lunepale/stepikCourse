from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
button = browser.find_element_by_css_selector("button#book.btn.btn-primary").click()

x1 = browser.find_element_by_css_selector("span#input_value.nowrap")
x = x1.text
result = calc(x)

input1 = browser.find_element_by_css_selector("input#answer.form-control")
input1.send_keys(result)
browser.find_element_by_css_selector("button#solve.btn.btn-primary").click()

