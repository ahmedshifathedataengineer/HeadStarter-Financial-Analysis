from unittest.mock import AsyncMock
import asyncio

# Mock Kafka Producer
class MockKafkaProducer:
    async def start(self):
        print("Mock KafkaProducer started")

    async def send_and_wait(self, topic, message):
        print(f"Mock message sent to topic {topic}: {message.decode()}")

    async def stop(self):
        print("Mock KafkaProducer stopped")

# Mock Kafka Consumer (Optional)
class MockKafkaConsumer:
    async def start(self):
        print("Mock KafkaConsumer started")

    async def stop(self):
        print("Mock KafkaConsumer stopped")

    async def __aiter__(self):
        yield AsyncMock(value=b"Mock consumed message")

async def produce():
    producer = MockKafkaProducer()
    await producer.start()
    try:
        await producer.send_and_wait("test-topic", b"Hello, Kafka!")
    finally:
        await producer.stop()

async def consume():
    consumer = MockKafkaConsumer()
    await consumer.start()
    try:
        async for msg in consumer:
            print(f"Consumed: {msg.value.decode()}")
    finally:
        await consumer.stop()

# Run both produce and consume
asyncio.run(produce())
asyncio.run(consume())
