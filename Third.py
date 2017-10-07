from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(18) > li:nth-child(1) > a:nth-child(1)')
elem.click()
browser.back()
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > p:nth-child(6)')
print elem.text
