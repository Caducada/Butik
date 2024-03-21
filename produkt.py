class Produkt:
    def __init__(self, namn, pristyp, pris):
        self.namn = namn
        self.pristyp = pristyp
        self.pris = pris

    def get_namn(self):
        return self.namn

    def get_typ(self):
        return self.pristyp

    def get_pris(self):
        return self.pris

    
