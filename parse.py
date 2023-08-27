import bs4
import json
import re
import requests


class Parser(object):
    def __init__(self, path):
        self.source = path

    def parse(self):
        with open(self.source, encoding='utf-8') as fp:
            f = fp.read()
        bs = bs4.BeautifulSoup(f, features='html.parser')

        result = {}
        books_list = bs.find('ul', 'products-list').find_all('li')
        count = 1
        for book in books_list:
            b = {}
            b['name'] = book.find('span', 'product__name').text
            b['price'] = book.find('span', 'price_current_RUB').text
            b['authors'] = book.find('p').text.split(', ')
            result[str(count)] = b
            count += 1
        
        return result
    
    def save(self, file_path):
        with open(file_path, "w", encoding='utf-8') as file:
            json.dump(self.parse(), file, ensure_ascii=False)
            