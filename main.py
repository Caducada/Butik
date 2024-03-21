import os
import random
import datetime
import kontroll
import kampanj_manager
from produkt import Produkt
from kampanj import Kampanj
from termcolor import colored
from kundvagn import Kundvagn
from produkt_manager import Produkt_manager

def run(produktlista, kampanjlista):
    while True:
        print("______Huvudmeny______")
        huvud_val = input(
            "1: Registrera en ny betalning\n2: Administrera kassan\n3: "
            + colored("Avsluta", "red")
            + "\n"
        )
        if huvud_val == "1":
            temp_kund = Kundvagn(produktlista, kampanjlista)
            while True:
                print(
                    ' Skriv "PAY" för att registrera betalningen i systemet. Skriv "b" för att gå tillbaka'
                )
                kassa_svar = input("Kommandon: <produkt-id> <gram/st> \n").split()
                if (
                    len(kassa_svar) == 1
                    and kassa_svar[0].lower() == "pay"
                    and temp_kund.vagn_kontroll(datetime.datetime.now())
                ):
                    now = datetime.datetime.now()
                    temp_kund.skriv_kvitto(now)
                    temp_kund.debitera(now)
                    break
                elif len(kassa_svar) == 1 and kassa_svar[0].lower() == "b":
                    break 
                elif (
                    len(kassa_svar) > 2
                    or not len(kassa_svar)
                    or len(kassa_svar) == 1
                    and kassa_svar[0].lower() != "pay"
                ):
                    print(colored("Ogilig input", "red"))
                elif (
                    len(kassa_svar) != 1
                    and kontroll.id_kontroll(kassa_svar[0], produktlista)
                    and kontroll.mängd_kontroll(kassa_svar[1])
                ):
                    if produktlista[kassa_svar[0]].get_typ() == "st":
                        temp_kund.add_produkt(kassa_svar[0], int(kassa_svar[1]))
                        print(
                            colored(
                                f"{kassa_svar[1]}st {produktlista[kassa_svar[0]].get_namn()}"
                                + " lades till i den nuvarande kundvagnen",
                                "green",
                            )
                        )

                    else:
                        temp_kund.add_produkt(
                            kassa_svar[0], float(kassa_svar[1]) / 1000
                        )
                        print(
                            colored(
                                f"{float(kassa_svar[1])/1000}kg {produktlista[kassa_svar[0]].get_namn()}"
                                + " lades till i den nuvarande kundvagnen",
                                "green",
                            )
                        )
        elif huvud_val == "2":
            while True:
                breaker = False
                print("______Administrations_meny______")
                admin_val = input(
                    "1: Lägg till en produkt\n2: Ändra en produkt\n3: Lägg till en kampanj\n4:"
                    + " Ändra en kampanj\n5:"
                    + colored(" Gå tillbaka", "yellow")
                    + "\n"
                )
                if admin_val == "1":
                    if len(produktlista) != (10**4):
                        while True:
                            temp_id = (
                                str(random.randint(0, 9))
                                + str(random.randint(0, 9))
                                + str(random.randint(0, 9))
                                + str(random.randint(0, 9))
                            )
                            if temp_id not in produktlista:
                                break
                        while True:
                            temp_namn = (
                                input(
                                    "Vänligen ange namnet på den produkt "
                                    "som du vill lägga till i systemet \n"
                                )
                                .lower()
                                .replace(" ", "_")
                            )
                            if kontroll.namn_kontroll(temp_namn, produktlista):
                                break
                        while True:
                            temp_typ = input(
                                f"Vänligen ange rätt typ av pris för din produkt {temp_namn}. st/kg \n"
                            ).lower()
                            if temp_typ == "kg" or temp_typ == "st":
                                break
                            else:
                                print(colored("Ogilitig input", "red"))
                        while True:
                            temp_pris = input(
                                f"Vänligen ange priset på din produkt {temp_namn} \n"
                            )
                            if kontroll.pris_kontroll(temp_pris):
                                break
                        produktlista.setdefault(
                            temp_id,
                            Produkt(
                                temp_namn,
                                temp_typ,
                                temp_pris,
                            ),
                        )
                        with open("produktlista.txt", "a+", encoding="utf-8") as bas:
                            bas.write(
                                temp_id
                                + " "
                                + temp_namn
                                + " "
                                + temp_pris
                                + "kr "
                                + temp_typ
                                + "\n"
                            )
                        print(
                            colored(
                                f"Grattis! Din produkt {temp_namn} lades till i systemet med id-et: {temp_id}",
                                "green",
                            )
                        )
                        break
                    else:
                        print(
                            colored(
                                "Det finns tyvärr inte plats med några fler produkter i systemet",
                                "red",
                            )
                        )
                elif admin_val == "2":
                    if len(produktlista):
                        while True:
                            id_val = input(
                                "Vänligen ange id-et på den produkt som du vill administrera \n"
                            )
                            if kontroll.id_kontroll(id_val, produktlista):
                                break
                        temp_manager = Produkt_manager(id_val, produktlista)
                        while True:
                            if id_val not in produktlista:
                                break
                            print(f"______{produktlista[id_val].get_namn()}_meny_____")
                            admin_val = input(
                                "1: Ändra produktens namn\n2: Ändra produktens pristyp"
                                + "\n3: Ändra produktens pris\n4: "
                                + colored("Ta bort produkten", "red")
                                + "\n5:"
                                + colored(" Gå tillbaka\n", "yellow")
                            )

                            if admin_val == "1":
                                produktlista = temp_manager.manage_namn()
                            elif admin_val == "2":
                                produktlista = temp_manager.manage_typ()
                            elif admin_val == "3":
                                produktlista = temp_manager.manage_pris()
                            elif admin_val == "4":
                                produktlista = temp_manager.del_produkt()
                            elif admin_val == "5":
                                break
                    else:
                        print(
                            colored(
                                "Det finns tyvärr inga produkter i det nuvarande kassasystemet",
                                "red",
                            )
                        )
                elif admin_val == "3":
                    now = datetime.datetime.now()
                    while True:
                        id_val = input(
                            "Vänligen ange id-et på den produkt som du vill koppla till en kampanj \n"
                        )
                        if kontroll.id_kontroll(id_val, produktlista):
                            break
                    while True:
                        kampanj_namn = input(
                            f"Vänligen ange namnet på din kampanj som du vill koppla "
                            + f"till produkten {produktlista[id_val].get_namn()} \n"
                        ).replace(" ", "_")
                        if kontroll.kampanj_namn_kontroll(
                            kampanj_namn, kampanjlista, id_val
                        ):
                            break
                    while True:
                        kampanj_start = kontroll.date_kontroll(
                            input(
                                "Vänligen ange när din kampanj ska börja (år + månad + dag) \n"
                            ).split(),
                            kampanjlista,
                            id_val,
                        )
                        if kampanj_start:
                            break
                    while True:
                        Kampanj_slut = kontroll.date_kontroll(
                            input(
                                "Vänligen ange när din kampanj ska sluta (år + månad + dag) \n"
                            ).split(),
                            kampanjlista,
                            id_val,
                        )
                        if Kampanj_slut:
                            if kampanj_start < Kampanj_slut:
                                break
                            else:
                                print(
                                    colored(
                                        "Ogiltig input. Ett slutdatum måste vara minst en dag efter startdatumet",
                                        "red",
                                    )
                                )
                    while True:
                        if produktlista[id_val].get_typ() == "st":
                            while True:
                                tröskel = input(
                                    f"Vänligen ange hur många av produkten {produktlista[id_val].get_namn()} "
                                    + f"en kund behöver köpa för att aktivera kampanjen {kampanj_namn} \n"
                                )
                                if tröskel.isnumeric():
                                    if int(tröskel) != 0:
                                        tröskel = float(tröskel)
                                        break
                                    else:
                                        print(
                                            colored(
                                                "Ogiltig input. Det är ej möjligt att köpa 0st av en produkt",
                                                "red",
                                            )
                                        )
                                else:
                                    print("Ändast siffror, tack")
                            break
                        else:
                            while True:
                                tröskel = input(
                                    f"Vänligen ange hur många gram eller av produkten {produktlista[id_val].get_namn()} "
                                    + f"en kund behöver köpa för att aktivera kampanjen {kampanj_namn} \n"
                                )
                                if tröskel.isnumeric():
                                    if int(tröskel) != 0:
                                        tröskel = float(tröskel) / 1000
                                        break
                                    else:
                                        print(
                                            colored(
                                                "Ogiltig input. Det är ej möjligt att köpa 0kg av en produkt",
                                                "red",
                                            )
                                        )
                                else:
                                    print(colored("Ändast siffror, tack", "red"))
                            break
                    while True:
                        minskning_procent = input(
                            "Vänligen ange hur många procent mindre en kund behöver "
                            + "betala för produkten om hen aktiverar kampanjen \n"
                        )
                        if not minskning_procent.isnumeric():
                            print(colored("Ändast siffror, tack", "red"))
                            continue
                        if int(minskning_procent) > 99:
                            print(
                                colored(
                                    "Ogiltig input. En produkt kan inte vara gratis",
                                    "red",
                                )
                            )
                            continue
                        if int(minskning_procent) == 0:
                            print(
                                colored(
                                    "Ogiltig input. En kampanj måste minska en produkts pris med minst en procent",
                                    "red",
                                )
                            )
                            continue
                        break
                    with open("kampanjlista.txt", "a", encoding="utf-8") as bas:
                        bas.write(
                            kampanj_namn
                            + " "
                            + id_val
                            + " "
                            + kampanj_start.strftime("%x")
                            + " "
                            + Kampanj_slut.strftime("%x")
                            + " "
                            + str(tröskel)
                            + " "
                            + str(round((100 - int(minskning_procent)) / 100, 5))
                            + "\n"
                        )
                    kampanjlista.append(
                        Kampanj(
                            id_val,
                            kampanj_namn,
                            kampanj_start,
                            Kampanj_slut,
                            tröskel,
                            round((100 - int(minskning_procent)) / 100, 5),
                        )
                    )

                    print(
                        colored(
                            f"Grattis! Din kampanj: {kampanj_namn} "
                            + f"kopplades till produkten {produktlista[id_val].get_namn()}",
                            "green",
                        )
                    )
                elif admin_val == "4":
                    if len(kampanjlista) != 1:
                        while True:
                            if breaker == True:
                                break
                            id_finns = False
                            kampanj_id_val = input(
                                "Vänligen ange id-et som kampanjen du vill ändra är kopplad till\n"
                            )
                            if kontroll.id_kontroll(kampanj_id_val, produktlista):
                                for kampanj in kampanjlista:
                                    if kampanj.get_id() == kampanj_id_val:
                                        id_finns = True
                                if id_finns:
                                    break
                                else:
                                    print(
                                        colored(
                                            "Id-et du angav har tyvärr inga kampanjer kopplade till sig",
                                            "red",
                                        )
                                    )
                        while True:
                            kampanj_namn_val = input(
                                f"Vänligen ange namnet på den kampanj som är kopplad till produkten"
                                + f"{produktlista[kampanj_id_val]} och som du vill ändra\n"
                            ).replace(" ", "_")
                            for kampanj in kampanjlista:
                                namn_finns = False
                                if (
                                    kampanj_namn_val == kampanj.get_namn()
                                    and kampanj_id_val == kampanj.get_id()
                                ):
                                    kampanjlista = kampanj_manager.run_manager(
                                        kampanj, kampanjlista, produktlista
                                    )
                                    namn_finns = True
                                    break
                            if namn_finns:
                                breaker = True
                                break
                            else:
                                print(
                                    colored(
                                        f"Produkten {produktlista[kampanj_id_val].get_namn()} har "
                                        + f"tyvärr ingen kampanj med namnet {kampanj_namn_val}",
                                        "red",
                                    )
                                )
                    else:
                        print(
                            colored(
                                "Det finns tyvärr inga kampanjer i den nuvarande kassan",
                                "red",
                            )
                        )
                elif admin_val == "5":
                    break
        elif huvud_val == "3":
            os.system("cls" if os.name == "nt" else "clear")
            exit()
        else:
            print(colored("Ogiltig input", "red"))


