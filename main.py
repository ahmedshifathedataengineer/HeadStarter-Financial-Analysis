import threading
from app.kafka_producer import send_to_kafka
from app.kafka_consumer import consume_articles

# Example URLs for testing
example_urls = [
    "https://www.example.com/article1",
    "https://www.example.com/article2",
    "https://www.example.com/article3"
]

def producer_thread():
    for url in example_urls:
        send_to_kafka("article_firehose", url)

def consumer_thread():
    consume_articles()

if __name__ == "__main__":
    # Start producer and consumer threads
    threading.Thread(target=producer_thread).start()
    threading.Thread(target=consumer_thread).start()
