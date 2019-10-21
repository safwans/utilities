'''
Created on Mar 1, 2019

@author: safwans
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import time

def simple_get():
  #launch url
  url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"
  
  driver = webdriver.Chrome('/Users/safwans/gdrive/software/packages/chromedriver')  # Optional argument, if not specified will search path.
  driver.get('http://www.google.com/xhtml');
  time.sleep(5)
  search_box = driver.find_element_by_name('q')
  print(search_box)

# # create a new Firefox session
# driver = webdriver.Chrome()
# driver.implicitly_wait(30)
# driver.get(url)
# 
# python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
# print(python_button)
# python_button.click() #click fhsu link

if __name__ == '__main__':
  simple_get()
#     url = 'https://www.airbnb.com/s/plus_homes'
#     div_class = '_14csrlku'
#     raw_html = simple_get(url)
#     print(raw_html)
#     display_p(raw_html) 