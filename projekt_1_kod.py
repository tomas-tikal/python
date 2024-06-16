
"""
projekt_1.py: prvni projekt do Engeto Online Python Akademie

author: Tomas TIKAL
email: tikal@3t.cz
discord: ti_to_80805
"""
import string

import projekt_1_knihovna
from projekt_1_knihovna import *

# seznam existujicich registrovanych uzivatelu (slovnik VSTUP)
uzivatele = {"bob": "pass", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# prihlaseni uzivatele (slovnik VZOREK)
jmeno = input("Prihlasovaci jmeno: ")
heslo = input("heslo: ")
prihlaseni = {jmeno: heslo}

# vyhodnoceni existence jmena a hesla v registrovanych uzivatelich
if(not porovnej_slovnik(uzivatele, prihlaseni)):
    print("Nejsi registrovany uzivatel, koncis :(")
    exit()
else:
    print("GRATULUJI registrovany uzivateli, vstup do aplikace POVOLEN :)")

# print("Nyni vyber jednu z variant textu nize. Povolene hodnoty jsou cislice 1,2 nebo 3: ")

#  vstup od uzivatele, otestovani povolenych hodnot a ulozeni volby do 'seznam_slov'
while True:
    pocet_textu = len(projekt_1_knihovna.TEXTS)
    print("zadej volbu od 1 do", pocet_textu , "nebo písmeno Q pro konec: \n", end="")
    volba = input()
    povolene_volby = []
    v = 1
    while v <= pocet_textu:
        povolene_volby.append(str(v))
        v += 1
    povolene_volby.append('q')
    povolene_volby.append('Q')

    if(not (volba in povolene_volby)):
        print("Povolené volby jsou pouze:", povolene_volby)
        print("Špatná volba, program končí")
        exit()

    seznam_slov = str.split(TEXTS[int(volba)-1])
    break

# pocet slov
print("Výpis obsahuje", len(seznam_slov), "slov ve vybraném textu.")

pocet_vyskytu_velke_pismeno = {}
pocet_vyskytu_velka_pismena = {}
pocet_vyskytu_mala_pismena = {}
pocet_vyskytu_cislo_pismena = {}

for slovo in seznam_slov:
    # při výskytu slova s velkym prvnim pismenem se zvýší obsah počítadla o 1
    if(str.isupper(list(slovo)[0])):
        pocet_vyskytu_velke_pismeno[slovo] = pocet_vyskytu_velke_pismeno.get(slovo, 0) + 1

    # při výskytu slova s velkymi pismeny se zvýší obsah počítadla o 1
    if(str.isupper(slovo)):
        if(not je_cislice(slovo)):
            continue
        else:
            pocet_vyskytu_velka_pismena[slovo] = pocet_vyskytu_velka_pismena.get(slovo, 0) + 1

    # při výskytu slova s malymi pismeny se zvýší obsah počítadla o 1
    if(str.islower(slovo)):
        pocet_vyskytu_mala_pismena[slovo] = pocet_vyskytu_mala_pismena.get(slovo, 0) + 1

    # při výskytu cisla se zvýší obsah počítadla o 1
    if(str.isnumeric(slovo)):
        pocet_vyskytu_cislo_pismena[slovo] = pocet_vyskytu_cislo_pismena.get(slovo, 0) + 1

print("Výpis obsahuje", sum(pocet_vyskytu_velke_pismeno.values()) , "s prvním velkým písmenem.")
print("Výpis obsahuje", sum(pocet_vyskytu_velka_pismena.values()) , "velkými písmeny.")
print("Výpis obsahuje", sum(pocet_vyskytu_mala_pismena.values()) , "malými písmeny.")
print("Výpis obsahuje", sum(pocet_vyskytu_cislo_pismena.values()) , "čísel.")

# soucet vsech cisel
pocet_vyskytu_velka_pismena = {}
suma = 0
for slovo in seznam_slov:
    # soucet 
    if(str.isnumeric(slovo)):
        suma += int(slovo)
print("Součet všech čísel ", suma)

# cetnost ruznych delek slov v textu
pocet_vyskytu = {}
for slovo in seznam_slov:
        slovo = slovo.replace(',', '')
        slovo = slovo.replace('.', '')
        klic = len(slovo)
        if klic not in pocet_vyskytu:
            pocet_vyskytu.update({klic: 1})
        else:
            pocet_vyskytu.update({klic: pocet_vyskytu.get(klic) + 1})

pocet_vyskytu_sorted = dict(sorted(pocet_vyskytu.items()))

# vypise tabulku
nejvice_vyskytu = max(zip(pocet_vyskytu_sorted.values(), pocet_vyskytu_sorted.keys()))[0]

hlavicka_delka = "LEN"
hlavicka_pocet_hvezdicky = "OCCURENCES"
hlavicka_pocet_cislo = "NR."
print()

print(hlavicka_delka, "|", hlavicka_pocet_hvezdicky, " " * (nejvice_vyskytu - 10), "|", hlavicka_pocet_cislo, sep = "")

for delka_slova, pocet_slov in pocet_vyskytu_sorted.items():
    if(delka_slova < 10):
        print(' ' * (len(hlavicka_delka) - 1) , delka_slova, '|', '*' * pocet_slov, " " * (nejvice_vyskytu - pocet_slov), '|', pocet_slov, sep = "")
    else:
        print(' ' * (len(hlavicka_delka) - 2) , delka_slova, '|', '*' * pocet_slov, " " * (nejvice_vyskytu - pocet_slov), '|', pocet_slov, sep = "")






