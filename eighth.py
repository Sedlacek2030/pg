
def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    
    binarni_cislo = str(binarni_cislo)
    return int(binarni_cislo, 2)


def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

if __name__ == "__main__":
    print(bin_to_dec("0")) == 0
    print (bin_to_dec(1)) == 1
    print (bin_to_dec("100")) == 4
    print (bin_to_dec(101)) == 5
    print (bin_to_dec("010101")) == 21
    print (bin_to_dec(10000000)) == 128