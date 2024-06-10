
"""
projekt_1.py: prvni projekt do Engeto Online Python Akademie

author: Tomas TIKAL
email: tikal@3t.cz
discord: ti_to_80805
"""
import string
from projekt_1_knihovna import *

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

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

print("Nyni vyber jednu z variant textu nize. Povolene hodnoty jsou cislice 1,2 nebo 3: ")

# priprava textu
prvni_text = str(TEXTS[0])
druhy_text = str(TEXTS[1])
treti_text = str(TEXTS[2])

#  vstup od uzivatele, otestovani povolenych hodnot a ulozeni volby do 'seznam_slov'
while True:
    volba = input("Vloz cislici 1,2,3 nebo písmeno Q pro konec: \n")
    match volba:
        case "1":
            print("Vlozena cislice 1, jdu dal ... \n")
            seznam_slov = str.split(TEXTS[0])
            break
        case "2":
            print("Vlozena cislice 2, jdu dal ... \n")
            seznam_slov = str.split(TEXTS[1])
            break
        case "3":
            print("Vlozena cislice 3, jdu dal ... \n")
            seznam_slov = str.split(TEXTS[2])
            break
        case "q":
            print("Vlozeno písmeno q, program je ukocen.")
            exit()
        case "Q":
            print("Vlozeno písmeno Q, program je ukocen.")
            exit()
        case default:
            print("Zkus to znova :) \n")
            continue
         

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
    elif(str.isupper(slovo)):
        pocet_vyskytu_velka_pismena[slovo] = pocet_vyskytu_velka_pismena.get(slovo, 0) + 1

    # při výskytu slova s malymi pismeny se zvýší obsah počítadla o 1
    elif(str.islower(slovo)):
        pocet_vyskytu_mala_pismena[slovo] = pocet_vyskytu_mala_pismena.get(slovo, 0) + 1

    # při výskytu cisla se zvýší obsah počítadla o 1
    elif(str.isnumeric(slovo)):
        pocet_vyskytu_cislo_pismena[slovo] = pocet_vyskytu_cislo_pismena.get(slovo, 0) + 1

print("Výpis obsahuje", len(pocet_vyskytu_velke_pismeno) , "s prvním velkým písmenem.")
print("Výpis obsahuje", len(pocet_vyskytu_velka_pismena) , "velkými písmeny.")
print("Výpis obsahuje", len(pocet_vyskytu_mala_pismena) , "malými písmeny.")
print("Výpis obsahuje", len(pocet_vyskytu_cislo_pismena) , "čísel.")


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






