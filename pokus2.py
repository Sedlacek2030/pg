# funkce vrati treti prvek ze seznamu pokud ma mene nez 3 prvky, vrati None
def vrat_treti(seznam):
    if len(seznam) < 3:
        return None
    else:
        return seznam[2]

# funkce spocita prumer z hodnot v seznamu
def udelej_prumer(seznam):
    return sum(seznam)/len(seznam)

# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
    jmeno = slovnik["jmeno"]
    prijmeni = slovnik["prijmeni"]
    vek = slovnik["vek"]
    prumer = slovnik["prumer"]
    return f"Jmeno:{jmeno}, Příjmení:{prijmeni}, Věk: {vek}, Průměr:{prumer}"


if __name__ == "__main__":
    
    obalka = [9,8,7,6,5]
    vysledek = udelej_prumer(obalka)
    print (vysledek)
    
    print(vrat_treti([9,8,7,6,5]))      #vrať 7
    print(udelej_prumer([9,8,7,6,5]))   
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    vysledek = naformatuj_text(student)
    print(vysledek)

    student["vek"]
    student["prijmeni"]
    student["jmeno"]
    student["znamky"]