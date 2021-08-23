from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.ryanbaird.com')
title = browser.title

print(title)