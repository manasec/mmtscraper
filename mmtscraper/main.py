from mmtscraper import MmtScraper
from Table2xlsx import Table2xlsx
from time import sleep
url = 'https://www.makemytrip.com/'
categories = ['daily-deals',
              'daily-deals/bank',
            'daily-deals/flights',
              'daily-deals/hotels-coupon-offers',
            'daily-deals/holidays-coupon-offers',
              'cabs-coupon-offers',
              'bus-coupon-offers']
#categories - all the potential offer dirs for mmt offer url's  
sheetcount = 1                                   
workbook = "data.xlsx"
sheetname = "Sheet"

print("starting mmtscraper...")

for category in categories:
    print("\ncurrent target category - ",categories[sheetcount-1])
    scraper = MmtScraper(url, category)
    print("loading url, getting offer links!..")
    scraper.load_mmt_url()
    offer_links = scraper.extract_offer_links()
    
    
    print("extracting offer details for all offers on ",categories[sheetcount-1])
    for link in offer_links:
        
        response = scraper.open_offer_link(link)
        #if response.status_code
        offer_table = scraper.extract_table(response)
        print("converting html to table")
        table_list = Table2xlsx.html_table_converter(offer_table)
        print("populating {} in {} file with *{}* offer coupons...".format(sheetname+str(sheetcount),workbook,len(table_list)-1))
        Table2xlsx.table_to_xlsx(workbook, sheetname+str(sheetcount), table_list)

    


     
        #break
    sheetcount += 1
    print("\ndone with {} , now quitting driver..".format(category))
    sleep(2)
    scraper.quit()
