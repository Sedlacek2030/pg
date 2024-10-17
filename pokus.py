import sys

def main(soubor):
    otevreny_soubor = open (soubor, "r" )
    for radka in otevreny_soubor:
        parametry = radka.split(",")
        vek = int(parametry[2])