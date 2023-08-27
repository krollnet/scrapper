from download import Downloader
import json
from data import Book, BookList, read_json
from parse import Parser

def process(url, web_page_path=None, data_path=None):
    downloader = Downloader(URL, method="GET")
    downloader.save(web_page_path)

    
    parser = Parser(web_page_path)
    parser.parse()
    parser.save(data_path)

    data = read_json(data_path)
    books = BookList()
    for index, d in data.items():
        book = Book(d.get('name'), int(d.get('price')), d.get('authors'))
        books.append_book(book)

    print("Все книги:")
    print(books)
    print()
    
    print("Поиск книги по имени автора: Людмила Чельцова:")
    print(books.find_book_by_author('Людмила Чельцова'))
    print()

    print("Книги стоимостью от 200 до 900 рублей:")
    print(books.price_between(200, 900))
    print()

    return books.get_stats()

URL = "https://store.artlebedev.ru/books/typography/"
WEB_PAGE_PATH = "site.html"
DATA_PATH = "final.json"

result = process(URL, WEB_PAGE_PATH, DATA_PATH)
print(result)