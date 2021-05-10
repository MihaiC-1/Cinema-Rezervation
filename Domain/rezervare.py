class Rezervare:
    def __init__(self, id_, id_film, id_card, data, ora):
        self.id_ = id_
        self.id_film = id_film
        self.id_card = id_card
        self.data = data
        self.ora = ora

    def __str__(self):
        return 'ID : {}, ID film : {}, ID card client : {}, Data : {}, Ora : {}'.format(self.id_, self.id_film,
                                                                                        self.id_card, self.data,
                                                                                        self.ora)

    def get_id(self):
        return self.id_

    def get_id_film(self):
        return self.id_film

    def get_id_card(self):
        return self.id_card

    def get_data(self):
        return self.data

    def get_ora(self):
        return self.ora

    def set_id(self, id_nou):
        self.id_ = id_nou

    def set_id_film(self, film):
        self.id_film = film

    def set_id_card(self, card):
        self.id_card = card

    def set_data(self, data_nou):
        self.data = data_nou

    def set_ora(self, ora_noua):
        self.ora = ora_noua
