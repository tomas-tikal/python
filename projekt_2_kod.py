
"""
projekt_1.py: prvni projekt do Engeto Online Python Akademie

author: Tomas TIKAL
email: tikal@3t.cz
discord: ti_to_80805
"""

import random
import projekt_2_knihovna


print("Ahoj.")
print("-------------------------------")
print("Vygeneruji Ti 4 číslice pro hru")
print("Krávy a bejci.")
print("-------------------------------")

while True:
    cislo_tajne = random.randrange(1000,9999)
    if(len(list(str(cislo_tajne))) != len(set(str(cislo_tajne)))):
        continue
    break

pocet_pokusu = 0
while True:
    cislo_uzivatel = projekt_2_knihovna.vstup_uzivatele()
    # odkomentuj pro vypisování tajného čísla:
    #print("Vybrané počítačem:", cislo_tajne)

    ct = list(str(cislo_tajne))
    cu = list(str(cislo_uzivatel))

    print("Vybrané uživatelem:", cislo_uzivatel)
    bull = 0
    cow = 0

    for i in cu:
        if (i in ct):
            if (cu.index(i) == ct.index(i)):
                bull = bull + 1
            else:
                cow = cow + 1

    print("Bulls", bull) if bull > 1 else print("Bull", bull)
    print("Cows", cow) if cow > 1 else print("Cow", cow)

    pocet_pokusu = pocet_pokusu + 1
    if(bull == 4):
        print("Gratuluji, číslo jsi uhádl v celkem:", pocet_pokusu, " pokusech!")
        exit()



