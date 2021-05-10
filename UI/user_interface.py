from Service.film_service import *
from Service.card_service import *
from Service.rezervare_service import *


def show_menu():
    print('1. CRUD film')
    print('2. CRUD card client')
    print('3. CRUD rezervari')
    print('4. Cautare filme sau clienti.')
    print('5. Afisare rezervari din interval de ore.')
    print('6. Afisare filme descrescator dupa numarul de rezervari.')
    print('7. Afisare carduri descrescator dupa numarul de puncte.')
    print('8. Stergere rezervari din interval orar.')
    print('9. Incrementare puncte pentru zile de nastere din intervalul dat.')
    print('10. Exit')


def show_menu_CRUD_film():
    print('1. Create film')
    print('2. Read film')
    print('3. Update film')
    print('4. Delete film')


def show_menu_CRUD_card():
    print('1. Create card client')
    print('2. Read card client')
    print('3. Update card client')
    print('4. Delete card client')


def show_menu_CRUD_rezervare():
    print('1. Create rezervare')
    print('2. Read rezervare')
    print('3. Update rezervare')
    print('4. Delete rezervare')


def show_menu_cautare_filme_clienti():
    print('1. Cautare film dupa titlu.')
    print('2. Cautare client dupa nume.')
    print('3. Cautare client dupa prenume.')
    print('4. Cautare client dupa cnp.')


