import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


search_request = 'ноутбук'
url = 'https://www.citrus.ua'

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(10)

browser.get(url)
browser.implicitly_wait(10)

browser.find_element_by_css_selector('[name="search"]').send_keys(search_request)
browser.find_element_by_css_selector('[name="search"]').send_keys(Keys.ENTER)
browser.implicitly_wait(10)

actualResult = browser.find_element_by_css_selector('[class="result-title"]').text


expectedResult = "Результаты поиска: ноутбук"

assert actualResult == expectedResult

browser.close()
