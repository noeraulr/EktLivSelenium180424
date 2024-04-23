from pprint import pprint
def starting():
    start_urls = []
    for _ in range(1,4):
        start_url = f'https://www.elektra.mx/linea-blanca/refrigeradores-y-congeladores/refrigeradores?page={_}'
        start_urls.append(start_url)
    return start_urls

if __name__ == '__main__':
    pprint(starting())