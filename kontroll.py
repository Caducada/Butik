import datetime
from termcolor import colored

def id_kontroll(id, produktlista):
    """Kontrollerar att ett angivet id är giltigt"""
    ...
    if not id.isnumeric():
        print(colored("Ogiltig input. Ett produkt-id kan bara inehålla siffror", "red"))
        return False
    if len(id) != 4:
        print(colored("Ogilitg input. Ett produkt-id måste vara fyra siffror långt", "red"))
        return False
    for nyckel in produktlista.keys():
        if nyckel == id:
            return True
    print(colored("Id-et du angav finns tyvärr inte i systemet", "red"))


def mängd_kontroll(mängd, counter=0):
    """Kontrollerar att en angiven mängd är giltig"""
    ...
    for tecken in mängd:
        if tecken == ".":
            counter += 1
    if (
        counter == 1
        and mängd[0 : mängd.index(".")].isnumeric()
        and mängd[mängd.index(".") + 1 : len(mängd)].isnumeric()
    ):
        print(colored("Ogilit mängd. Decimaltal är ej tillåtna", "red"))
        return False
    if mängd[0] == "-":
        if (
            counter == 1
            and mängd[1 : len(mängd)].replace(".", "").isnumeric()
            and str(mängd)[1] != "."
            and mängd[-1] != "."
        ):
            print(colored("Ogilig mängd. Negativa tal är ej tillåtna", "red"))
            return False
        elif mängd[1 : len(mängd)].isnumeric():
            print(colored("Ogilig mängd. Negativa tal är ej tillåtna", "red"))
            return False
    if not mängd.isnumeric():
        print(colored("Ogilig input. En mängd kan endast vara en siffra", "red"))
        return False
    if float(mängd) == 0:
        print(colored("Ogiltigt input. Mängden måste vara större än 0", "red"))
        return False
    return True


def pris_kontroll(siffra, counter=0):
    """Kontrollerar att ett angivet pris är riktigt"""
    ...
    for tecken in siffra:
        if tecken == ".":
            counter += 1
    if (
        siffra.isnumeric()
        or counter == 1
        and siffra[0 : siffra.index(".")].isnumeric()
        and siffra[siffra.index(".") + 1 : len(siffra)].isnumeric()
    ):
        return True
    else:
        print(colored("Ogilitig input. Ändast siffror är tillåtna", "red"))


def namn_kontroll(namn, produktlista, counter=0):
    """Kontrollerar att ett angivet namn är giltigt"""
    ...
    if not len(namn):
        print(colored("Ogiltig input. Ett namn måste inehålla minst en bokstav", "red"))
        return False
    for id in produktlista:
        if produktlista[id].get_namn() == namn:
            print(colored("Denna produkt finns tyvärr redan registrerad i systemet", "red"))
            return False
    for tecken in namn:
        if tecken == "_":
            counter += 1
        if not tecken.isalpha() and not tecken == "_":
            print(colored("Ändast bokstäver, tack", "red"))
            return False
    if len(namn) == counter:
        print(colored("Ogiltig input. Ett namn måste inehålla minst en bokstav", "red"))
        return False
    return True


def kampanj_namn_kontroll(namn, kampanjlista, id, counter=0):
    """Kontrollerar om ett namn för en kampanj är giltigt"""
    if not len(namn):
        print(colored("Ogiltig input. Ett namn måste inehålla minst en bokstav", "red"))
        return False
    for tecken in namn:
        if tecken == "_" or not tecken.isalpha():
            counter += 1
    if counter == len(namn):
        print(colored("Ogiltig input. Ett namn måste inehålla minst en bokstav", "red"))
        return False
    for kampanj in kampanjlista:
        if kampanj.get_namn() == namn and kampanj.get_id() == id:
            print(
                colored("Ogiltig input. En kampanj med detta namn "
                + "och id finns redan kopplat till den nuvarande produkten", "red")
            )
            return False
    return True


def date_kontroll(date, kampanjlista, id):
    """Kontrollerar att ett angivet datum är giltigt och retunerar det i sådana fall"""
    ...
    while True:
        if len(date) == 3:
            try:
                dt_kampanj = datetime.datetime.strptime(
                    date[0] + "-" + date[1] + "-" + date[2], "%Y-%m-%d"
                )
                break
            except ValueError:
                print(colored("Ogiltig datum", "red"))
                return False
        else:
            print(colored("Ogilitg input", "red"))
            return False
    for kampanj in kampanjlista:
        if (
            id == kampanj.get_id()
            and kampanj.get_start() <= dt_kampanj <= kampanj.get_slut()
        ):
            print(
                colored("Ogiltigt datum. Produkten har redan en kampanj kopplad till sig under denna period", "red")
            )
            return False
    return dt_kampanj
