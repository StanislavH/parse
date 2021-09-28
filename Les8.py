from selenium import webdriver
import time
from pymongo import MongoClient


def write_result(data):
    db = MongoClient('localhost', 27017)['gb_mongo']
    asd = list(db.collection.find())
    [a + ' ' + b for a in data for b in asd if a != b]


def parse_opendata2():
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "C:\Tutorial\down"}
    options.add_experimental_option("prefs", prefs);
    driver = webdriver.Chrome(r'C:\chromedriver.exe', chrome_options=options)
    driver.get('https://data.gov.ru/')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/a[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="tabs-0-center-1"]/div/div/div/div[3]/div/div[4]/div/div/a').click()
    time.sleep(3)
    docs = driver.find_elements_by_xpath(
        '/html/body/div[1]/div/div[3]/div/div[4]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/div/div/h2/a')
    for i in range(len(docs)):
        docs[i] = docs[i].get_attribute("href")
    for i in docs:
        print(i)
        driver.get(i)
        time.sleep(5)
        if len(driver.find_elements_by_xpath(
                '/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[3]/div/div[2]/div/div[4]/div/div/div/div[3]/table[2]/tbody/tr/td[5]/a')) > 0:
            driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[3]/div/div[2]/div/div[4]/div/div/div/div[3]/table[2]/tbody/tr/td[5]/a').click()
    driver.close()


parse_opendata2()
