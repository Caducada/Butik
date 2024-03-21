import kontroll
from produkt import Produkt
from termcolor import colored


class Produkt_manager:
    def __init__(self, id, produktlista):
        self.id = id
        self.produktlista = produktlista
        self.temp_produkt = Produkt(
            produktlista[id].get_namn(),
            produktlista[id].get_typ(),
            produktlista[id].get_pris(),
        )

    def manage_namn(self):
        """Retunerar en ny produktlista där namnet på en specifik produkt har ändrats"""
        ...
        while True:
            namn_ändrad = input("Vänligen ange det nya namnet på produkten \n").replace(
                " ", "_"
            )
            if namn_ändrad == self.produktlista[self.id].get_namn():
                print(
                    colored(
                        "Ogiltig input. Namnet du angav är det samma som produktens nuvarande namn"
                    )
                )
                continue
            if kontroll.namn_kontroll(namn_ändrad, self.produktlista):
                print(
                    colored(
                        f"Grattis! Din produkt {self.produktlista[self.id].get_namn()}"
                        + f" bytte namn till {namn_ändrad}",
                        "green",
                    )
                )
                self.produktlista.pop(self.id)
                self.produktlista.setdefault(
                    self.id,
                    Produkt(
                        namn_ändrad,
                        self.temp_produkt.get_typ(),
                        self.temp_produkt.get_pris(),
                    ),
                )
                with open("produktlista.txt", "a+", encoding="utf-8") as bas:
                    bas.write(
                        self.id
                        + " "
                        + namn_ändrad
                        + " "
                        + self.produktlista[self.id].get_pris()
                        + "kr "
                        + self.produktlista[self.id].get_typ()
                        + "\n"
                    )
                return self.produktlista

    def manage_typ(self):
        """Retunerar en ny produktlista där pristypen på en specifik produkt har ändrats"""
        ...
        if self.produktlista[self.id].get_typ() == "st":
            self.produktlista.pop(self.id)
            self.produktlista.setdefault(
                self.id,
                Produkt(
                    self.temp_produkt.get_namn(), "kg", self.temp_produkt.get_pris()
                ),
            )
            self.temp_produkt == self.produktlista[self.id]
        else:
            self.produktlista.pop(self.id)
            self.produktlista.setdefault(
                self.id,
                Produkt(
                    self.temp_produkt.get_namn(), "st", self.temp_produkt.get_pris()
                ),
            )
            self.temp_produkt == self.produktlista[self.id]
        with open("produktlista.txt", "a+", encoding="utf-8") as bas:
            bas.write(
                self.id
                + " "
                + self.produktlista[self.id].get_namn()
                + " "
                + self.produktlista[self.id].get_pris()
                + "kr "
                + self.produktlista[self.id].get_typ()
                + "\n"
            )
        print(
            colored(
                f"Grattis! Pristypen på produkten {self.produktlista[self.id].get_namn()}"
                + f" har ändrats till {self.produktlista[self.id].get_typ()}",
                "green",
            )
        )
        return self.produktlista

    def manage_pris(self):
        """Retunerar en ny produktlista där priset på en specifik produkt har ändrats"""
        ...
        while True:
            pris_ändrad = input("Vänligen ange det nya priset på produkten \n")
            if pris_ändrad == self.produktlista[self.id].get_pris():
                print(
                    colored(
                        "Ogiltig input. Det nya priset kan inte vara samma som det gammla",
                        "red",
                    )
                )
                continue
            if kontroll.pris_kontroll(pris_ändrad):
                break

        self.produktlista.pop(self.id)
        self.produktlista.setdefault(
            self.id,
            Produkt(
                self.temp_produkt.get_namn(), self.temp_produkt.get_typ(), pris_ändrad
            ),
        )
        with open("produktlista.txt", "a+", encoding="utf-8") as bas:
            bas.write(
                self.id
                + " "
                + self.produktlista[self.id].get_namn()
                + " "
                + pris_ändrad
                + "kr "
                + self.produktlista[self.id].get_typ()
                + "\n"
            )
        print(
            colored(
                f"Grattis! Priset på produkten {self.produktlista[self.id].get_namn()} "
                + f"har ändrats till {pris_ändrad}",
                "green",
            )
        )
        return self.produktlista

    def del_produkt(self):
        """Låter användaren ta bort en produkt från produktlistan"""
        ...
        while True:
            incase = input(
                colored(
                    "Är du säker på att du vill ta port produkten {}? Y/N \n", "yellow"
                ).format(self.produktlista[self.id].get_namn())
            ).lower()
            if incase == "y" or incase == "n":
                break
            else:
                print(colored("Ogiltig input", "red"))
        if incase == "n":
            return self.produktlistaz
        else:
            with open("produktlista.txt", "a+", encoding="utf-8") as bas:
                bas.write(
                    "Produkten "
                    + self.produktlista[self.id].get_namn()
                    + " med id: "
                    + self.id
                    + " togs bort ifrån produktlistan\n"
                )
            self.produktlista.pop(self.id)
            print(
                colored(
                    f"Produkten {self.temp_produkt.get_namn()} "
                    f"med id-et {self.id} togs bort från systemet\n",
                    "yellow",
                )
            )
            return self.produktlista