def start_up():
    produktlista = {
        "7772": Produkt(
            "skinksmörgås",
            "st",
            "45",
        ),
        "6229": Produkt(
            "redbull",
            "st",
            "15",
        ),
        "2637": Produkt(
            "lösgodis",
            "kg",
            "125",
        ),
    }
    kampanj_lista = [
        Kampanj(
            "all",
            "ingen_kampanj",
            datetime.datetime(1000, 1, 1),
            datetime.datetime(1000, 1, 1),
            0,
            1,
        ),
        Kampanj(
            "2637",
            "Halloween_2023",
            datetime.datetime(2023, 10, 15),
            datetime.datetime(2023, 11, 15),
            0.5,
            0.5,
        ),
    ]

    if not os.path.isfile("kampanjlista.txt"):
        with open("kampanjlista.txt", "w+", encoding="utf-8") as bas:
            for kampanj in kampanj_lista:
                bas.write(
                    kampanj.get_namn()
                    + " "
                    + kampanj.get_id()
                    + " "
                    + kampanj.get_start().strftime("%x")
                    + " "
                    + kampanj.get_slut().strftime("%x")
                    + " "
                    + str(kampanj.get_tröskel())
                    + " "
                    + str(kampanj.get_faktor())
                    + "\n"
                )
    else:
        kampanj_lista.clear()
        with open("kampanjlista.txt", "r+", encoding="utf-8") as bas:
            läsa = bas.read().split("\n")
            for temp_kampanj in läsa:
                temp_ordlista = temp_kampanj.split()
                if len(temp_ordlista) == 6:
                    kampanj_lista.append(
                        Kampanj(
                            temp_ordlista[1],
                            temp_ordlista[0],
                            datetime.datetime.strptime(temp_ordlista[2], "%x"),
                            datetime.datetime.strptime(temp_ordlista[3], "%x"),
                            float(temp_ordlista[4]),
                            float(temp_ordlista[5]),
                        )
                    )
                elif len(temp_ordlista) == 4:
                    for kampanj in kampanj_lista:
                        if (
                            kampanj.get_namn() == temp_ordlista[0]
                            and kampanj.get_id() == temp_ordlista[1]
                        ):
                            kampanj_lista.pop(kampanj_lista.index(kampanj))

    if not os.path.isfile("produktlista.txt"):
        with open("produktlista.txt", "w+", encoding="utf-8") as bas:
            for id in produktlista.keys():
                bas.write(
                    id
                    + " "
                    + produktlista[id].get_namn()
                    + " "
                    + produktlista[id].get_pris()
                    + "kr "
                    + produktlista[id].get_typ()
                    + "\n"
                )
    else:
        produktlista.clear()
        with open("produktlista.txt", "r", encoding="utf-8") as bas:
            läsa = bas.read()
            for temp_produkt in läsa.split("\n"):
                temp_ordlista = temp_produkt.split()
                if len(temp_ordlista) == 4:
                    produktlista[temp_ordlista[0]] = Produkt(
                        temp_ordlista[1],
                        temp_ordlista[3],
                        temp_ordlista[2][0:-2],
                    )
                elif len(temp_ordlista) == 9:
                    produktlista.pop(temp_ordlista[4])
    run(produktlista, kampanj_lista)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    start_up()
