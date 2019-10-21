""" Sample scrapper for cloud function. """
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup
#import re
#import pandas as pd
#import os
import time

def test_webdriver(event=None, context=None):
  #launch url
  url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"
  
  driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
  driver.get('http://www.google.com/xhtml');
  time.sleep(5)
  search_box = driver.find_element_by_name('q')
  print(search_box)
  driver.quit()

if __name__ == '__main__':
  test_webdriver()