def nejvyssi_hodnota(seznam_cisel):

    return max(seznam_cisel)

def test_nejvyssi():
    assert nejvyssi_hodnota([1,2,3,4,5,6])
    assert nejvyssi_hodnota([6,5,4,3,2,1])