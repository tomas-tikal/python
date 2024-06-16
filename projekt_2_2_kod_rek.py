
"""
projekt_2_2.py: druhý projekt do Engeto Online Python Akademie

author: Tomas TIKAL
email: tikal@3t.cz
discord: ti_to_80805
"""
import projekt_2_2_knihovna_rek
while True:
    velikost_sachovnice = input("Zadej velikost strany šachového pole pro hru: ")
    if(not velikost_sachovnice.isdecimal()):
        print('\"Velikost strany\" musí být CELÉ KLADNÉ číslo, zkus to znova :)')
        continue
    break

# naplnění prázdné tabulky 8x8 buněk
sachovnice= []
for j in range(int(velikost_sachovnice)):
    sloupecek= []
    for i in range(int(velikost_sachovnice)):
        retezec = str(j)+'.'+str(i)
        sloupecek.append(retezec)
    sachovnice.append(sloupecek)

# pomocná proměnná možných indexů v šachonici
pole_num = []
for j in range(int(velikost_sachovnice)):
    for i in range(int(velikost_sachovnice)):
        souradnice = str(j)+str(i)
        pole_num.append(int(souradnice))

print(pole_num)

# výpis prázdné šachovnice
projekt_2_2_knihovna_rek.vypis_sachovnice(sachovnice, velikost_sachovnice)

while True:
    #radek, sloupec = projekt_2_2_knihovna_rek.vstup_krizek(sachovnice)
    radek, sloupec = projekt_2_2_knihovna_rek.vstup(sachovnice, 'X', velikost_sachovnice, pole_num)
    sachovnice[int(radek)][int(sloupec)] = '.X.'
    projekt_2_2_knihovna_rek.vypis_sachovnice(sachovnice, velikost_sachovnice)
    projekt_2_2_knihovna_rek.kontrola_souseda(sachovnice, radek, sloupec, '.X.', pole_num)
    #radek, sloupec = projekt_2_2_knihovna_rek.vstup_kolecko(sachovnice)
    radek, sloupec = projekt_2_2_knihovna_rek.vstup(sachovnice, '0', velikost_sachovnice, pole_num)
    sachovnice[int(radek)][int(sloupec)] = '.O.'
    projekt_2_2_knihovna_rek.vypis_sachovnice(sachovnice, velikost_sachovnice)
    projekt_2_2_knihovna_rek.kontrola_souseda(sachovnice, radek, sloupec, '.O.', pole_num)


















