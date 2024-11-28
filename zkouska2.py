
def operace(typ, a, b):
    matematicka_operace = None
    if typ == "+":
       matematicka_operace = a+b
    elif typ == "-":
        matematicka_operace = a-b
    elif typ == "*":
        matematicka_operace = a*b
    elif typ == "/":
        try:
            matematicka_operace = a/b
        except ZeroDivisionError:
            print("Error")
            return None
    return matematicka_operace

if __name__ == "__main__":
    operace("+", 1 ,2)
    operace("-", 2 ,1)
    operace("*", 0 ,5)
    operace("/", 4 ,2)