# Transformation function
import asyncio
from mock_kafka_test import MockKafkaConsumer, MockKafkaProducer


def process_message(message):
    return f"Processed: {message}"

async def produce():
    producer = MockKafkaProducer()
    await producer.start()
    try:
        transformed_message = process_message("Hello, Kafka!")
        await producer.send_and_wait("test-topic", transformed_message.encode())
    finally:
        await producer.stop()

async def consume():
    consumer = MockKafkaConsumer()
    await consumer.start()
    try:
        async for msg in consumer:
            print(f"Consumed and processed: {msg.value.decode()}")
    finally:
        await consumer.stop()

asyncio.run(produce())
asyncio.run(consume())
