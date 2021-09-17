# Написать приложение, которое собирает основные новости с сайтов mail.ru, lenta.ru, yandex-новости. Для парсинга использовать XPath. Структура данных должна содержать:
# название источника;
# наименование новости;
# ссылку на новость;
# дата публикации.

from pprint import pprint
from lxml import html
import requests
from pymongo import MongoClient


def parse_mail_news(url="https://news.mail.ru/politics/"):
    try:
        response = requests.get(url)
        root = html.fromstring(response.text)
        source = root.xpath(
            "//*/div[@class='newsitem newsitem_height_fixed js-ago-wrapper js-pgng_item']/div[1]/span[2]/text()")
        names = root.xpath(
            "//*/div[@class='newsitem newsitem_height_fixed js-ago-wrapper js-pgng_item']/span[2]/a[1]/span/text()")
        hrefs = root.xpath(
            "//*/div[@class='newsitem newsitem_height_fixed js-ago-wrapper js-pgng_item']/span[2]/a[1]/@href")
        dates = root.xpath(
            "//*/div[@class='newsitem newsitem_height_fixed js-ago-wrapper js-pgng_item']/div[1]/span[1]/text()")
        #print(source)
        #print(names)
        #print(hrefs)
        #print(dates)
        for num, item in enumerate(source):
            news.append(
                {'source': source[num], 'name': names[num], 'url': hrefs[num], 'date': dates[num]})
    except:
        print('Ошибка запроса')


def parse_lenta_news(url="https://lenta.ru/parts/news/"):
    try:
        response = requests.get(url)
        root = html.fromstring(response.text)
        source = root.xpath("//*/div[1]/div[1]/a/@href")
        # source = root.xpath("//*/div/div/a[@target='_blank']/text()")
        names = root.xpath("//*/div/div[2]/h3/a/text()")
        hrefs = root.xpath('//*/div/div[2]/h3/a/@href')
        dates = root.xpath("//*/div/div[@class='info g-date item__info']/text()")
        # print(source)
        # print(names)
        # print(hrefs)
        # print(dates)
        for num, item in enumerate(source):
            news.append(
                {'source': source[num], 'name': names[num], 'url': hrefs[num], 'date': dates[num]})
    except:
        print('Ошибка запроса')


def parse_yandex_news(url="https://yandex.ru/news/"):
    try:
        response = requests.get(url)
        root = html.fromstring(response.text)
        source = root.xpath("//*/article/div[3]/div[1]/div/span[1]/a[1]/text()")
        names = root.xpath("//*/article/div[1]/div/a/h2/text()")
        hrefs = root.xpath('//*/article/div[1]/div/a/@href')
        dates = root.xpath("//*/article/div[3]/div[1]/div/span[2]/text()")
        ##print(source)
        #print(names)
        #print(hrefs)
        #print(dates)
        for num, item in enumerate(source):
            news.append(
                {'source': source[num], 'name': names[num], 'url': hrefs[num], 'date': dates[num]})
    except:
        print('Ошибка запроса')


def write_db(x):
    db = MongoClient('localhost', 27017)['gb_3_mongo']
    news_collection = db.news_collection
    db.news_collection.insert_many(x)

news = []
parse_mail_news()
parse_lenta_news()
parse_yandex_news()
write_db(news)
