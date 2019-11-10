#KINO.py
"""This is me new class"""
from bs4 import BeautifulSoup as bs
import requests as re

class Kinoparser:
    """Cinema data"""
    def __init__(self, city):
        """This function keep information about city"""

        self.data = None
        self.city = city

    def extract_raw_content(self):
        """This function extracts raw data"""

        main_page_url = "https://msk.subscity.ru"
        get_main_page_response = re.get(main_page_url)
        self.data = bs(get_main_page_response.text, 'html.parser')

    def print_raw_content(self):
        """This function print raw content"""

        return self.data.prettify()

    def get_films_list(self):
        """This function display list of films"""

        list_of_all_films = list()
        all_films = self.data.find_all("div", class_="movie-plate")
        for film in all_films:
            list_of_all_films.append(film["attr-title"])

        return list_of_all_films[1:-1]

KINO_IN_MOSCOW = Kinoparser('msk')
KINO_IN_MOSCOW.extract_raw_content()
KINO_IN_MOSCOW.get_films_list()
