from Repository.film_repo import *
from Repository.film_repo_validator import *


class ServiceFilm:
    def __init__(self):
        self.repo = RepoFilm('/Users/c.mihai/Desktop/exersare/laborator 8-9/filme.txt')

    def create(self, id_, titlu, an_aparitie, pret_bilet, in_program):
        clas = Film(id_, titlu, an_aparitie, pret_bilet, in_program)

        validare = FilmValidator(clas)
        validare.validare()

        self.repo.create(clas)

    def read(self, id_):
        return self.repo.read(id_)

    def update(self, id_, titlu, an_aparitie, pret_bilet, in_program):
        clas = Film(id_, titlu, an_aparitie, pret_bilet, in_program)

        validare = FilmValidator(clas)
        validare.validare()

        self.repo.update(clas)

    def delete(self, id_):
        self.repo.delete(id_)

    def show_all(self):
        return self.repo.all()

    def read_titlu(self, titlu):
        filme = self.show_all()
        rez = []
        for f in filme:
            if f.get_titlu() == titlu:
                rez.append(self.read(f.get_id()))
        return rez
