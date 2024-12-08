from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_to_kafka(topic, message):
    try:
        producer.send(topic, message.encode('utf-8'))
        print(f"Sent to Kafka: {message}")
    except Exception as e:
        print(f"Error sending message to Kafka: {e}")

# Test sending a URL
send_to_kafka("article_firehose", "https://www.example.com/article")
