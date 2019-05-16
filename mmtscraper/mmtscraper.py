from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import bs4
import requests

class MmtScraper(object):
    def __init__(self, url, category):

        self.url = url+category
        self.category = category
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--incognito')
        #self.options.add_argument('--headless')                                         #can try headless but mmt blocks this
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\acer\Desktop\python\chromedriver_win32\chromedriver.exe",
                                       options=self.options)
        self.delay = 3
        
    #loading the url
    def load_mmt_url(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "deal-view-details")))
            print("Page is ready")
        except TimeoutException:
            print("Loading took too much time! seems like no offers on {} page".format(self.category))
    #getting offer links of each offer listed on current offer category page
    def extract_offer_links(self):
        all_link_elements = self.driver.find_elements_by_class_name("deal-view-details")
        for i in range(len(all_link_elements)):
            all_link_elements[i] = all_link_elements[i].get_attribute('href')

        return all_link_elements
    #requesting a offer page   
    def open_offer_link(self,link):
        try:
            response = requests.get(link,timeout=3)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
             print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)

        return response
    #extracting tagobjects with class = tblOffer
    def extract_table(self,response):

        soup = bs4.BeautifulSoup(response.text,'lxml')
        offer_table = soup.select('.tblOffer')[0]
        return offer_table

   
        
    #to end the session(quitting the browser)
    def quit(self):
        self.driver.close()


