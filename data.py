from parser import *
import json


def read_json(file_path):
    with open (file_path, 'r', encoding = 'utf-8') as file:
        obj = json.load(file)
    return obj


class Book:
    def __init__(self, name, price, authors=[]):
        self.name = name
        self.price = price 
        self.authors = authors
    def __str__(self):
        return f'"Название: {self.name}; авторы: {", ".join(self.authors)}; стоимость: {self.price}"'
    def __repr__(self):
        return f'"Название: {self.name}; авторы: {", ".join(self.authors)}; стоимость: {self.price}"'

class BookList():
    def __init__(self, book_list=[]):
        self.book_list = book_list
    
    def __str__(self):
        return f'{self.book_list}'
    
    def append_book(self, book):
        self.book_list.append(book)

    def min_price(self):
        prices=[]
        for book in self.book_list:
            prices.append(book.price)
        return min(prices)
    
    def max_price(self):
        prices=[]
        for book in self.book_list:
            prices.append(book.price)
        return max(prices)
    
    def avg_price(self):
        prices=[]
        for book in self.book_list:
            prices.append(book.price)
        return round(sum(prices)/len(prices),2)
    
    def find_book_by_author(self, author):
        books=[]
        for book in self.book_list:
            for auth in book.authors:
                if auth == author:
                    books.append(book)
        return books
    
    def price_between(self, start, end):
        books = []
        for book in self.book_list:
            if start <= book.price <= end:
                books.append(book)
        return books 
    
    def get_stats(self):
        return {'min': self.min_price(), 'max': self.max_price(), 'avg': self.avg_price()}
                    