class Console:
    def __init__(self):
        self.filme = ServiceFilm()
        self.carduri = ServiceCard()
        self.rezervari = ServiceRezervare()

    def handle_add_film(self):
        try:
            id_ = int(input('ID : '))
            titlu = input('Titlu : ')
            an_aparitie = input('An aparitie : ')
            pret = float(input('Pret bilet : '))
            program = input('In program : ')

            self.filme.create(id_, titlu, an_aparitie, pret, program)
        except Exception as ex:
            print(ex)

    def handle_read_film(self):
        try:
            id_ = int(input("ID : "))

            f = self.filme.read(id_)
            print(f, '\n')
        except Exception as ex:
            print(ex)

    def handle_update_film(self):
        try:
            id_ = int(input('ID : '))
            titlu = input('Titlu nou : ')
            an_aparitie = input('An aparitie nou : ')
            pret = float(input('Pret bilet nou : '))
            program = input('In program nou : ')

            self.filme.update(id_, titlu, an_aparitie, pret, program)
        except Exception as ex:
            print(ex)

    def handle_delete_film(self):
        try:
            id_ = int(input('ID de stergere : '))

            self.filme.delete(id_)
        except Exception as ex:
            print(ex)

    def handle_add_card(self):
        try:
            id_ = int(input('ID : '))
            nume = input('Nume : ')
            prenume = input('Prenume : ')
            cnp = input('CNP : ')
            data_nastere = input('Data nastere : ')
            data_inregistrare = input('Data inregistrare : ')
            puncte = int(input('Puncte acumulate : '))

            self.carduri.create(id_, nume, prenume, cnp, data_nastere, data_inregistrare, puncte)
        except Exception as ex:
            print(ex)

    def handle_read_card(self):
        try:
            id_ = int(input('ID : '))

            c = self.carduri.read(id_)
            print(c, '\n')
        except Exception as ex:
            print(ex)

    def handle_update_card(self):
        try:
            id_ = int(input('ID : '))
            nume = input('Nume nou : ')
            prenume = input('Prenume nou : ')
            cnp = input('CNP nou : ')
            data_nastere = input('Data nastere noua : ')
            data_inregistrare = input('Data inregistrare noua : ')
            puncte = int(input('Puncte acumulate nou : '))

            self.carduri.update(id_, nume, prenume, cnp, data_nastere, data_inregistrare, puncte)
        except Exception as ex:
            print(ex)

    def handle_delete_card(self):
        try:
            id_ = int(input('ID pentru stergere : '))

            self.carduri.delete(id_)
        except Exception as ex:
            print(ex)

    def handle_add_rezervare(self):
        try:
            id_ = int(input('ID : '))
            id_film = int(input('ID film : '))
            id_card = int(input('ID card : '))
            data = input('Data : ')
            ora = input('Ora : ')

            self.rezervari.create(id_, id_film, id_card, data, ora)
        except Exception as ex:
            print(ex)

    def handle_read_rezervare(self):
        try:
            id_ = int(input('ID : '))

            r = self.rezervari.read(id_)
            print(r, '\n')
        except Exception as ex:
            print(ex)

    def handle_update_rezervare(self):
        try:
            id_ = int(input('ID nou : '))
            id_film = int(input('ID film nou : '))
            id_card = int(input('ID card nou : '))
            data = input('Data noua : ')
            ora = input('Ora noua : ')

            self.rezervari.update(id_, id_film, id_card, data, ora)
        except Exception as ex:
            print(ex)

    def handle_delete_rezervare(self):
        try:
            id_ = int(input('ID pentru stergere : '))

            self.rezervari.delete(id_)
        except Exception as ex:
            print(ex)

    def handle_filme_clienti(self):
        try:
            show_menu_cautare_filme_clienti()
            optiune = input('Alegeti optiunea : ')

            if optiune == '1':
                titlu = input('Titlu : ')
                rez = self.filme.read_titlu(titlu)
                for r in rez:
                    print(r, '\n')
            elif optiune == '2':
                nume = input('Nume : ')
                rez = self.carduri.read_nume(nume)
                for r in rez:
                    print(r, '\n')
            elif optiune == '3':
                prenume = input('Prenume : ')
                rez = self.carduri.read_prenume(prenume)
                for r in rez:
                    print(r, '\n')
            elif optiune == '4':
                cnp = input('CNP : ')
                rez = self.carduri.read_cnp(cnp)
                for r in rez:
                    print(r, '\n')
            else:
                print('Nu exista optiunea \n')
        except Exception as ex:
            print(ex)

    def handle_interval_de_ore(self):
        try:
            start = input('Ora de inceput de forma hh:mm : ')
            end = input('Ora de final de forma hh:mm : ')

            s = start.split(':')
            e = end.split(':')
            h_s = int(s[0])
            m_s = int(s[1])
            h_e = int(e[0])
            m_e = int(e[1])

            if len(s) != 2 or len(e) != 2:
                raise ValueError('Orele trebuie sa fie de forma corecta.')
            elif h_s < 0 or h_s > 23:
                raise ValueError('Ora trebuie sa fie intre 0 si 23.')
            elif m_s < 0 or m_s > 59:
                raise ValueError('Minutele trebuie sa fie intre 0 si 59.')
            elif h_e < 0 or h_e > 23:
                raise ValueError('Ora trebuie sa fie intre 0 si 23.')
            elif m_e < 0 or m_e > 59:
                raise ValueError('Minutele trebuie sa fie intre 0 si 59.')
            elif h_s > h_e:
                raise ValueError('Ora de inceput trebuie sa fie mai mica sau egala.')
            elif h_s == h_e and m_s > m_e:
                raise ValueError('Daca orele sunt egale, minutul de inceput trebuie sa fie mai mic ca minutul de final')

            rez = self.rezervari.show_interval(h_s, m_s, h_e, m_e)
            for r in rez:
                print(r, '\n')
        except Exception as ex:
            print(ex)

    def handle_descresc_nr_rezervari(self):
        rez = self.rezervari.show_idFilme_descrescator()

        for r in rez:
            print(self.filme.read(r[0]), ' ---> Nr rezervari : ', r[1], '\n')

    def handle_descrescator_nrPuncte(self):
        rez = self.carduri.carduri_descresc_nrPuncte()

        for r in rez:
            print(self.carduri.read(r[0]), '\n')

    def handle_delete_inerval_orar(self):
        try:
            start = input('Ora de start de forma hh:mm : ')
            end = input('Ora de sfarsit de forma hh:mm : ')

            s = start.split(':')
            e = end.split(':')
            h_s = int(s[0])
            m_s = int(s[1])
            h_e = int(e[0])
            m_e = int(e[1])

            if len(s) != 2 or len(e) != 2:
                raise ValueError('Orele trebuie sa fie de forma corecta.')
            elif h_s < 0 or h_s > 23:
                raise ValueError('Ora trebuie sa fie intre 0 si 23.')
            elif m_s < 0 or m_s > 59:
                raise ValueError('Minutele trebuie sa fie intre 0 si 59.')
            elif h_e < 0 or h_e > 23:
                raise ValueError('Ora trebuie sa fie intre 0 si 23.')
            elif m_e < 0 or m_e > 59:
                raise ValueError('Minutele trebuie sa fie intre 0 si 59.')
            elif h_s > h_e:
                raise ValueError('Ora de inceput trebuie sa fie mai mica sau egala.')
            elif h_s == h_e and m_s > m_e:
                raise ValueError('Daca orele sunt egale, minutul de inceput trebuie sa fie mai mic ca minutul de final')

            rez = self.rezervari.show_interval(h_s, m_s, h_e, m_e)
            for r in rez:
                self.rezervari.delete(r.get_id())
        except Exception as ex:
            print(ex)

    def handle_incrementare_puncte(self):
        try:
            nr_puncte = int(input('Cu cate puncte se incrementeaza : '))
            start = input('Data de inceput de forma zi.luna.an : ')
            end = input('Data de final de forma zi.luna.an : ')

            s = start.split('.')
            e = end.split('.')

            if nr_puncte < 1:
                raise ValueError('Trebuie sa incrementati cu minim un punct.')

            if len(s) != 3 or len(e) != 3:
                raise ValueError('Data de inceput si final trebuie sa rezpecte forma ceruta.')

            zi_s = int(s[0])
            luna_s = int(s[1])
            an_s = int(s[2])
            zi_e = int(e[0])
            luna_e = int(e[1])
            an_e = int(e[2])

            if not(1 <= zi_s <= 31) or not(1 <= zi_e <= 31):
                raise ValueError('Ziua trebuie sa fie intre 1 si 31')
            elif not(1 <= luna_s <= 12) or not(1 <= luna_e <= 12):
                raise ValueError('Luna trebuie sa fie intre 1 si 12')
            elif not(1900 <= an_s <= 2021) or not(1900 <= an_e <= 2021):
                raise ValueError('Mai verificati odata anii.')

            if an_s != an_e and an_s > an_e:
                raise ValueError('Anul de inceput trebuie mai mic ca anul de final.')
            elif an_s == an_e:
                if luna_s != luna_e and luna_s > luna_e:
                    raise ValueError('Luna de inceput trebuie mai mica ca luna de final.')
                elif luna_s == luna_e:
                    if zi_s != zi_e and zi_s > zi_e:
                        raise ValueError('Ziua de inceput trebuie mai mica ca ziua de final.')

            self.carduri.adunare_puncte_zile_nastere(zi_s, luna_s, an_s, zi_e, luna_e, an_e, nr_puncte)
        except Exception as ex:
            print(ex)

    def run_console(self):
        while True:
            show_menu()
            op = input('Alegeti o optiune : ')

            if op == '1':
                show_menu_CRUD_film()
                op = input('Alegeti o optiune : ')
                if op == '1':
                    self.handle_add_film()
                elif op == '2':
                    self.handle_read_film()
                elif op == '3':
                    self.handle_update_film()
                elif op == '4':
                    self.handle_delete_film()
            elif op == '2':
                show_menu_CRUD_card()
                op = input('Alegeti o optiune : ')
                if op == '1':
                    self.handle_add_card()
                elif op == '2':
                    self.handle_read_card()
                elif op == '3':
                    self.handle_update_card()
                elif op == '4':
                    self.handle_delete_card()
            elif op == '3':
                show_menu_CRUD_rezervare()
                op = input('Alegeti o optiune : ')
                if op == '1':
                    self.handle_add_rezervare()
                elif op == '2':
                    self.handle_read_rezervare()
                elif op == '3':
                    self.handle_update_rezervare()
                elif op == '4':
                    self.handle_delete_rezervare()
            elif op == '4':
                self.handle_filme_clienti()
            elif op == '5':
                self.handle_interval_de_ore()
            elif op == '6':
                self.handle_descresc_nr_rezervari()
            elif op == '7':
                self.handle_descrescator_nrPuncte()
            elif op == '8':
                self.handle_delete_inerval_orar()
            elif op == '9':
                self.handle_incrementare_puncte()
            elif op == '10':
                print('Exit program !')
                break
            else:
                print('Nu exista optiunea!')
