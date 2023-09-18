from bs4 import BeautifulSoup

html_doc = """
<html>
  <head><title>Сказка о трёх богатырях</title></head>
  <body>
    <p class="title"><b>Сказка о трёх богатырях</b></p>

    <p class="story">
      Давным-давно жили-были три богатыря:
      <a href="http://example.com/ilya" class="hero" id="link1">Илья Муромец</a>,
      <a href="http://example.com/alesha" class="hero" id="link2">Алёша Попович</a> и
      <a href="http://example.com/dobrynya" class="hero" id="link3">Добрыня Никитич</a>.
    </p>

    <p class="story">
      И был у них один противник
      <a href="http://example.com/dragon" class="antihero" id="link4">Змей Горыныч</a>.
    </p>

    <p class="story" name="end">
      Вот и сказке конец, а кто слушал — молодец!
    </p>
  </body>
</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')

# Поиск в коде всех тегов <b>.
# result = soup.find_all('b')

# Поиск в коде всех тегов <title> и <b>.
# result = soup.find_all(['title', 'b'])

# Поиск в коде всех элементов с классом 'title'.
# result = soup.find_all(attrs={'class': 'title'})

# Поиск в коде всех элементов <a class='hero'>.
# result = soup.find_all('a', attrs={'class': 'hero'})

# Поиск в коде всех элементов id='link2'.
# result = soup.find_all(id='link2')

# Поиск в коде всех элементов class_='antihero'.
# result = soup.find_all(class_='antihero')

# # Поиск в HTML-коде всех тегов <p class='story'>. Найдётся три элемента.
# all_stories = soup.find_all('p', class_='story')
# # Берётся только первый тег с индексом 0.
# first_story = all_stories[0]
# # Поиск внутри найденного тега id='link2'.
# link2 = first_story.find_all(id='link2')

# Поиск в коде первого элемента <a class="hero">
# result = soup.find('a', attrs={'class': 'hero'})

first_story = soup.find('p', class_='story')
link2 = first_story.find(id='link2')

# Обращение к тексту тега.
print(link2.text)
# Обращение к атрибуту тега, в котором содержится ссылка.
print(link2['href'])
