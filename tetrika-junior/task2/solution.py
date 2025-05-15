import requests
from bs4 import BeautifulSoup
import re
import csv


START_URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
BASE_URL = 'https://ru.wikipedia.org'


result: dict = {}


def write_in_csv():
    with open('beasts.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Буква', 'Количество'])  # заголовки

        for key, value in result.items():
            writer.writerow([key, value])


# Эту функцию я добавил чтобы считывать только русскоязычные названия животных.
def is_russian_letter(char: str) -> bool:
    return bool(re.fullmatch(r'[А-Яа-яёЁ]', char))


def parse_page(url: str) -> str | None:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        all_groups_element = soup.find('div', 'mw-category mw-category-columns')
        all_groups = all_groups_element.find_all('div', class_ = 'mw-category-group')

        for group in all_groups:
            h3 = group.find('h3')
            letter = h3.get_text(strip=True)
            # Проверка на то, является ли буква русской, чтобы считывать только русскоязычные названия
            # Можно закоментировать если эта проверка не требуется
            if not is_russian_letter(letter):
                return None

            ul = group.find('ul')
            if ul:
                links = ul.find_all('li')
                count = len(links)
                if letter in result:
                    result[letter] += count
                else:
                    result[letter] = count

        mw_pages = soup.find('div', id ='mw-pages')
        next_link = mw_pages.find('a', string = 'Следующая страница')
        next_href = next_link['href'] if next_link else None
        print(f'Страница считана, всего букв: {len(result.keys())}\n'
              f'Результат: {result}\n'
              f'URL: {url}\n'
              f'Следующая страница: {next_href}\n')

        if next_href:
            return BASE_URL + next_href
        else:
            return None
    else:
        print(f'Не удалось загрузить страницу: {url}')


def parser(url: str):
    url_ = url
    while url_:
        next_url = parse_page(url= url_)
        url_ = next_url
    write_in_csv()


parser(START_URL)
print('#'*50)
print(f'Конечный результат: {result}')