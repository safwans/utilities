from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from AirbnbHomesDB import AirbnbHomesDB

# URL_TOP_RATED_HOMES = 'https://www.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3A13ef1a9a-e457-4d8c-a8e5-add199c76c59%7Cst%3AHOME_GROUPING_TOP_REVIEWED&rank_mode=top_rated&title_type=TOP_REVIEWED_HOMES&allow_override%5B%5D=&s_tag=oUNrWV5z'
URL_TOP_RATED_HOMES = 'https://www.airbnb.com/s/plus_homes?refinement_paths%5B%5D=%2Fselect_homes&click_referer=t%3ASEE_ALL%7Csid%3A080a23d5-653e-40f4-836d-dffc4db5d2d9%7Cst%3AHOME_GROUPING_SELECT_HOMES&superhost=false&guests=0&adults=0&children=0&title_type=SELECT_GROUPING&allow_override%5B%5D=&s_tag=bPQPWbrq'
CSS_HOME_LINK = 'div._1szwzht > a'
CSS_HOME_NAME = CSS_HOME_LINK + ' > span'
CSS_HOME_IMAGE = CSS_HOME_LINK + '  div._1df8dftk'
#_1wcpzyga _e296pg _gig1e7

class AirbnbHomesScrapper:
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/safwans/gdrive/software/packages/chromedriver')
        self.wait = WebDriverWait(self.driver, 10)

    def get_links(self):
        """Extracts and returns company links (maximum number of company links for return is provided)."""
        self.driver.get(URL_TOP_RATED_HOMES)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_HOME_LINK)))
        print("Found List Item")
        home_count = 0
        prev_count = 0
        target_count = 5000
        home_names = []
        home_links = []
        home_images = []
        
        while home_count < target_count:
          self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          home_links_selector = self.driver.find_elements_by_css_selector(CSS_HOME_LINK)
          home_names_selector = self.driver.find_elements_by_css_selector(CSS_HOME_NAME)
          home_images_selector = self.driver.find_elements_by_css_selector(CSS_HOME_IMAGE)
          temp_links = [home_link.get_attribute("href")
                         for home_link in home_links_selector]
          temp_names = [home_name.text
                         for home_name in home_names_selector]
          temp_images = [re.findall(r'url\(\"(.*\.jpg).*', home_image.get_attribute("style"))[0]
                         for home_image in home_images_selector]

#           print("\n".join(home_images_selector))

          
#           temp_homes = [home_detail.text
#                 for home_detail in self.driver.find_elements_by_css_selector(CSS_HOME_LIST_ITEM)]
          home_names += temp_names
          home_links.extend(temp_links)
          home_images.extend(temp_images)
          home_count = len(home_names)
          if home_count == prev_count:
            break
          else:
            prev_count = home_count
          
#             self.wait.until(lambda driver: self.get_last_line_number() != last_line_number)
#             last_line_number = self.get_last_line_number()
#         print("\n".join(home_names))
#         print("\n".join(home_links))
        print("\n".join(home_images))
        return home_names, home_links, home_images

    def get_company_data(self, company_link):
        """Extracts and prints out company specific information."""
        self.driver.get(company_link)

        return {
            row.find_element_by_css_selector(".company-info-card-label").text: row.find_element_by_css_selector(".company-info-card-data").text
            for row in self.driver.find_elements_by_css_selector('.company-info-card-table > .columns > .row')
        }

if __name__ == '__main__':
    print("Starting")
    scraper = AirbnbHomesScrapper()

    home_names, home_links, home_images = scraper.get_links()
    
    airbnb_homes_db = AirbnbHomesDB()
#     
    for index in range(len(home_names)):
      airbnb_homes_db.save(home_names[index], home_links[index], home_images[index])



# Airbnb URLs

# Top Rated Homes
#https://www.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3A13ef1a9a-e457-4d8c-a8e5-add199c76c59%7Cst%3AHOME_GROUPING_TOP_REVIEWED&rank_mode=top_rated&title_type=TOP_REVIEWED_HOMES&allow_override%5B%5D=&s_tag=oUNrWV5z

# AirBnB Plus
#https://www.airbnb.com/s/plus_homes?refinement_paths%5B%5D=%2Fselect_homes&click_referer=t%3ASEE_ALL%7Csid%3A080a23d5-653e-40f4-836d-dffc4db5d2d9%7Cst%3AHOME_GROUPING_SELECT_HOMES&superhost=false&guests=0&adults=0&children=0&title_type=SELECT_GROUPING&allow_override%5B%5D=&s_tag=bPQPWbrq

