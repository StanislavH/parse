# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы) с сайтов Superjob и HH.
# Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
# Наименование вакансии.
# Предлагаемую зарплату (отдельно минимальную и максимальную).
# Ссылку на саму вакансию.
# Сайт, откуда собрана вакансия.

# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
# Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas.

from bs4 import BeautifulSoup
import requests
import re
import lxml


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
                    [i['name'], str(i['salary']['from']) + '-' + str(i['salary']['to']), i['url'], 'hh.ru'])
                # print(i['name'], str(i['salary']['from']) + '-' + str(i['salary']['to']), i['url'], 'hh.ru')
            except Exception:
                print('Что-то пошло не так')


def getSJvacancy(name_vac, page):
    for p in range(0, page):
        url_sj = 'https://russia.superjob.ru/vacancy/search/?keywords=' + name_vac + '&page=' + str(p)
        response = requests.get(url_sj).text
        soup = BeautifulSoup(response, 'lxml')

        vacancy_names = [re.sub('<[^>]*>', '', str(i)) for i in soup.select('div.jNMYr div a')]
        vacancy_salaries = [re.sub('<[^>]*>', '', str(i)).replace(u'\xa0', u' ') for i in soup.select('div.jNMYr span._1OuF_')]
        vacancy_urls = ['https://russia.superjob.ru' + i['href'] for i in soup.select('div.jNMYr div a')]

        for num, item in enumerate(vacancy_names):
            vacancies.append([vacancy_names[num], vacancy_salaries[num], vacancy_urls[num], 'superjob.ru'])


name = 'Программист'
pages = 3
vacancies = []
getHHvacancy(name, pages)
getSJvacancy(name, pages)
print(vacancies)
