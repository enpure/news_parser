from parser import get_news
from db import save_news


def main():
    news_items = get_news()
    if news_items:
        save_news(news_items)
        print(f"Сохранено {len(news_items)} новостей в базу данных")
    else:
        print("Не удалось получить новости")


if __name__ == '__main__':
    main()
