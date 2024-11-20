
import sys
import requests
from bs4 import BeautifulSoup


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    response = requests.get(url)
    if response.status_code == 200: #status code 200 == úspěšná odpověď
        soup = BeautifulSoup(response.content, 'html.parser') #rozložení HTML obsahu na manší části, aby počítač "porozuměl" textu
        for a_tag in soup.find_all("a", href = True): #vyhledání všechodkazů <a href="..."> duh...
            hrefs.append(a_tag["href"]) #přidání odkazů do seznamu
        else:
            print(f"Chyba: Stavový kód {response.status_code}")

    return hrefs #vrátí seznam odkazů


if __name__ == "__main__": #chybí řádek pro zadání URL uživatelem (spuštění př. python sixth.py https://www.jcu.cz/cz/)
    try:
        url = sys.argv[1] #získání URL z argumentu příkazového řádku
        linx = download_url_and_get_all_hrefs(url) #funkce pro vypsání odkazů, obviously
        print("Nalezené odkazy:") #vypsaání nalezených odkazů
        for link in linx:
            print(link)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")

#All work done by ChatGPT, maybe