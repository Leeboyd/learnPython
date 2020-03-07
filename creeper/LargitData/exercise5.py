import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

browser = webdriver.Firefox()
browser.get("https://www.agoda.com/zh-tw/search?asq=NQVGXW6jsE3tbdY9S%2BqUCrtlrBvgbZWPCWcTs5yGDQUTcZFzo3lmB4hod%2FJCcXbIJQnJ9Okma6a7bP1a%2FrMbI2XTHaUyOaiMwoCVZax2nzkJ5B%2BOxW2foSB5q4qGW2HpxDftxzeeUD4leEKmfR6%2FVXMA6GWbclz8p2pOBplSeqqrYUxlAws10aWdGwt4ajNMikrSP3cx4715NAYXt0MMqf5JlA5NuTTnQUzzmtT29TE%3D&city=13899&cid=1844104&tick=637195599047&languageId=20&userId=b12b206d-de1e-4443-8ed6-1a29987677ea&sessionId=malrd1oqxewyvosv5bmjgfpy&pageTypeId=1&origin=TW&locale=zh-TW&aid=130589&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=b12b206d-de1e-4443-8ed6-1a29987677ea&prid=0&checkIn=2020-03-23&checkOut=2020-03-25&rooms=1&adults=2&children=0&priceCur=TWD&los=2&textToSearch=%E8%8A%9D%E5%8A%A0%E5%93%A5(IL)&travellerType=1&familyMode=off&productType=-1&sort=agodaRecommended")
time.sleep(1)

soup = BeautifulSoup(browser.page_source, 'html.parser')
try:
  while soup.select('#paginationNext'):
    for title in soup.select('.InfoBox__HotelTitle'):
      print(title.text)
    time.sleep(1)
    browser.find_element(By.ID, "paginationNext").click()
except Exception as e:
  browser.close()