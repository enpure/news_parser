import requests
from bs4 import BeautifulSoup

def get_news():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все элементы с классом 'athing' (они содержат каждую новость)
        stories = soup.find_all('tr', class_='athing')
        news_items = []

        for story in stories:
            # Находим заголовок и ссылку
            title_tag = story.find('span', class_='titleline').find('a')
            if title_tag:
                title = title_tag.get_text()
                link = title_tag['href']

                # Находим количество очков (рейтинг) для новости
                score_tag = story.find_next_sibling('tr').find('span', class_='score')
                score = score_tag.get_text().replace(' points', '') if score_tag else '0'

                # Добавляем данные в список
                news_items.append({
                    'title': title,
                    'link': link,
                    'score': score
                })

        return news_items
    else:
        print(f"Ошибка при получении данных: {response.status_code}")
        return []

# Тестируем парсер
if __name__ == '__main__':
    news = get_news()
    for item in news:
        print(item)
