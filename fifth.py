
import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    """
    Tato funkce načte binární soubor z cesty file_name,
    z něj přečte prvních header_length bytů a ty vrátí pomocí return
    """
    try:
        with open(file_name, 'rb') as f:
            return f.read(header_length)
    except FileNotFoundError:
        print(f"Soubor nenalezen")
        return None
    except Exception as e:
        print(f"Došlo k chybě: {e}")
        return None


def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné jpeg_header
    """
    # načti hlavičku souboru
    header = read_header(file_name, len(jpeg_header))
    if header == jpeg_header:
        return True
    else:
        return False

    # vyhodnoť zda je soubor jpeg


def is_gif(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanými hlavičkami v proměnných gif_header1 a gif_header2
    """
    # vyhodnoť zda je soubor gif
    header1 = read_header(file_name, len(gif_header1))
    header2 = read_header(file_name, len(gif_header2))
    if header1 == gif_header1 or header2 == gif_header2:
        return True
    else:
        return False
    


def is_png(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné png_header
    """
    # vyhodnoť zda je soubor png
    header = read_header(file_name, len(png_header))
    if header == png_header:
        return True
    else:
        return False


def print_file_type(file_name):
    """
    Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    # přidej try-except blok, odchyť obecnou vyjímku Exception a vypiš ji
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except IndexError:
        print("Nebyl zadát název souboru.")
    except Exception as e:
        print(f"Došlo k neočekávané chybě: {e}")

#Assitance provided via ChatGPT