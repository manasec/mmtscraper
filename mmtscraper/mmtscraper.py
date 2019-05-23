from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import bs4
import requests
import re

class MmtScraper(object):
    def __init__(self, url):

        self.url = url
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--incognito')
        #self.options.add_argument('--headless')                                         #can try headless but mmt blocks this
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\acer\Desktop\python\chromedriver_win32\chromedriver.exe",
                                       options=self.options)
        self.delay = 3
        
    
    def load_mmt_url(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "deal-view-details")))
            print("Page is ready")
        except TimeoutException:
            print("Loading took too much time! seems like no offers")
    
    def extract_offer_links(self):
        all_link_elements = self.driver.find_elements_by_class_name("deal-view-details")
        for i in range(len(all_link_elements)):
            all_link_elements[i] = all_link_elements[i].get_attribute('href')

        return all_link_elements
      
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
    
    def extract_table(self,response):

        soup = bs4.BeautifulSoup(response.text,'lxml')
        offer_table = soup.select('.tblOffer')
        if offer_table:
            return offer_table[0]
        else:
            return -1
    def noTable(self,response):
        
        table_list = [["Coupon Code","Offer Details",
                    "Minimum Booking Amount (INR)","Booking Channel",
                    "Applicable Banks"],[]]
        coupon_code_pattern = re.compile(r"\b\s[A-Z]{4,}[0-9]*")
        list_text = self.get_list_text(response)
        coupon = coupon_code_pattern.search(list_text)
        if coupon:
            table_list[1].append(coupon.group(0))
                
        else:
            table_list[1].append("no coupon code")
        
        soup = bs4.BeautifulSoup(response.text,'lxml')
        steps = soup.select(".steps")
        alist = ""
        for step in steps:
            alist+= step.text
        alist = alist.split("\n")
        offer_detail_index = alist.index("Offers")+1
        min_amount_index = alist.index("Min. booking amount")+1
        applicable_bank_index = alist.index("Applicable Banks")+1
        booking_channel_index = alist.index("Booking Channel")+1
        new_list = [alist[offer_detail_index],alist[min_amount_index],
            alist[booking_channel_index],alist[applicable_bank_index]]
        for index in range(len(new_list)):
            table_list[1].append(new_list[index])

        return table_list
        

    def get_category(self,response):

        soup = bs4.BeautifulSoup(response.text,'lxml')
        category = soup.select(".bannerInnerContent")[0]
        return category.text

    def get_list_text(self, response):
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        listing = soup.select(".listing")
        text = ""
        for alist in listing:
            text = text + alist.text
        return text
    
    def quit(self):
        self.driver.quit()


