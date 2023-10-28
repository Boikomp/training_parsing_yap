import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'http://51.250.32.149/login/'

if __name__ == '__main__':
    session = requests.session()
    response = session.get(LOGIN_URL)
    soup = BeautifulSoup(response.text, features='lxml')
    scrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    data = {
        'username': 'test_parser_user',
        'password': 'testpassword',
        'csrfmiddlewaretoken': scrf_token,
    }

    response = session.post(LOGIN_URL, data=data)
    response.encoding = 'utf-8'
    print(response.status_code)
