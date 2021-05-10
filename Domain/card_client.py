class CardClient:
    def __init__(self, id_, nume, prenume, CNP, data_nastere, data_inregistrare, puncte_acumulate):
        self.id_ = id_
        self.nume = nume
        self.prenume = prenume
        self.cnp = CNP
        self.data_nastere = data_nastere
        self.data_inregistrare = data_inregistrare
        self.puncte = puncte_acumulate

    def __str__(self):
        return 'ID : {}, Nume : {}, Prenume : {}, CNP : {}, Data nastere : {}, Data inregistrare : {}, Puncte ' \
               'acumulate : {}'.format(self.id_, self.nume, self.prenume, self.cnp, self.data_nastere,
                                       self.data_inregistrare, self.puncte)

    def get_id(self):
        return self.id_

    def get_nume(self):
        return self.nume

    def get_prenume(self):
        return self.prenume

    def get_cnp(self):
        return self.cnp

    def get_data_nastere(self):
        return self.data_nastere

    def get_data_inregistrare(self):
        return self.data_inregistrare

    def get_puncte_acumulate(self):
        return self.puncte

    def set_id(self, id_nou):
        self.id_ = id_nou

    def set_nume(self, nume_nou):
        self.nume = nume_nou

    def set_prenume(self, prenume_nou):
        self.prenume = prenume_nou

    def set_cnp(self, cnp):
        self.cnp = cnp

    def set_data_nastere(self, data_noua):
        self.data_nastere = data_noua

    def set_data_inregistrare(self, data_noua):
        self.data_inregistrare = data_noua

    def set_puncte_acumulate(self, puncte):
        self.puncte = puncte
