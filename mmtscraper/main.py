from mmtscraper import MmtScraper
from Table2xlsx import Table2xlsx
from time import sleep

url = 'https://www.makemytrip.com/daily-deals'
                                
workbook = "data.xlsx"
sheetname = "Sheet1"


print("starting mmtscraper...")
print("\ncurrent target - ",url)
scraper = MmtScraper(url)
print("loading url, getting offer links!..")
scraper.load_mmt_url()
offer_links = scraper.extract_offer_links()
print("extracting offer details for all offers on ", url)

for link in offer_links:
        
    response = scraper.open_offer_link(link)
        
    offer_table = scraper.extract_table(response)
    if offer_table==-1:
        table_list = scraper.noTable(response)
    else:
        print("converting html to table")
        table_list = Table2xlsx.html_table_converter(offer_table)
    print("getting category of the offer..")
    category_detail = scraper.get_category(response)
    print("getting other details about the offer..")
    list_text = scraper.get_list_text(response)
    table_list = Table2xlsx.fill_missing(category_detail, list_text, link, table_list)             
    print("populating {} in {} file with *{}* offer coupons...".format(sheetname,workbook,len(table_list)-1))
    Table2xlsx.table_to_xlsx(workbook, sheetname, table_list)



print("\ndone with scraping , now quitting driver..")
sleep(2)
scraper.quit()
    



