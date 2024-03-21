import os
import kampanj_manager
from termcolor import colored


class Kundvagn:
    def __init__(self, produktlista, kampanj_lista):
        self.produktlista = produktlista
        self.temp_köp = {}
        self.priser = []
        self.kampanj_lista = kampanj_lista
        if not os.path.isfile("Löplista.txt"):
            with open("Löplista.txt", "w+", encoding="utf-8") as löplista:
                löplista.write("1\n")
        with open("Löplista.txt", "r+") as löpläsa:
            self.löpdelad = löpläsa.read().split("\n")

    def add_produkt(self, id, mängd):
        """Lägger till en produkt i den nuvarande kundvagnen"""
        ...
        if id not in self.temp_köp:
            self.temp_köp.setdefault(id, mängd)
        else:
            self.temp_köp[id] += mängd

    def vagn_kontroll(self, now):
        """Kontrollerar att ett köp kan genomföras"""
        ...
        if len(self.temp_köp):
            for id in self.temp_köp.keys():
                temp_kampanj = kampanj_manager.get_temp_kampanj(
                    self.kampanj_lista, id, self.temp_köp[id], now
                )
                if (
                    self.temp_köp[id]
                    * int(self.produktlista[id].get_pris())
                    * temp_kampanj.get_faktor()
                    < 0.5
                ):
                    print(
                        colored(f"Ogiltig mängd {self.produktlista[id].get_namn()}." 
                        +" Det totala priset för en produkt kan inte vara mindre än en krona", "red")
                    )
                    return False
                self.priser.append(
                    self.temp_köp[id]
                    * float(self.produktlista[id].get_pris())
                    * temp_kampanj.get_faktor()
                )
            return True
        else:
            print(
                colored("Ogilitg input. Du har inte lagt till några varor i den nuvarande kundvagnen", "red")
            )

    def skriv_kvitto(self, now):
        """Skriver ut ett kvitto i terminalen"""
        ...
        print(f"Kvitto: {self.löpdelad[-2]}")
        for id in self.temp_köp.keys():
            temp_kampanj = kampanj_manager.get_temp_kampanj(
                self.kampanj_lista, id, self.temp_köp[id], now
            )
            print(
                self.produktlista[id].get_namn()
                + ", "
                + str(self.temp_köp[id])
                + self.produktlista[id].get_typ()
                + ", "
                + str(
                    round(
                        float(self.produktlista[id].get_pris())
                        * self.temp_köp[id]
                        * temp_kampanj.get_faktor(),
                        5,
                    )
                )
                + "kr Kampanj: "
                + temp_kampanj.get_namn()
            )
        print(
            "Summa: "
            + str(round(sum(self.priser)))
            + "kr\n"
            + now.strftime("%c")
            + "\n_______________________________\n"
        )

    def debitera(self, now):
        """Skriver kvittot i en fil med dagens datum som namn"""
        ...
        with open(
            f'RECEIPTS_{now.strftime("%Y/%m/%d").replace("/","")}.txt', "a+", encoding="utf-8"
        ) as temp_kvitto:
            temp_kvitto.write("\nKvitto: " + self.löpdelad[-2] + "\n")
            for id in self.temp_köp.keys():
                temp_kampanj = kampanj_manager.get_temp_kampanj(
                    self.kampanj_lista, id, self.temp_köp[id], now
                )
                temp_kvitto.write(self.produktlista[id].get_namn() + ", ")
                if self.produktlista[id].get_typ() == "kg":
                    temp_kvitto.write(str(self.temp_köp[id]) + "kg, ")
                else:
                    temp_kvitto.write(str(int(self.temp_köp[id])) + "st, ")
                temp_kvitto.write(
                    str(
                        round(
                            float(self.produktlista[id].get_pris())
                            * self.temp_köp[id]
                            * temp_kampanj.get_faktor(),
                            5,
                        )
                    )
                    + "kr Kampaj: "
                    + temp_kampanj.get_namn()
                    + "\n"
                )
            temp_kvitto.write(
                "Summa: "
                + str(round(sum(self.priser)))
                + "kr\n"
                + now.strftime("%c")
                + "\n_______________________________\n"
            )

        with open("Löplista.txt", "a+") as löplista:
            löplista.write(str(int(self.löpdelad[-2]) + 1) + "\n")
