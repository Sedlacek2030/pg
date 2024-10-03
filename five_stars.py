
def stars_while():
    print("Start")
    i = 0

    while i<5:
        print("*")
        i += 1
    print("konec")

def stars_for():
    print("Start")

    for i in [0,1,2,3,4]: #for i in range(5)
        print("*")
        print("*", i)
    print("konec")
stars_while()
stars_for()

def in_range(min_number, max_number, number):

    if number >= min_number and number <= max_number:
        print("Number in range")
    else :
        print ("Number not in range")

in_range(100, 1000, 1)

#funkce vrátí string "Ahoj *jmeno*"
def pozdrav_jmeno(jmeno):

    print("Ahoj "+jm+"!")
jm = input("Zadej jméno: ")

pozdrav_jmeno(jm)