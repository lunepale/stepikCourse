from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    elements = browser.find_elements_by_css_selector("div.second_block input.form-control")
    for element in elements:
        element.send_keys("123")
    element1=browser.find_element_by_css_selector("div.first_block input.form-control.first")
    element1.send_keys("1234")

    element2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    element2.send_keys("1234")

    element3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
    element3.send_keys("1234")
    time.sleep(5)

    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()