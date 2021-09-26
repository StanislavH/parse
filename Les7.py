from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from pymongo import MongoClient


def write_result(data):
    db = MongoClient('localhost', 27017)['gb_mongo']
    asd = list(db.collection.find())
    [a + ' ' + b for a in data for b in asd if a != b]


def parse_mail():
    driver = webdriver.Chrome(r'C:\chromedriver.exe')

    mails_collecion = []
    driver.get('https://mail.ru/')
    input_field = driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/div[1]/div[2]/input')
    input_field.send_keys('study.ai_172@mail.ru')
    input_field.send_keys(Keys.ENTER)
    time.sleep(2)
    input_field = driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/div[2]/input')
    input_field.send_keys('NextPassword172???')
    input_field.send_keys(Keys.ENTER)
    time.sleep(20)

    mails = driver.find_elements_by_xpath(
        '//a[@class="llc js-tooltip-direction_letter-bottom js-letter-list-item llc_normal"]')
    for i in range(len(mails)):
        mails[i] = mails[i].get_attribute("href")

    for i in range(0, 2, 1):
        print(mails[i])
        driver.get(mails[i])
        time.sleep(5)
        mail_from = driver.find_element_by_xpath(
            '//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/span').get_attribute(
            'title')
        mail_date = driver.find_element_by_xpath(
            '//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[1]').text
        mail_title = driver.find_element_by_xpath(
            '//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div/div/div[1]/div[3]/h2').text
        mail_text = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div')
        mails_collecion.append({'source': mail_from, 'date': mail_date, 'title': mail_title, 'text': mail_text})
        print(mail_from, mail_date, mail_title, mail_text)
        time.sleep(5)
    print(mails_collecion)
    # write_result(mails_collecion)
    driver.close()


def parse_mvideo():
    driver = webdriver.Chrome(r'C:\chromedriver.exe')
    product_collecion1 = []
    driver.get('https://www.mvideo.ru/')
    input_field = driver.find_element_by_name('Ntt')
    input_field.send_keys("Новинки")
    input_field.send_keys(Keys.ENTER)
    time.sleep(9)
    driver.find_element_by_class_name('modal-layout__close').click()
    time.sleep(2)
    ActionChains(driver).send_keys(Keys.END).perform()
    time.sleep(2)
    products1_name = driver.find_elements_by_class_name("product-title__text")
    products1_price = driver.find_elements_by_xpath(
        "/html/body/mvid-root/div/mvid-srp/mvid-layout/div/main/mvid-product-list-block/div[2]/mvid-product-list/mvid-plp-product-cards-layout/div/mvid-product-cards-row/div/div/mvid-plp-price-block/div/mvid-price/div/p/span[1]")
    for i in range(len(products1_name)):
        product_collecion1.append({'name': products1_name[i].text, 'price': products1_price[i].text})
    print(product_collecion1)
    # write_result(product_collecion1)
    driver.close()


def parse_onlinetrade():
    driver = webdriver.Chrome(r'C:\chromedriver.exe')
    product_collecion2 = []
    driver.get('https://www.onlinetrade.ru/')
    input_field = driver.find_element_by_name('query')
    input_field.send_keys("Новинки")
    input_field.send_keys(Keys.ENTER)
    time.sleep(5)
    products2_name = driver.find_elements_by_xpath(
        '//*[@id="main_area"]/div[4]/div/div[5]/div[2]/div[2]/div/div[2]/div/div[3]/a')
    products2_price = driver.find_elements_by_xpath(
        '//*[@id="main_area"]/div[4]/div/div[5]/div[2]/div[2]/div/div[3]/div[1]/span')
    for i in range(len(products2_name)):
        product_collecion2.append({'name': products2_name[i].text, 'price': products2_price[i].text})
    print(product_collecion2)
    # write_result(product_collecion2)
    driver.close()


# parse_mail()
parse_mvideo()
# parse_onlinetrade()
