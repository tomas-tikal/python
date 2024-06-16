
# pomocná proměnná pro ohraničení indexů šachovnice
sousedi = [-11, -10, -9, -1, 1, 9, 10, 11]


def vstup(sachovnicka, hrac, velikost, pole_num):
    while True:
        print("Zadej pozici na šachovnici (hraje:", hrac, ")")
        radek = input("Zadej číslo řádku: ")
        sloupec = input("Zadej číslo sloupce: ")

        if (not (radek.isnumeric() and (int(radek) >= 0 and int(radek) <= int(velikost)))):
            print("Nezadali jste platný vstup - levé číslo v daném poli - zkuste to znovu")
            continue

        if (not (sloupec.isnumeric() and (int(sloupec) >= 0 and int(sloupec) <= int(velikost)))):
            print("Nezadali jste platný vstup - pravé číslo v daném poli - zkuste to znovu")
            continue

        if((hrac == 'X') and  (sachovnicka[int(radek)][int(sloupec)] == '.O.')):
            print("Tato pozice je obsazena soupeřem - zkuste to znovu")
            continue

        if((hrac == 'O') and  (sachovnicka[int(radek)][int(sloupec)] == '.X.')):
            print("Tato pozice je obsazena soupeřem - zkuste to znovu")
            continue

        break
    return radek, sloupec

def vypis_sachovnice(vstup, velikost):
    i = 0
    while i < int(velikost):
        print(vstup[i])
        i += 1


def kontrola_souseda(matice, r, s, znak, pole_num, pocet_rekurzi):
    pozice = int(r+s)
    spravna_pole = 1
    for i in sousedi:
        while (spravna_pole < int(pocet_rekurzi)):
            if((pozice + spravna_pole * i) in pole_num):
                #print("je tam", pozice + i)
                souradnice_x = (pozice + spravna_pole * i) // 10
                souradnice_y = (pozice + spravna_pole * i) % 10
                #print("X a Y:", souradnice_x, souradnice_y)
                if(matice[souradnice_x][souradnice_y] == znak):
                    spravna_pole += 1
                    continue
                else:
                    break
            else:
                break
        if(spravna_pole == int(pocet_rekurzi)):
            print("Hráč:", znak, "vyhrál")
            exit()

    return True

