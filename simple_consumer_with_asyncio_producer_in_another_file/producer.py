import asyncio

from simple_consumer_with_asyncio_producer_in_another_file.producer_class import Producer


def main():
    producer = Producer()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(producer.producer())
    loop.stop()


if __name__ == '__main__':
    main()
