class Film:
    def __init__(self, id_, titlu, an_aparitie, pret_bilet, in_program):
        self.id_ = id_
        self.titlu = titlu
        self.an_aparitie = an_aparitie
        self.pret_bilet = pret_bilet
        self.in_program = in_program

    def __str__(self):
        return 'ID film : {}, Titlu : {}, An aparitie : {}, Pret bilet : {}, In program : {}'.format(self.id_,
                                                                                                     self.titlu,
                                                                                                     self.an_aparitie,
                                                                                                     self.pret_bilet,
                                                                                                     self.in_program)

    def get_id(self):
        return self.id_

    def get_titlu(self):
        return self.titlu

    def get_an_aparitie(self):
        return self.an_aparitie

    def get_pret_bilet(self):
        return self.pret_bilet

    def get_in_program(self):
        return self.in_program

    def set_id(self, id_nou):
        self.id_ = id_nou

    def set_titlu(self, titlu_nou):
        self.titlu = titlu_nou

    def set_an_aparitie(self, an_nou):
        self.an_aparitie = an_nou

    def set_pret_bilet(self, pret_nou):
        self.pret_bilet = pret_nou

    def set_in_program(self, program_nou):
        self.in_program = program_nou
