# Příklad 3: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `convert_to_czk`, která:
# 1. Přijme částku (`amount`) jako desetinné číslo a kód měny (`currency`) jako řetězec (např. "USD", "EUR").
# 2. Stáhne aktuální kurzovní lístek z URL:
#    http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
# 3. Načte příslušný kurz podle zadaného kódu měny a provede převod zadané částky na české koruny (CZK).
# 4. Funkce vrátí výslednou částku v CZK zaokrouhlenou na dvě desetinná místa.
# Pokud zadaná měna v kurzovním lístku neexistuje, vyhoďte výjimku `ValueError`.

import requests

def convert_to_czk(amount, currency):
    # Stáhnout aktuální kurzovní lístek
    response = requests.get("http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt")
    
    if response.status_code != 200:     #Kontrola úspěšného připojení
        raise Exception("Nelze se připojit k serveru")
    
    lines = response.text.splitlines() # Rozdělí text na řádky       
        
    for i in range(len(lines)):      #Najde index pro začátek dat (první řádek s kurzy)                   
        if "země|měna|množství|kód|kurz" in lines[i]:
            header_index = i + 1
            break
        
        rates = {}          # Načteme kurzy do slovníku       
        for line in lines[header_index:]:
            parts = line.split("|") #Rozdělení řádku na části
            if len(parts) == 5:
                code = parts[3].strip()
                rate_str = parts[4].replace(",", ".").strip()  # Nahradí čárky tečkou pro float konverzi
                try:        #kontrola chyb
                    rate = float(rate_str)
                    rates[code] = rate
                except ValueError:
                    continue

        # Zkontrolujeme zda máme přítomnou měnu a provedeme konverzi
        if currency not in rates:
            raise ValueError(f"Měna {currency} nebyla nalezena.")
        
        czk_amount = amount * rates[currency]
        
        return round(czk_amount, 2) #zaokrouhlení na 2 desetinná místa

# Pytest testy pro Příklad 3 
from unittest.mock import patch, MagicMock

# Pytest testy pro Příklad 3
from unittest.mock import patch, MagicMock

def test_convert_to_czk():
    mock_response = """31.10.2025 #237
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|14,894
EMU|euro|1|EUR|25,480
USA|dolar|1|USD|23,000
Velká Británie|libra|1|GBP|29,745
"""
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, text=mock_response)

        assert convert_to_czk(100, "USD") == 2300.00
        assert convert_to_czk(50, "EUR") == 1274.00
        assert convert_to_czk(200, "AUD") == 2978.80
        
        try:
            convert_to_czk(100, "XYZ")
        except ValueError as e:
            assert str(e) == "Currency XYZ not found in the exchange rate list."