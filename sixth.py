
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
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for a_tag in soup.find_all("a", href = True):
            hrefs.append(a_tag["href"])
        else:
            print(f"Chyba: Stavový kód {response.status_code}")

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        linx = download_url_and_get_all_hrefs(url)
        print("Nalezené odkazy:")
        for link in linx:
            print(link)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")