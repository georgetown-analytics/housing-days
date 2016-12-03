__author__ = 'Will'

import requests
import csv
import re
import time
from bs4 import BeautifulSoup

query='20001'
realtor_search_query = 'http://www.realtor.com/realestateandhomes-search/'+str(query)

def process_search_page(page_results_list):
    page_list = []
    for result in page_results_list:
        result_url = result.findAll(name="a")[0].get("href")
        page_list.append(result_url)
        print(result_url)
    return page_list


session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, image/webp,*/*;q=.8"}

filename = 'RealtorScrape '+str(query)+'.csv'
html = session.get(realtor_search_query, headers=headers)
page_results_bsObj = BeautifulSoup(html.text, "html.parser")
initial_page_results_list = page_results_bsObj.findAll(name="div", attrs={"class":lambda x: x and 'js-record-user-activity' in x})
all_urls = []
page_count = 1
page_results_list = initial_page_results_list
error = False
while error == False:
#for i in range(1):
    print("PAGE "+str(page_count))
    all_urls += process_search_page(page_results_list)
    try:
        next_page = page_results_bsObj.find(name="a", attrs={"class":"next"}).get("href")
    except AttributeError:
        error = True

    html = session.get("http://www.realtor.com"+str(next_page), headers=headers)
    page_results_bsObj = BeautifulSoup(html.text, "html.parser")
    page_results_list = page_results_bsObj.findAll(name="div", attrs={"class":"js-record-user-activity js-navigate-to srp-item  "})
    page_count+=1

listings = [[]]
i = 0
listings.append(["street_address", "address_locality", "address_region", "postal_code", "beds", "price", "property_style", "property_type", "property_year", "latest_activity_date", "latest_activity_type"])
for url in all_urls:
    i+=1
    print(i)
    html = session.get("http://www.realtor.com"+str(url), headers=headers)
    result_detail_bsObj = BeautifulSoup(html.text, "html.parser")
    street_address = result_detail_bsObj.find(name="span", attrs={"itemprop":"streetAddress"}).get_text()
    address_locality = result_detail_bsObj.find(name="span", attrs={"itemprop":"addressLocality"}).get_text()
    address_region = result_detail_bsObj.find(name="span", attrs={"itemprop":"addressRegion"}).get_text()
    postal_code = result_detail_bsObj.find(name="span", attrs={"itemprop":"postalCode"}).get_text()
    beds = result_detail_bsObj.find(name="li", attrs={"data-label":"property-meta-beds"}).find(name="span", attrs={"class":"data-value"}).get_text()
    price = result_detail_bsObj.find(name="span", attrs={"itemprop":"price"}).get_text()
    try:
        property_style = result_detail_bsObj.find(name="li", attrs={"data-label":"property-style"}).find(name="a").get_text()
    except AttributeError:
        property_style = ""
    try:
        property_type = result_detail_bsObj.find(name="li", attrs={"data-label":"property-type"}).get_text()
    except AttributeError:
        property_type = ""
    try:
        property_year = result_detail_bsObj.find(name="li", attrs={"data-label":"property-year"}).get_text().replace('\n', ' ').replace('\r', '')
    except AttributeError:
        property_year = ""
    try:
        latest_activity_date = result_detail_bsObj.find(name="div", attrs={"id":"ldp-history-price"}).findAll(name="tr")[1].findAll(name="td")[0].get_text()
    except IndexError:
        latest_activity_date = ""
    except AttributeError:
        latest_activity_date = ""


    try:
        latest_activity_type = result_detail_bsObj.find(name="div", attrs={"id":"ldp-history-price"}).findAll(name="tr")[1].findAll(name="td")[1].get_text()
    except IndexError:
        latest_activity_type = ""
    except AttributeError:
        latest_activity_type = ""


    listings.append([street_address, address_locality, address_region, postal_code, beds, price, property_style, property_type, property_year, latest_activity_date, latest_activity_type])


with open(filename, 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile)
    for row in listings:
        thedatawriter.writerow(row)