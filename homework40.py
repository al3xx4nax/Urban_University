import requests
from bs4 import BeautifulSoup as BS

page = 0
count = 0
print('\tТоп 1000 лучших фильмов с сайта "КиноАфиша":\n'
      '\t--------------------------------------------')
while True:
    r = requests.get('https://www.kinoafisha.info/rating/movies/?page=' + str(page))
    html = BS(r.content, 'html.parser')
    items = html.select(".ratings_list > .movieList_item")

    if len(items) and page <= 9:
        for el in items:
            title = el.select('.movieItem_info > .movieItem_title')
            genre = el.find('span', class_='movieItem_genres').text
            country = el.find('span', class_='movieItem_year').text
            rating = el.find('span', class_='movieItem_itemRating').text
            count += 1
            print(f'{count} место:\b\n'
                  f'Название: {title[0].text}\n'
                  f'Жанр: {genre}\n'
                  f'Год выхода, страна производства: {country}\n'
                  f'Рейтинг: {rating}\n')
        page += 1
    else:
        break
