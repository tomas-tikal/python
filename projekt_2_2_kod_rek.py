
"""
projekt_2_2.py: druhý projekt do Engeto Online Python Akademie

author: Tomas TIKAL
email: tikal@3t.cz
discord: ti_to_80805
"""
import projekt_2_2_knihovna_rek

# naplnění prázdné tabulky 8x8 buněk
sachovnice= []
for j in range(8):
    sloupecek= []
    for i in range(8):
        retezec = str(j)+'.'+str(i)
        sloupecek.append(retezec)
    sachovnice.append(sloupecek)

# výpis prázdné šachovnice
projekt_2_2_knihovna_rek.vypis_sachovnice(sachovnice)

while True:
    #radek, sloupec = projekt_2_2_knihovna_rek.vstup_krizek(sachovnice)
    radek, sloupec = projekt_2_2_knihovna_rek.vstup(sachovnice, 'X')
    sachovnice[int(radek)][int(sloupec)] = '.X.'
    projekt_2_2_knihovna_rek.vypis_sachovnice(sachovnice)
    projekt_2_2_knihovna_rek.kontrola_souseda(sachovnice, radek, sloupec, '.X.')
    #radek, sloupec = projekt_2_2_knihovna_rek.vstup_kolecko(sachovnice)
    radek, sloupec = projekt_2_2_knihovna_rek.vstup(sachovnice, '0')
    sachovnice[int(radek)][int(sloupec)] = '.O.'
    projekt_2_2_knihovna_rek.vypis_sachovnice(sachovnice)
    projekt_2_2_knihovna_rek.kontrola_souseda(sachovnice, radek, sloupec, '.O.')


















