from Domain.film import *


class FilmValidator:
    def __init__(self, film: Film):
        self.film = film

    def validare(self):
        if self.film.get_pret_bilet() < 0.0:
            raise ValueError('Pretul trebuie sa fie strict pozitiv.')

        if self.film.get_in_program() not in ['da', 'nu']:
            raise ValueError('La rubrica In program trebuie scris da sau nu !')

        if int(self.film.get_an_aparitie()) < 1900:
            raise ValueError('Anul aparitiei este prea mic.')
