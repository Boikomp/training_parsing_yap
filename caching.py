import requests_cache

# Сохранение адреса веб-страницы в константу. Это удобно, потому
# что при написании парсера, к адресу нужно постоянно обращаться.
MAIN_DOC_URL = 'https://docs.python.org/3/'

if __name__ == '__main__':
    # Сессия, кеширующая результаты загрузки страниц.
    session = requests_cache.CachedSession()
    # Очистка кеша.
    # session.cache.clear()
    # Загрузка веб-страницы при помощи HTTP-метода get().
    response = session.get(MAIN_DOC_URL)
    # Печать списка закешированных веб-страниц.
    print(session.cache.urls())
