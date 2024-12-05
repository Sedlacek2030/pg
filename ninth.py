def dec_to_bin(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"
    if isinstance(cislo, str): #pokud je číslo string převede na int
        cislo = int(cislo)
    
    return bin(cislo)[2:] #bin převede číslo na binární(číslo bude začít 0b pro označení binarního čísla). [2:](slicer) odstraní první dva znaky


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"