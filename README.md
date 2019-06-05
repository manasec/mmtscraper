# Mmtscraper
  This Project is a offers scraper for makemytrip.com. This will scrape all the offers currently available at MakeMyTrip and store them into a workbook.
### Packages used
* **Selenium**
> _Selenium automates browsers. That's it! What you do with that power is entirely up to you. 
> Primarily, it is for automating web applications for testing purposes, 
> but is certainly not limited to just that._
  
  documentation and further reading - [Selenium](https://pypi.org/project/selenium/).
* **BeautifulSoup**
> _Beautiful Soup is a Python library for pulling data out of HTML and XML files. 
> It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 
> and the best thing about bs4 is that it handles structurally or syntactically incorrect HTML code written for a web page_

  documentation - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* **requests**
  > _Requests allows you to send organic, grass-fed HTTP/1.1 requests, without the need for manual labor._
  
  documentation - [Requests](https://2.python-requests.org/en/master/)
* **html-table-extractor**
  > _HTML Table Extractor is a python library that uses [Beautiful Soup] to extract data from complicated and messy html tables._
  
  documentation - [html-table-extractor(https://pypi.org/project/html-table-extractor/)
* **openpyxl**
  > _openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files._
  
  documentation - [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
  
### Usage
  first of all clone this repo with:
```
git clone https://github.com/manasec/Scrapers.git
```
  then install required dependencies and libraries using:
```
pip install -r requirements.txt
```
  And finally run the driver program from circles-scrapers/mmtscraper/ directory:
```
python main.py
```
### Important notes:
* flush/clear all the data of data.xlsx file everytime before running the package to avoid redundancy, this can be automated with a small code snippet but i will update it later
* Firefox driver or IE can be used in place of chromedriver as per your preference
* The offer directories and the html structure of the website may change in future, this repo will get updated accordingly.
* The regex's used are not strict but does the work for now.
* use rotating proxies and different user-agents to avoid getting blocked
* **I'm not responsible for any action/ban by makemytrip on anyone for scraping their website, use this tool at your own risk.**
  
    
