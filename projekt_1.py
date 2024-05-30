
"""
projekt_1.py: prvni projekt do Engeto Online Python Akademie

author: Tomas TIKAL
email: tikal@3t.cz
discord: ti_to_80805
"""
import string

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

# definice funkce, ktera zjisti, zdali ve slovniku 'VSTUP' se nachazi hodnoty vlozene uzivatelem 'VZOREK'
def porovnej_slovnik(vstup, vzorek):
    for key, value in vzorek.items():
        if key not in vstup or vstup[key] != value:
            return False
    return True


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

# vytisteni na obrazovku:
# print("PRVNI: ", prvni_text)
# print("\n")
# print("DRUHY: ", druhy_text)
# print("\n")
# print("TRETI: ", treti_text)
# print("\n")


#  vstup od uzivatele, otestovani povolenych hodnot a ulozeni volby do 'seznam_slov'
while True:
    volba = input("Vloz cislici 1,2,3 nebo 9 pro konec: \n")
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
        case "9":
            print("Vlozena cislice 9, program je ukocen.")
            exit()
        case default:
            print("Zkus to znova :) \n")
            continue
         
# testovaci vypisy
# print()
# print(seznam_slov)
# print()

# pocet slov
print("There are ", len(seznam_slov), " words in the selected text.")

# pocet slov s prvnim velkym pismenem
pocet_vyskytu_velke_pismeno = {}
for slovo in seznam_slov:
    # při výskytu slova s velkym prvnim pismenem se zvýší obsah počítadla o 1
    if(str.isupper(list(slovo)[0])):
        pocet_vyskytu_velke_pismeno[slovo] = pocet_vyskytu_velke_pismeno.get(slovo, 0) + 1
print("There are ", len(pocet_vyskytu_velke_pismeno) , "titlecase words.")

# pocet slov psanych velkymi pismeny
pocet_vyskytu_velka_pismena = {}
for slovo in seznam_slov:
    # při výskytu slova s velkymi pismeny se zvýší obsah počítadla o 1
    if(str.isupper(slovo)):
        pocet_vyskytu_velka_pismena[slovo] = pocet_vyskytu_velka_pismena.get(slovo, 0) + 1
print("There are ", len(pocet_vyskytu_velka_pismena) , "uppercase words. Jsou to: ", pocet_vyskytu_velka_pismena.keys())

# pocet slov psanych malymi pismeny
pocet_vyskytu_velka_pismena = {}
for slovo in seznam_slov:
    # při výskytu slova s malymi pismeny se zvýší obsah počítadla o 1
    if(str.islower(slovo)):
        pocet_vyskytu_velka_pismena[slovo] = pocet_vyskytu_velka_pismena.get(slovo, 0) + 1
print("There are ", len(pocet_vyskytu_velka_pismena) , "lowercase words.")

# pocet slov, ktera obsahuji cislo
pocet_vyskytu_velka_pismena = {}
for slovo in seznam_slov:
    # při výskytu cisla se zvýší obsah počítadla o 1
    if(str.isnumeric(slovo)):
        pocet_vyskytu_velka_pismena[slovo] = pocet_vyskytu_velka_pismena.get(slovo, 0) + 1
print("There are ", len(pocet_vyskytu_velka_pismena) , " numeric strings. Jsou to: ", pocet_vyskytu_velka_pismena.keys())

# soucet vsech cisel
pocet_vyskytu_velka_pismena = {}
suma = 0
for slovo in seznam_slov:
    # soucet 
    if(str.isnumeric(slovo)):
        suma += int(slovo)
print("The sum of all the numbers ", suma)

# cetnost ruznych delek slov v textu
pocet_vyskytu = {}
for slovo in seznam_slov:
        klic = len(slovo)
        if klic not in pocet_vyskytu:
            pocet_vyskytu.update({klic: 1})
        else:
            pocet_vyskytu.update({klic: pocet_vyskytu.get(klic) + 1})

pocet_vyskytu_sorted = dict(sorted(pocet_vyskytu.items()))
# print(pocet_vyskytu_sorted)

# vypise tabulku
hlavicka_delka = "Delka slova"
hlavicka_pocet = "Pocet slov"
print()
print(hlavicka_delka, "|", hlavicka_pocet)

for delka_slova, pocet_slov in pocet_vyskytu_sorted.items():
    #print('{}: {}'.format(delka_slova, pocet_slov))
    if(delka_slova < 10):
        print(' ' * (len(hlavicka_delka) - 2) , delka_slova, '|', '*' * pocet_slov, pocet_slov)
    else:
        print(' ' * (len(hlavicka_delka) - 3) , delka_slova, '|', '*' * pocet_slov, pocet_slov)






