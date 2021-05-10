from Repository.card_repo import *
from Repository.card_repo_validator import *


class ServiceCard:
    def __init__(self):
        self.repo = RepoCard('/Users/c.mihai/Desktop/exersare/laborator 8-9/card_clienti.txt')

    def create(self, id_, nume, prenume, cnp, data_nastere, data_inregistrare, puncte_acumulate):
        clas = CardClient(id_, nume, prenume, cnp, data_nastere, data_inregistrare, puncte_acumulate)

        validator = CardValidator(clas)
        validator.validator()

        self.repo.create(clas)

    def read(self, id_):
        return self.repo.read(id_)

    def update(self, id_, nume, prenume, cnp, data_nastere, data_inregistrare, puncte_acumulate):
        clas = CardClient(id_, nume, prenume, cnp, data_nastere, data_inregistrare, puncte_acumulate)
        self.repo.update(clas)

    def delete(self, id_):
        self.repo.delete(id_)

    def show_all(self):
        return self.repo.all()

    def read_nume(self, nume):
        clienti = self.show_all()
        rez = []
        for c in clienti:
            if c.get_nume() == nume:
                rez.append(self.read(c.get_id()))
        return rez

    def read_prenume(self, prenume):
        clienti = self.show_all()
        rez = []
        for c in clienti:
            if c.get_prenume() == prenume:
                rez.append(self.read(c.get_id()))
        return rez

    def read_cnp(self, cnp):
        clienti = self.show_all()
        rez = []
        for c in clienti:
            if c.get_cnp() == cnp:
                rez.append(self.read(c.get_id()))
        return rez

    def carduri_descresc_nrPuncte(self):
        rez = []
        carduri = self.show_all()

        for c in carduri:
            rez.append((c.get_id(), c.get_puncte_acumulate()))

        for i in range(len(rez) - 1):
            for j in range(i + 1, len(rez)):
                if rez[i][0] < rez[j][0]:
                    aux = rez[i]
                    rez[i] = rez[j]
                    rez[j] = aux

        return rez

    def adunare_puncte_zile_nastere(self, zi_s, luna_s, an_s, zi_e, luna_e, an_e, nr_puncte):
        carduri = self.show_all()

        for c in carduri:
            data = c.get_data_nastere()
            d = data.split('.')
            zi = int(d[0])
            luna = int(d[1])
            an = int(d[2])
            if an_s != an_e:
                if an_s < an < an_e:
                    self.update(c.get_id(), c.get_nume(), c.get_prenume(), c.get_cnp(), c.get_data_nastere(),
                                c.get_data_inregistrare(), c.get_puncte_acumulate()+nr_puncte)
                elif an == an_s:
                    if luna > luna_s:
                        self.update(c.get_id(), c.get_nume(), c.get_prenume(), c.get_cnp(), c.get_data_nastere(),
                                    c.get_data_inregistrare(), c.get_puncte_acumulate() + nr_puncte)
                    elif luna == luna_s:
                        if zi >= zi_s:
                            self.update(c.get_id(), c.get_nume(), c.get_prenume(), c.get_cnp(), c.get_data_nastere(),
                                        c.get_data_inregistrare(), c.get_puncte_acumulate() + nr_puncte)
                elif an == an_e:
                    if luna < luna_e:
                        self.update(c.get_id(), c.get_nume(), c.get_prenume(), c.get_cnp(), c.get_data_nastere(),
                                    c.get_data_inregistrare(), c.get_puncte_acumulate() + nr_puncte)
                    elif luna == luna_e:
                        if zi <= zi_e:
                            self.update(c.get_id(), c.get_nume(), c.get_prenume(), c.get_cnp(), c.get_data_nastere(),
                                        c.get_data_inregistrare(), c.get_puncte_acumulate() + nr_puncte)
            else:
                if luna_s != luna_e:
                    if luna_s < luna < luna_e:
                        self.update(c.get_id(), c.get_nume(), c.get_prenume(), c.get_cnp(), c.get_data_nastere(),
                                    c.get_data_inregistrare(), c.get_puncte_acumulate() + nr_puncte)
                    elif luna == luna_s:
                        if zi >= zi_s:
                            self.update(c.get_id(), c.get_nume(), c.get_prenume(), c.get_cnp(), c.get_data_nastere(),
                                        c.get_data_inregistrare(), c.get_puncte_acumulate() + nr_puncte)
                    elif luna == luna_e:
                        if zi <= zi_e:
                            self.update(c.get_id(), c.get_nume(), c.get_prenume(), c.get_cnp(), c.get_data_nastere(),
                                        c.get_data_inregistrare(), c.get_puncte_acumulate() + nr_puncte)
                else:
                    if zi >= zi_s:
                        self.update(c.get_id(), c.get_nume(), c.get_prenume(), c.get_cnp(), c.get_data_nastere(),
                                    c.get_data_inregistrare(), c.get_puncte_acumulate() + nr_puncte)
                    elif zi <= zi_e:
                        self.update(c.get_id(), c.get_nume(), c.get_prenume(), c.get_cnp(), c.get_data_nastere(),
                                    c.get_data_inregistrare(), c.get_puncte_acumulate() + nr_puncte)
