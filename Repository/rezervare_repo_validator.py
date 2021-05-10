from Repository.rezervare_repo import *
from Repository.film_repo import *
from Repository.card_repo import *


class RezervareValidator:
    def __init__(self, rezervare: Rezervare):
        self.rezervare = rezervare
        self.repoR = RepoRezervare('/Users/c.mihai/Desktop/exersare/laborator 8-9/rezervari.txt')
        self.repoF = RepoFilm('/Users/c.mihai/Desktop/exersare/laborator 8-9/filme.txt')
        self.repoC = RepoCard('/Users/c.mihai/Desktop/exersare/laborator 8-9/card_clienti.txt')

    def validator(self):
        rezervari = self.repoR.all()
        filme = self.repoF.all()
        carduri = self.repoC.all()
        ok = True
        for f in filme:
            if self.rezervare.get_id_film() == f.get_id():
                ok = False
                if f.get_in_program() == 'nu':
                    raise ValueError('Filmul nu mai este in program.')

        if ok:
            raise ValueError('Nu exista film cu acest id.')

        okcard = True
        if self.rezervare.get_id_card() is not None:
            for c in carduri:
                if c.get_id() == self.rezervare.get_id_card():
                    okcard = False
                    break
        if okcard:
            raise ValueError('ID card este gresit.')

        d = self.rezervare.get_data()
        data = d.split('.')

        if len(data) != 3:
            raise ValueError('Data ttebuie sa fie de forma : zi.luna.an')
        elif int(data[0]) < 1 or int(data[0]) > 31:
            raise ValueError('Ziua trebuie sa fie intre 1 si 31.')
        elif int(data[1]) < 1 or int(data[1]) > 12:
            raise ValueError('Luna trebuie sa fie intre 1 si 12.')
        elif int(data[2]) < 1900 or int(data[2]) > 2021:
            raise ValueError('Mai verificati o data anul.')

        o = self.rezervare.get_ora()
        ora = o.split(':')

        if len(ora) != 2:
            raise ValueError('Ora trebuie sa fie de forma : hh:mm')
        elif int(ora[0]) < 0 or int(ora[0]) > 23:
            raise ValueError('Ora trebuie sa fie intre 0 si 23.')
        elif int(ora[1]) < 0 or int(ora[1]) > 59:
            raise ValueError('Minutele trebuie sa fie intre 0 si 59.')
