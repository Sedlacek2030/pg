import json
import requests
url = "https://db.carnewschina.com/suggest?q="
data=[
    {"Jmeno": "Alice", "vek": 20},
    {"Jmeno":"Bob", "vek": 25},
    {"Jmeno":"Dave", "vek": 30},
    ]

def download_json_and_parse_brands(prefix):
    url_prefix = url+prefix
    response=requests.get(url)
    if response.status_code != 200:
        print("Chyba")
        return[]
    data = response.json()
    
    brands=[]
    for brand in data["brands"]:
        brands.append(brand["name"])

    return brands
if __name__ == "__main__":
    with open("data.json", "r") as fp:
        content = fp.read()
        print(content)