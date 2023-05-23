import datetime

class Book:
    title = None
    author = None
    year = None

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f'Название книги: {self.title}, ' \
               f'автор книги: {self.author}, ' \
               f'год издания: {self.year}'

    def get_year(self):
        current_year = datetime.date.today().year
        return f'Возраст книги: {current_year - self.year} лет'

book = Book('Отцы и дети', 'Тургенев', 1862)
info = book.get_info()
age = book.get_year()
print(info)
print(age)