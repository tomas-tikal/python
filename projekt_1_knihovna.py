# definice funkce, ktera zjisti, zdali ve slovniku 'VSTUP' se nachazi hodnoty vlozene uzivatelem 'VZOREK'
def porovnej_slovnik(vstup, vzorek):
    for key, value in vzorek.items():
        if key not in vstup or vstup[key] != value:
            return False
    return True
