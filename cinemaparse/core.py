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
     def get_film_nearest_session(self, film):
        page = requests.get('https://{}.subscity.ru/'.format(self.town))
        soup = BeautifulSoup(page.text, 'html.parser')
        names = soup.find_all(class_="movie-plate")
        for name in names:
            if name.get('attr-title') == film:
                url = 'https://{}.subscity.ru/'.format(self.town) + name.find('a').get('href')
                page = requests.get(url)
                soup = BeautifulSoup(page.text, 'html.parser')
                cinemas = soup.find_all(class_="row-entity")
                time_cinema = dict()
                for cinema in cinemas:
                    for t in cinema.find_all(class_='text-center cell-screenings'):
                        t = int(t.get('attr-time'))
                        name = cinema.find(class_='underdashed').text
                        if time.time() < t:
                            time_cinema[t + 3600 * 3] = name
                time_cinema = sorted(time_cinema.items(), key=lambda key: key[0])
                if len(time_cinema) == 0 or datetime.utcfromtimestamp(time_cinema[0][0]).strftime('%x') != datetime.today().strftime('%x'):
                    return None, None
                return time_cinema[0][1], datetime.utcfromtimestamp(time_cinema[0][0]).strftime('%H:%M')

KINO_IN_MOSCOW = Kinoparser('msk')
KINO_IN_MOSCOW.extract_raw_content()
KINO_IN_MOSCOW.get_films_list()
