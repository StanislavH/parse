from bs4 import BeautifulSoup
import requests
import re
import lxml
from pymongo import MongoClient


def write_result(data):
    db = MongoClient('localhost', 27017)['gb_3_mongo']
    vacancy_collection = db.vacancy_collection
    #[a + ' ' + b for a in list1 for b in list2 if a != b]
    asd = list(db.vacancy_collection.find())
    [a + ' ' + b for a in data for b in asd if a != b]
    #for x in data:
    #    if db.vacancy_collection.find({"url": x["url"]}):
    #        db.vacancy_collection.insert_one(x)


def find_vacancy(sal=3000):
    db = MongoClient('localhost', 27017)['gb_3_mongo']
    vacancy_collection = db.vacancy_collection
    for x in db.vacancy_collection.find({"min_sal": {"$gt": str(sal)}}):
        print(x)


def getHHvacancy(name_vac, page):
    for p in range(0, page):
        params = {
            'text': 'NAME:' + name_vac,  # Текст фильтра. В имени должно быть слово "Аналитик"
            'page': p,  # Индекс страницы поиска на HH
            'per_page': 10  # Кол-во вакансий на 1 странице
        }
        data = requests.get('https://api.hh.ru/vacancies', params).json()
        for i in data['items']:
            try:
                vacancies.append(
                    {"name": i['name'], "min_sal": str(i['salary']['from']), "max_sal": str(i['salary']['to']),
                     "url": i['url'],
                     "site": 'hh.ru'})
                # print(i['name'], str(i['salary']['from']) + '-' + str(i['salary']['to']), i['url'], 'hh.ru')
            except Exception:
                print('Что-то пошло не так')

def getSJvacancy(name_vac, page):
    for p in range(0, page):
        url_sj = 'https://russia.superjob.ru/vacancy/search/?keywords=' + name_vac + '&page=' + str(p)
        response = requests.get(url_sj).text
        soup = BeautifulSoup(response, 'lxml')

        vacancy_names = [re.sub('<[^>]*>', '', str(i)) for i in soup.select('div.jNMYr div a')]
        vacancy_salaries = [re.sub('<[^>]*>', '', str(i)).replace(u'\xa0', u' ') for i in
                            soup.select('div.jNMYr span._1OuF_')]
        vacancy_urls = ['https://russia.superjob.ru' + i['href'] for i in soup.select('div.jNMYr div a')]

        for num, item in enumerate(vacancy_names):
            if "договор" in vacancy_salaries[num]:
                vacancies.append({"name": vacancy_names[num], "min_sal": "-", "max_sal": "-", "url": vacancy_urls[num],
                                  "site": 'superjob.ru'})
            elif "—" in vacancy_salaries[num]:
                vacancies.append({"name": vacancy_names[num],
                                  "min_sal": vacancy_salaries[num][:vacancy_salaries[num].find("—")].replace(' ', ''),
                                  "max_sal": vacancy_salaries[num][vacancy_salaries[num].find("—") + 1:vacancy_salaries[
                                                                                      num].find("руб") - 1].replace(' ',
                                                                                                                 ''),
                                  "url": vacancy_urls[num],
                                  "site": 'superjob.ru'})
            elif "до" in vacancy_salaries[num]:
                vacancies.append({"name": vacancy_names[num],
                                  "min_sal": "-",
                                  "max_sal": vacancy_salaries[num][
                                             vacancy_salaries[num].find("до") + 3:vacancy_salaries[
                                                                                      num].find("руб") - 1].replace(' ',
                                                                                                                    ''),
                                  "url": vacancy_urls[num],
                                  "site": 'superjob.ru'})
            elif "от" in vacancy_salaries[num]:
                vacancies.append({"name": vacancy_names[num], "min_sal": vacancy_salaries[num][
                                                                         vacancy_salaries[num].find("от") + 3:
                                                                         vacancy_salaries[num].find("руб") - 1].replace(
                    ' ', ''), "max_sal": "-", "url": vacancy_urls[num],
                                  "site": 'superjob.ru'})


name = 'Программист'
pages = 1
vacancies = []
getHHvacancy(name, pages)
getSJvacancy(name, pages)
# print(vacancies)
write_result(vacancies)
find_vacancy(150000)
