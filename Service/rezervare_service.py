from Repository.rezervare_repo import *
from Repository.rezervare_repo_validator import *


class ServiceRezervare:
    def __init__(self):
        self.repo = RepoRezervare('/Users/c.mihai/Desktop/exersare/laborator 8-9/rezervari.txt')

    def create(self, id_, id_film, id_card, data, ora):
        clas = Rezervare(id_, id_film, id_card, data, ora)

        r = RezervareValidator(clas)
        r.validator()

        self.repo.create(clas)

    def read(self, id_):
        return self.repo.read(id_)

    def update(self, id_, id_film, id_card, data, ora):
        clas = Rezervare(id_, id_film, id_card, data, ora)

        r = RezervareValidator(clas)
        r.validator()

        self.repo.update(clas)

    def delete(self, id_):
        self.repo.delete(id_)

    def show_all(self):
        return self.repo.all()

    def show_interval(self, h_start, m_start, h_end, m_end):
        rezervari = self.show_all()
        rez = []
        for r in rezervari:
            ora = r.get_ora()
            o = ora.split(':')
            h = int(o[0])
            m = int(o[1])
            if h_start != h_end:
                if h_start < h < h_end:
                    rez.append(self.read(r.get_id()))
                elif h == h_start:
                    if m_start <= m:
                        rez.append(self.read(r.get_id()))
                elif h == h_end:
                    if m <= m_end:
                        rez.append(self.read(r.get_id()))
            else:
                if m_start <= m <= m_end:
                    rez.append(self.read(r.get_id()))
        return rez

    def show_idFilme_descrescator(self):
        rezervari = self.show_all()
        rez = []

        for r in rezervari:
            ok = True
            for i in range(len(rez)):
                if r.get_id_film() == rez[i][0]:
                    rez[i][1] = rez[i][1] + 1
                    ok = False
            if ok:
                rez.append([r.get_id_film(), 1])

        for i in range(len(rez) - 1):
            for j in range(i + 1, len(rez)):
                if rez[i][1] < rez[j][1]:
                    aux = rez[i]
                    rez[i] = rez[j]
                    rez[j] = aux

        return rez
