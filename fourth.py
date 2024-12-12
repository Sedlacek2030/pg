def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka["typ"]
    pozice = figurka["pozice"]
    
    #Ověření existence cílové pozice
    if not (1 <= cilova_pozice[0]<=8 and 1<=cilova_pozice[1]<=8):
       return False
    
    #Ověření volnosti pozice
    if cilova_pozice in obsazene_pozice:
        return False

    #Pohyb jednotlivých figur
    if typ == "pěšec":
        return tah_pesec(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "jezdec":
        return tah_jezdec(pozice, cilova_pozice,)
    elif typ == "věž":
        return tah_vez(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "střelec":
        return tah_strelec(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "dáma":
        return tah_dama(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "král":
        return tah_kral(pozice, cilova_pozice,)
    else:
        return False
    
    #Funkce tahu figur
def tah_pesec(pozice, cilova_pozice, obsazene_pozice):
    smer = 1 #Směr pohybu pěšce
    if pozice[1] == cilova_pozice[1]: #Stejný sloupec
        if cilova_pozice[0] == pozice[0]+smer and cilova_pozice not in obsazene_pozice:
            return True
        elif pozice[0] == 2 and cilova_pozice[0] == pozice[0]+2*smer and (pozice[1]) not in obsazene_pozice and cilova_pozice not in obsazene_pozice:
            return True
    return False
    
def tah_jezdec(pozice, cilova_pozice):
    radkovy_posun = abs(pozice[0] - cilova_pozice[0])
    sloupcovy_posun = abs(pozice[1] - cilova_pozice[1])
    return (radkovy_posun, sloupcovy_posun) in [(2,1), (1,2)]
    
def tah_vez(pozice, cilova_pozice, obsazene_pozice):
    if pozice[0] == cilova_pozice[0] or pozice[1] == cilova_pozice[1]:
        return cesta_volna(pozice, cilova_pozice, obsazene_pozice)
    return False
    
def tah_strelec(pozice, cilova_pozice, obsazene_pozice):
    radkovy_posun = abs(pozice[0] - cilova_pozice[0])
    sloupcovy_posun = abs(pozice[1] - cilova_pozice[1])
    if radkovy_posun == sloupcovy_posun:
        return cesta_volna(pozice, cilova_pozice, obsazene_pozice)
    return False
    
def tah_dama(pozice, cilova_pozice, obsazene_pozice):
    if tah_vez(pozice, cilova_pozice, obsazene_pozice) or tah_strelec(pozice, cilova_pozice, obsazene_pozice):
        return True
    return False    
    
def tah_kral(pozice, cilova_pozice):
        radkovy_posun = abs(pozice[0] - cilova_pozice[0])
        sloupcovy_posun = abs(pozice[1] - cilova_pozice[1])
        return max(radkovy_posun, sloupcovy_posun) == 1    
    
def cesta_volna(pozice, cilova_pozice, obsazena_pozice):
    radkovy_smer = (cilova_pozice[0]-pozice[0])// max(1, abs(cilova_pozice[0] - pozice[0]))
    sloupcovy_smer = (cilova_pozice[1] - pozice[1]) // max(1, abs(cilova_pozice[1] - pozice[1]))
    radek, sloupec = pozice[0] + radkovy_smer, pozice[1] + sloupcovy_smer
    while (radek, sloupec) != cilova_pozice:
        if (radek, sloupec) in obsazene_pozice:
            return False
        radek += radkovy_smer
        sloupec += sloupcovy_smer
    return True    

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku). V předchozích verzích tento řádek chyběl, tudíž neprocházely testy
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
    
    #Assited by ChatGPT