import re
from bs4 import BeautifulSoup
from selenium import webdriver
import requests


req = requests.get('https://thepiratebays.com/')
soup = BeautifulSoup(req.text, features="html.parser")
search_input = soup.findAll(id=re.compile('search.{6}'))
# print()
# for inp in inputs:
#     print(inp)

# browser = webdriver.Chrome()
# browser.quit()

# browser.get('https://www.youtube.com/')
# print(browser.title)

# print(browser)
