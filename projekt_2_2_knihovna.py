
# pomocná proměnná pro ohraničení indexů šachovnice
pole_num = [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31, 32, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 50, 51, 52, 53, 54, 55, 56, 57, 60, 61, 62, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 75, 76, 77]
sousedi = [-11, -10, -9, -1, 1, 9, 10, 11]
# sousedi_sousedu = [-22, -20, -18, -2, 2, 20, 22]

def vstup_krizek(sachovnicka):
    while True:
        print("Zadej pozici na šachovnici (hraje křížek):")
        radek = input("Zadej řádek (hodnota 0-7): ")
        sloupec = input("Zadej sloupec (hodnota 0-7): ")

        if (not (radek.isnumeric() and (int(radek) >= 0 and int(radek) <= 7))):
            print("Nezadali jste platný vstup - hodnota 0-7 - zkuste to znovu")
            continue

        if (not (sloupec.isnumeric() and (int(sloupec) >= 0 and int(sloupec) <= 7))):
            print("Nezadali jste platný vstup - hodnota 0-7 - zkuste to znovu")
            continue

        if (sachovnicka[int(radek)][int(sloupec)] == '.O.'):
            print("Tato pozice je obsazena soupeřem - zkuste to znovu")
            continue

        break
    return radek, sloupec

def vstup_kolecko(sachovnicka):
    while True:
        print("Zadej pozici na šachovnici (hraje kolečko):")
        radek = input("Zadej řádek (hodnota 0-7): ")
        sloupec = input("Zadej sloupec (hodnota 0-7): ")

        if (not (radek.isnumeric() and (int(radek) >= 0 and int(radek) <= 7))):
            print("Nezadali jste platný vstup - hodnota 0-7 - zkuste to znovu")
            continue

        if (not (sloupec.isnumeric() and (int(sloupec) >= 0 and int(sloupec) <= 7))):
            print("Nezadali jste platný vstup - hodnota 0-7 - zkuste to znovu")
            continue

        if (sachovnicka[int(radek)][int(sloupec)] == '.X.'):
            print("Tato pozice je obsazena soupeřem - zkuste to znovu")
            continue



        break
    return radek, sloupec

def vypis_sachovnice(vstup):
    i = 0
    while i < 8:
        print(vstup[i])
        i += 1


def kontrola_souseda(matice, r, s, znak):
    pozice = int(r+s)
    for i in sousedi:
        if((pozice + i) in pole_num):
            #print("je tam", pozice + i)
            souradnice_x = (pozice + i) // 10
            souradnice_y = (pozice + i) % 10
            #print("X a Y:", souradnice_x, souradnice_y)
            if(matice[souradnice_x][souradnice_y] == znak):
                #print("Znak:", znak, "má souseda vedle")
                if((pozice + 2*i) in pole_num):
                    souradnice_xx = (pozice + 2*i) // 10
                    souradnice_yy = (pozice + 2*i) % 10
                    #print("XX a YY:",souradnice_xx, souradnice_yy)
                    if (matice[souradnice_xx][souradnice_yy] == znak):
                        print("Znak:", znak, "vyhrál")
                        exit()

    return True

