class Kampanj:
    def __init__(self, id, namn, start, slut, tröskel, faktor):
        self.id = id
        self.namn = namn
        self.start = start
        self.slut = slut
        self.tröskel = tröskel
        self.faktor = faktor

    def get_id(self):
        return self.id

    def get_namn(self):
        return self.namn

    def get_start(self):
        return self.start

    def get_slut(self):
        return self.slut

    def get_tröskel(self):
        return self.tröskel

    def get_faktor(self):
        return self.faktor
    


