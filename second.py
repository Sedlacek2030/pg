from num2words import num2words

def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    number = int(cislo)
    if 0 <= number <= 100:
        #Překlad do češtiny
        return num2words(number, lang='cz')
    else:
        return "Guess again"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)