from Domain.card_client import *
from Repository.card_repo import *


class CardValidator:
    def __init__(self, card: CardClient):
        self.card = card
        self.repo = RepoCard('/Users/c.mihai/Desktop/exersare/laborator 8-9/card_clienti.txt')

    def validator(self):
        store = self.repo.all()

        for s in store:
            if self.card.get_cnp() == s.get_cnp():
                raise ValueError('Exista un card cu acest cnp.')

        data = self.card.get_data_nastere()
        nastere = data.split('.')

        if len(nastere) != 3:
            raise ValueError('Data nastere trebuie sa fie de forma : zi.luna.an')
        elif int(nastere[0]) < 1 or int(nastere[0]) > 31:
            raise ValueError('Ziua de nastere trebuie sa fie intre 1 si 31.')
        elif int(nastere[1]) < 1 or int(nastere[1]) > 12:
            raise ValueError('Luna de nastere trebuie sa fie intre 1 si 12.')
        elif int(nastere[2]) < 1900 or int(nastere[2]) > 2021:
            raise ValueError('Mai verificati o data anul nasterii.')

        data = self.card.get_data_inregistrare()
        inre = data.split('.')

        if len(inre) != 3:
            raise ValueError('Data inregistrarii trebuie sa fie de forma : zi.luna.an')
        elif int(inre[0]) < 1 or int(inre[0]) > 31:
            raise ValueError('Ziua de inregistrare trebuie sa fie intre 1 si 31.')
        elif int(inre[1]) < 1 or int(inre[1]) > 12:
            raise ValueError('Luna de inregistrare trebuie sa fie intre 1 si 12.')
        elif int(inre[2]) < 1900 or int(inre[2]) > 2022:
            raise ValueError('Mai verificati o data anul inregistrarii.')

        if self.card.get_puncte_acumulate() < 0:
            raise ValueError('Punctele acumulate nu pot fi mai mici ca 0.')
