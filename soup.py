from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    # simple_html = '<html><body><p>Это самый простой HTML!</p></body></html>'
    # soup = BeautifulSoup(simple_html, features='lxml')

    response = requests.get('https://docs.python.org/4/')
    soup = BeautifulSoup(response.text, features='lxml')
    # Печать содержимого только тега <body>.
    print(soup.html.body.prettify())
