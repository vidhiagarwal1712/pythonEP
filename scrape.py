from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
from selenium.webdriver.common.by import By
url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome(
    'C:/Users/yena0/Downloads/chromedriver_win32/chromedriver')
browser.get(url)
time.sleep(10)

headers = ['name', 'LIGHT_YEARS_FROM_EARTH', 'PLANET_MASS', 'STELLAR_MAGNITUDE', 'DISCOVERY_DATE',
           'hyperlink', 'PLANET TYPE', 'PLANET RADIUS', 'ORBITAL RADIUS', 'ORBITAL PERIOD', 'ECCENTRICITY']
planetdata = []


def scrapdata():

    for f in range(0, 5):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        allultags = soup.find_all('ul', attrs={'class', 'exoplanet'})
        for eachul in allultags:
            alllitags = eachul.find_all('li')
            templist = []
            for index, eachli in enumerate(alllitags):
                if(index == 0):
                    templist.append(eachli.find_all('a')[0].contents[0])
                else:
                    templist.append(eachli.contents[0])
            hyperlinkvalue = alllitags[0]
            templist.append('https://exoplanets.nasa.gov' +
                            hyperlinkvalue.find_all('a', href=True)[0]['href'])
            planetdata.append(templist)
        browser.find_element(
            By.XPATH, '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    


scrapdata()
newplanetdata = []


def scrapmoredata(l):
    try:
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        templist = []
        alltrtags = soup.find_all('tr', attrs={'class', 'fact_row'})
        for indextr,eachtr in enumerate(alltrtags):
            alltd = eachtr.find_all('td')
            for indextd,eachtd in enumerate(alltd):
                if((indextr == 0 and indextd == 1) or (indextr == 1 and indextd == 0) or (indextr == 3 and indextd == 1)):
                    continue
                else:
                    templist.append(eachtd.find_all(
                    'div', attrs={'class', 'value'})[0].contents[0])
    except:
        time.sleep(1)
        scrapmoredata(l)
    newplanetdata.append(templist)


for index, data in enumerate(planetdata):
    scrapmoredata(data[5])
finalplanetdata = []
for index,data in enumerate(planetdata):
    newplanetdatavalue = newplanetdata[index]
    finalplanetdata.append(data+newplanetdatavalue)
with open('scraper.csv', 'w', newline='') as X:
    csvwriter = csv.writer(X)
    csvwriter.writerow(headers)
    csvwriter.writerows(finalplanetdata)