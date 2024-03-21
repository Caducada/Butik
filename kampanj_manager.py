import datetime
import kontroll
from kampanj import Kampanj
from termcolor import colored


def run_manager(kampanj, kampanjlista, produktlista):
    """Låter användaren ändra en kampanj"""
    while True:
        print(f"______{kampanj.get_namn()}_meny_____")
        kampanj_admin = input(
            "1. Ändra namnet på kampanjen\n2. Ändra starten för kampanjen\n3. "
            + "Ändra slutet för kampanjen\n4. Ändra kampanjens tröskel. \n(Hur många/mycket av "
            + "produkten en kund behöver köpa för att aktivera kampanjen)\n"
            + "5. Ändra kampanjens faktror.\n(Hur mycket produktens pris kommer "
            + "att minska om kunden aktiverar kampanjen\n6."
            + colored(" Ta bort kampanjen", "red")
            + "\n7."
            + colored(" Gå tillbaka\n", "yellow")
        )
        if kampanj_admin == "1":
            while True:
                namn_ändrad = input(
                    "Vänligen ange det nya namnet på kampanjen \n"
                ).replace(" ", "_")
                if kontroll.kampanj_namn_kontroll(
                    namn_ändrad, kampanjlista, kampanj.get_id()
                ):
                    if namn_ändrad != kampanj.get_namn():
                        break
                    else:
                        print(
                            colored(
                                "Ogiltig input. Namnet du angav är detsamma som kampanjens nuvarsande namn\n",
                                "red",
                            )
                        )
            skriv_bort(kampanj)
            kampanjlista.append(
                Kampanj(
                    kampanj.get_id(),
                    namn_ändrad,
                    kampanj.get_start(),
                    kampanj.get_slut(),
                    kampanj.get_tröskel(),
                    kampanj.get_faktor(),
                )
            )
            print(
                colored(
                    f"Grattis! Din kampanj {kampanj.get_namn()} ändrade namn till {namn_ändrad}",
                    "green",
                )
            )
            kampanjlista.pop(kampanjlista.index(kampanj))
            with open("kampanjlista.txt", "a", encoding="utf-8") as bas:
                bas.write(
                    namn_ändrad
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
            kampanj = kampanjlista[-1]
        elif kampanj_admin == "2":
            while True:
                start_ändrad = input(
                    "Vänligen ange kampanjens nya startdatum med formatet (år + månad + dag)\n"
                ).split()
                if len(start_ändrad) == 3:
                    try:
                        dt_start_ändrad = datetime.datetime.strptime(
                            start_ändrad[0]
                            + "-"
                            + start_ändrad[1]
                            + "-"
                            + start_ändrad[2],
                            "%Y-%m-%d",
                        )
                        if dt_start_ändrad > kampanj.get_slut():
                            print(
                                colored(
                                    "Ogiltigt datum. Startdatumet kan inte inträffa efter kampanjens slutdatum",
                                    "red",
                                )
                            )
                        elif dt_start_ändrad == kampanj.get_slut():
                            print(
                                colored(
                                    "Ogiltigt datum. Startdatumet kan inte inträffa under kampanjens slutdatum",
                                    "red",
                                )
                            )
                        elif dt_start_ändrad == kampanj.get_slut():
                            print(
                                colored(
                                    "Ogiltigt datum. Startdatumet kan inte vara detsamma som slutdatumet",
                                    "red",
                                )
                            )
                        elif dt_start_ändrad == kampanj.get_start():
                            print(
                                colored(
                                    "Ogiltigt datum. Datumet du angav är detsamma som kampanjens nuvarande startdatum",
                                    "red",
                                )
                            )
                        else:
                            break
                    except ValueError:
                        print(colored("Ogiltigt datum", "red"))
                else:
                    print(colored("Ogiltig input", "red"))
            skriv_bort(kampanj)
            kampanjlista.append(
                Kampanj(
                    kampanj.get_id(),
                    kampanj.get_namn(),
                    dt_start_ändrad,
                    kampanj.get_slut(),
                    kampanj.get_tröskel(),
                    kampanj.get_faktor(),
                )
            )
            print(
                colored(
                    "Grattis! Din kampanj {} ändrade sitt startdatum till {}".format(
                        kampanj.get_namn(), dt_start_ändrad.strftime("%x")
                    ),
                    "green",
                )
            )
            kampanjlista.pop(kampanjlista.index(kampanj))
            with open("kampanjlista.txt", "a", encoding="utf-8") as bas:
                bas.write(
                    kampanj.get_namn()
                    + " "
                    + kampanj.get_id()
                    + " "
                    + dt_start_ändrad.strftime("%x")
                    + " "
                    + kampanj.get_slut().strftime("%x")
                    + " "
                    + str(kampanj.get_tröskel())
                    + " "
                    + str(kampanj.get_faktor())
                    + "\n"
                )
            kampanj = kampanjlista[-1]
        elif kampanj_admin == "3":
            while True:
                slut_ändrad = input(
                    "Vänligen ange kampanjens nya slutdatum med formatet (år + månad + dag)\n"
                ).split()
                if len(slut_ändrad) == 3:
                    try:
                        dt_slut_ändrad = datetime.datetime.strptime(
                            slut_ändrad[0]
                            + "-"
                            + slut_ändrad[1]
                            + "-"
                            + slut_ändrad[2],
                            "%Y-%m-%d",
                        )
                        if dt_slut_ändrad < kampanj.get_start():
                            print(
                                colored(
                                    "Ogiltigt datum. Slutdatumet kan inte inträffa innan kampanjens startdatun",
                                    "red",
                                )
                            )
                        elif dt_slut_ändrad == kampanj.get_start():
                            print(
                                colored(
                                    "Ogiltig datum. Slutdatumet kan inte vara detsamma som startdatumet",
                                    "red",
                                )
                            )
                        elif dt_slut_ändrad == kampanj.get_start():
                            print(
                                colored(
                                    "Ogiltigt datum. Startdatumet kan inte vara detsamma som slutdatumet",
                                    "red",
                                )
                            )
                        elif dt_slut_ändrad == kampanj.get_slut():
                            print(
                                colored(
                                    "Ogiltigt datum. Datumet du angav är detsamma som kampanjens nuvarande slutdatum",
                                    "red",
                                )
                            )
                        else:
                            break
                    except ValueError:
                        print(colored("Ogiltigt datum", "red"))
                else:
                    print(colored("Ogiltig input", "red"))
            skriv_bort(kampanj)
            kampanjlista.append(
                Kampanj(
                    kampanj.get_id(),
                    kampanj.get_namn(),
                    kampanj.get_start(),
                    dt_slut_ändrad,
                    kampanj.get_tröskel(),
                    kampanj.get_faktor(),
                )
            )
            print(
                colored(
                    "Grattis! Din kampanj {} ändrade sitt slutdatum till {}".format(
                        kampanj.get_namn(), dt_slut_ändrad.strftime("%x")
                    ),
                    "green",
                )
            )
            kampanjlista.pop(kampanjlista.index(kampanj))
            with open("kampanjlista.txt", "a", encoding="utf-8") as bas:
                bas.write(
                    kampanj.get_namn()
                    + " "
                    + kampanj.get_id()
                    + " "
                    + kampanj.get_start().strftime("%x")
                    + " "
                    + dt_slut_ändrad.strftime("%x")
                    + " "
                    + str(kampanj.get_tröskel())
                    + " "
                    + str(kampanj.get_faktor())
                    + "\n"
                )
            kampanj = kampanjlista[-1]
        elif kampanj_admin == "4":
            while True:
                if produktlista[kampanj.get_id()].get_typ() == "st":
                    while True:
                        tröskel_ändrad = input(
                            f"Vänligen ange hur många av produkten "
                            + f"{produktlista[kampanj.get_id()].get_namn()} "
                            + f"en kund behöver köpa för att aktivera kampanjen {kampanj.get_namn()} \n"
                        )
                        if tröskel_ändrad.isnumeric():
                            if float(tröskel_ändrad) == kampanj.get_tröskel():
                                print(
                                    colored(
                                        "Ogiltig input. Siffran du angav är detsamma "
                                        + "som kampanjens nuvarande tröskel",
                                        "red",
                                    )
                                )
                                continue
                            if float(tröskel_ändrad) != 0:
                                tröskel_ändrad = float(tröskel_ändrad)
                                break
                            else:
                                print(
                                    colored(
                                        "Ogiltig input. Det är ej möjligt att köpa 0st av en produkt",
                                        "red",
                                    )
                                )
                        else:
                            print(colored("Ändast siffror, tack", "red"))
                    break
                else:
                    while True:
                        tröskel_ändrad = input(
                            f"Vänligen ange hur många gram eller av produkten {produktlista[kampanj.get_id()].get_namn()} "
                            + f"en kund behöver köpa för att aktivera kampanjen {kampanj.get_namn()} \n"
                        )
                        if tröskel_ändrad.isnumeric():
                            if float(tröskel_ändrad) == kampanj.get_tröskel * 1000:
                                print(
                                    colored(
                                        "Ogiltig input. Siffran du angav är detsamma som kampanjens nuvarande tröskel",
                                        "red",
                                    )
                                )
                                continue
                            if float(tröskel_ändrad) != 0.0:
                                tröskel_ändrad = float(tröskel_ändrad) / 1000
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
            skriv_bort(kampanj)
            kampanjlista.append(
                Kampanj(
                    kampanj.get_id(),
                    kampanj.get_namn(),
                    kampanj.get_start(),
                    kampanj.get_slut(),
                    tröskel_ändrad,
                    kampanj.get_faktor(),
                )
            )
            print(
                colored(
                    "Grattis! Din kampanj {} ändrade sin tröskel till {}".format(
                        kampanj.get_namn(), tröskel_ändrad
                    ),
                    "green",
                )
            )
            kampanjlista.pop(kampanjlista.index(kampanj))
            with open("kampanjlista.txt", "a", encoding="utf-8") as bas:
                bas.write(
                    kampanj.get_namn()
                    + " "
                    + kampanj.get_id()
                    + " "
                    + kampanj.get_start().strftime("%x")
                    + " "
                    + kampanj.get_slut().strftime("%x")
                    + " "
                    + str(tröskel_ändrad)
                    + " "
                    + str(kampanj.get_faktor())
                    + "\n"
                )
            kampanj = kampanjlista[-1]
        elif kampanj_admin == "5":
            while True:
                minskning_procent = input(
                    "Vänligen ange hur många procent mindre en kund behöver "
                    + "betala för produkten om hen aktiverar kampanjen \n"
                )
                if not minskning_procent.isnumeric():
                    print(colored("Ändast siffror, tack"), "red")
                    continue
                if int(minskning_procent) > 99:
                    print(
                        colored("Ogiltig input. En produkt kan inte vara gratis"), "red"
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
                if (
                    round((100 - int(minskning_procent)) / 100, 5)
                    == kampanj.get_faktor()
                ):
                    print(
                        colored(
                            "Ogiltigt input. Siffran du angav är densamma som kampanjens nuvarande faktor",
                            "red",
                        )
                    )
                    continue
                break
            skriv_bort(kampanj)
            kampanjlista.append(
                Kampanj(
                    kampanj.get_id(),
                    kampanj.get_namn(),
                    kampanj.get_start(),
                    kampanj.get_slut(),
                    kampanj.get_tröskel(),
                    round((100 - int(minskning_procent)) / 100, 5),
                )
            )
            print(
                colored(
                    "Grattis! Din kampanj {} ändrade sin faktor till {}".format(
                        kampanj.get_namn(), minskning_procent
                    ),
                    "green",
                )
            )
            kampanjlista.pop(kampanjlista.index(kampanj))
            with open("kampanjlista.txt", "a", encoding="utf-8") as bas:
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
                    + str(round((100 - int(minskning_procent)) / 100, 5))
                    + "\n"
                )
            kampanj = kampanjlista[-1]

        elif kampanj_admin == "6":
            while True:
                incase = input(
                    colored(
                        f"Är du säker på att du vill ta bort kampanjen "
                        + f"{kampanj.get_namn()} ifrån produkten "
                        + f"{produktlista[kampanj.get_id()].get_namn()} (Y/N)\n",
                        "yellow",
                    )
                ).lower()
                if incase == "y" or incase == "n":
                    break
                else:
                    print(colored("Ogiltig input", "red"))
            if incase == "y":
                skriv_bort(kampanj)
                kampanjlista.pop(kampanjlista.index(kampanj))
                return kampanjlista
        elif kampanj_admin == "7":
            return kampanjlista
        else:
            print(colored("Ogiltig input", "red"))


def skriv_bort(kampanj):
    """Skriver att en kampanj togs bort i textfilen kampanjlista"""
    with open("kampanjlista.txt", "a", encoding="utf-8") as bas:
        bas.write(kampanj.get_namn() + " " + kampanj.get_id() + " " + "togs bort\n")


def get_temp_kampanj(kampanjlista, id, mängd, now):
    """Retunerar kampanjen som för tillfället påverkar en produkts pris"""
    ...
    temp_kampanjer = []
    for kampanj in kampanjlista:
        if (
            kampanj.get_id() == id
            and kampanj.get_start() <= now <= kampanj.get_slut()
            and kampanj.get_tröskel() <= mängd
        ):
            temp_kampanjer.append(kampanj)
    if len(temp_kampanjer):
        return temp_kampanjer[-1]
    return kampanjlista[0]
