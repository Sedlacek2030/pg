# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `process_strings`, která přijme seznam řetězců. 
# Funkce vrátí nový seznam, který obsahuje pouze řetězce delší než 3 znaky, převedené na velká písmena.
# Pokud seznam obsahuje řetězec "STOP", ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_strings(strings):
    výsledek = []
    for string in strings:  #pro každý string zkontroluje jestli není "STOP", jinak kontroluje délku stringu (pokud projde vrátí UPPERCASE verzi)
        if string == "STOP":
            break           #přerušení for loopu
        if len(string) >3:
            výsledek.append(string.upper()) #append != add (add nepřidává na konec a nedovoluje duplikáty) seznam/set
    return výsledek

# Pytest testy pro Příklad 2
def test_process_strings():
    assert process_strings(["abc", "abcd", "STOP", "efgh"]) == ["ABCD"]
    assert process_strings(["hello", "world", "STOP", "python"]) == ["HELLO", "WORLD"]
    assert process_strings(["hi", "ok", "go"]) == []
    assert process_strings(["code", "test", "debug"]) == ["CODE", "TEST", "DEBUG"]
