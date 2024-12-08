from kafka import KafkaConsumer
from app.scraper import scrape_article
from app.db_handler import save_to_db

consumer = KafkaConsumer(
    'article_firehose',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

def consume_articles():
    for message in consumer:
        url = message.value.decode('utf-8')
        print(f"Processing article: {url}")
        article_data = scrape_article(url)
        if article_data:
            save_to_db(article_data)
