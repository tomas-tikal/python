# vstup uživatele:
def vstup_uzivatele():
    while True:
        cislo_uzivatel = input("Zadej čtyřmístné číslo bez opakování číslic: ")

        if (not (cislo_uzivatel.isnumeric() and (int(cislo_uzivatel) >= 1000 and int(cislo_uzivatel) <= 9999))):
            print("Nezadali jste platný vstup - čtyřmístné číslo bez opakování číslic, zkuste to znovu")
            continue

        if (len(list(cislo_uzivatel)) != len(set(cislo_uzivatel))):
            print("Nezadali jste platný vstup - čtyřmístné číslo BEZ opakování číslic, zkuste to znovu")
            continue

        break
    return cislo_uzivatel




