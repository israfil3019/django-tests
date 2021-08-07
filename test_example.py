from selenium import webdriver

browser = webdriver.Edge()

browser.get('https://github.com/israfil3019')

assert browser.page_source.find('israfil')