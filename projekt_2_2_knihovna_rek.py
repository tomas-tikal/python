import collections

# pomocná proměnná pro výběr sousedních indexů šachovnice diagonál
# sousedi = [-11, -9, 9, 11]
sousedi1 = [-11, 11]
sousedi2 = [-9, 9]


def vstup(sachovnicka, hrac, velikost):
    while True:
        print("Zadej pozici na šachovnici (hraje:", hrac, ")")
        radek = input("Zadej číslo řádku: ")
        sloupec = input("Zadej číslo sloupce: ")

        if (not (radek.isnumeric() and (int(radek) >= 0 and int(radek) <= int(velikost)))):
            print("Nezadali jste platný vstup - levé číslo v daném poli - zkuste to znovu")
            continue
        elif (not (sloupec.isnumeric() and (int(sloupec) >= 0 and int(sloupec) <= int(velikost)))):
            print("Nezadali jste platný vstup - pravé číslo v daném poli - zkuste to znovu")
            continue
        elif ((hrac == 'X') and (sachovnicka[int(radek)][int(sloupec)] == '.O.')):
            print("Tato pozice je obsazena soupeřem - zkuste to znovu")
            continue
        elif ((hrac == 'O') and  (sachovnicka[int(radek)][int(sloupec)] == '.X.')):
            print("Tato pozice je obsazena soupeřem - zkuste to znovu")
            continue
        break
    return radek, sloupec


def vypis_sachovnice(vstup, velikost):
    i = 0
    while i < int(velikost):
        print(vstup[i])
        i += 1


def kontrola_souseda(matice, r, s, znak, pole_num, pocet_rek, velikost_sachovnice):
    uhadnuto = []
    i = 0
    while i < int(pocet_rek):
        uhadnuto.append(znak)
        i += 1

    # kontrola_radku
    radek = matice[int(r)]
    str_list = ' '.join(map(str, radek))
    str_sublist = ' '.join(map(str, uhadnuto))
    if(str_sublist in str_list):
        print("Hráč:", znak, "vyhrál")
        exit()

    # kontrola_sloupce
    i = 0
    sloupec = []
    while i < int(velikost_sachovnice):
        sloupec.append(matice[i][int(s)])
        i += 1

    str_list = ' '.join(map(str, sloupec))
    str_sublist = ' '.join(map(str, uhadnuto))
    if(str_sublist in str_list):
        print("Hráč:", znak, "vyhrál")
        exit()


    # kontrola diagonál - klesající směr
    pozice = int(r+s)
    uroven = 1
    uhlopricka = []
    uhlopricka.append(znak)
    pred = True

    for i in sousedi1:
        while ((pozice + uroven * i) in pole_num):
            souradnice_x = (pozice + uroven * i) // 10
            souradnice_y = (pozice + uroven * i) % 10
            if(pred):
                uhlopricka.insert(0, matice[souradnice_x][souradnice_y])
            else:
                uhlopricka.append(matice[souradnice_x][souradnice_y])
            uroven += 1
        uroven = 1
        pred = False

    str_list = ' '.join(map(str, uhlopricka))
    str_sublist = ' '.join(map(str, uhadnuto))
    if(str_sublist in str_list):
        print("Hráč:", znak, "vyhrál")
        exit()


    # kontrola diagonál - stoupající směr
    pozice = int(r+s)
    uroven = 1
    uhlopricka = []
    uhlopricka.append(znak)
    pred = True

    for i in sousedi2:
        while ((pozice + uroven * i) in pole_num):
            souradnice_x = (pozice + uroven * i) // 10
            souradnice_y = (pozice + uroven * i) % 10
            if(pred):
                uhlopricka.insert(0, matice[souradnice_x][souradnice_y])
            else:
                uhlopricka.append(matice[souradnice_x][souradnice_y])
            uroven += 1
        uroven = 1
        pred = False

    str_list = ' '.join(map(str, uhlopricka))
    str_sublist = ' '.join(map(str, uhadnuto))
    if(str_sublist in str_list):
        print("Hráč:", znak, "vyhrál")
        exit()
