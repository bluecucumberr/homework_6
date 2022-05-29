import argparse
import configparser
import os
import pickle

from datetime import datetime

parser = argparse.ArgumentParser(prog='Parser ini', description='Parser ini')
parser.add_argument('file_path', help='path to your ini file')
args = parser.parse_args()
print(args)

ini_path = args.file_path


class Book:
    def __init__(self, name_of_book, format, isbn, author, literary_genre):
        self.name_of_book = name_of_book
        self.format = format
        self.isbn = isbn
        self.author = author
        self.literary_genre = literary_genre

    def __str__(self):
        return f""" Book name is {self.name_of_book}, type of cover is {self.format}, ISBN is {self.isbn}, author is {self.author}, literary genre is {self.literary_genre}."""

    # Позволяет задать объект (обычно словарь), который будет использован при консервировании экземпляра класса.
    def __getstate__(self):
        state = {}
        state['name'] = self.name_of_book
        state['format'] = self.format
        state['isbn'] = self.isbn
        state['author'] = self.author
        state['literary_genre'] = self.literary_genre
        return state

    # Позволяет описать действия, необходимые для расконсервирования экземпляра класса.
    def __setstate__(self, state):
        self.name_of_book = state['name']
        self.format = state['format']
        self.isbn = state['isbn']
        self.author = state['author']
        self.literary_genre = state['literary_genre']


if os.path.exists(ini_path):
    config = configparser.ConfigParser()
    config.read(ini_path, encoding='utf8')
    # print (config['FIRST_BOOK']['name_of_book'])
    first_book = Book(
        config['FIRST_BOOK']['name_of_book'],
        config['FIRST_BOOK']['format'],
        config['FIRST_BOOK']['isbn'],
        config['FIRST_BOOK']['author'],
        config['FIRST_BOOK']['literary_genre']
    )
    second_book = Book(
        config['SECOND_BOOK']['name_of_book'],
        config['SECOND_BOOK']['format'],
        config['SECOND_BOOK']['isbn'],
        config['SECOND_BOOK']['author'],
        config['SECOND_BOOK']['literary_genre']
    )
    print(f'\nLoaded data from ini file to Class, first item is: \n{first_book}')
    print(f'\nLoaded data from ini file to Class, second item is: \n{second_book}')

    dir_to_save = 'Settings/'
    os.makedirs(dir_to_save, exist_ok=True)

    datatime_now = datetime.now().strftime("%d%m%Y_%H%M%S")

    with open(f'{dir_to_save}/books_{datatime_now}.txt', 'ab') as f:
        pickle.dump(first_book, f)  # записывает сериализованный объект в файл.
        pickle.dump(second_book, f)
    with open(f'{dir_to_save}/books_{datatime_now}.txt', 'rb') as f:
        first_book_new = pickle.load(f)  # загружает объект из файла.
        second_book_new = pickle.load(f)

    print(f'\nLoaded data from pickle file, first item is: \n{first_book_new}')
    print(f'\nLoaded data from pickle file, second item is: \n{second_book_new}')

else:
    print("Ini file not exist")
    print('Program will be stop')
    exit(0)
