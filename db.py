import mysql.connector


def connector_to_db():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ops123',
        database='news_parser'
    )
    return connection


def save_news(news_items):
    connection = connector_to_db()
    cursor = connection.cursor()

    for item in news_items:
        cursor.execute("""
        INSERT INTO news (title, link, score)
        VALUES (%s, %s, %s)
        """, (item['title'], item['link'], item['score']))

    connection.commit()
    cursor.close()
    connection.close()