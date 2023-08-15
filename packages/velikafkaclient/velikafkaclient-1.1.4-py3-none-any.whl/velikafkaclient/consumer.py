import json
import logging

from aiokafka import AIOKafkaConsumer
from confluent_kafka import Consumer, KafkaError, KafkaException

from .eventregistration import kafka_topic_events
from .exceptions import InvalidEventTopicException, InvalidEventStructure
from .killer import KafkaClientGracefulKiller


class AsyncKafkaConsumer:

    def __init__(self, bootstrap_servers, group_id=None):
        self.kafka_topic_events = kafka_topic_events
        self.client = None
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.subscriptions = dict()
        self.topics = set()
        self.killer = KafkaClientGracefulKiller(self)

    async def start(self):
        if self.client is not None:
            raise Exception("Consumer already started, stop before starting again <3")
        self.client = AIOKafkaConsumer(
            *list(self.topics),
            bootstrap_servers=self.bootstrap_servers,
            group_id=self.group_id
        )
        await self.client.start()

    async def stop(self):
        if self.client is None:
            raise Exception("Consumer is not started, start before stopping <3")
        await self.client.stop()
        self.client = None

    def subscribe(self, topic, handler):
        self.subscriptions[topic.value] = handler
        self.topics.add(topic.value)

    async def consume(self):
        async for msg in self.client:
            print("consumed: ", msg.topic, msg.partition, msg.offset, msg.value)
            if msg.topic not in self.kafka_topic_events.topic_event_models:
                raise InvalidEventTopicException(f"Topic {msg.topic} not found")
            topic_event_model = self.kafka_topic_events.topic_event_models[msg.topic]
            try:
                decoded_msg = msg.value.decode('utf-8')
                data = json.loads(decoded_msg)
                msg_event = topic_event_model(**data)
                handler = await self.subscriptions[msg.topic](msg_event)
                print(handler)
            except Exception as e:
                # TODO add proper exception handling
                raise InvalidEventStructure(f"Invalid event structure {str(msg.value)} for topic {msg.topic}")


class KafkaConsumer:

    def __init__(self, bootstrap_servers, group_id=None, auto_commit=True):
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.subscriptions = dict()
        self.auto_commit = auto_commit
        conf = {'bootstrap.servers': bootstrap_servers,
                'group.id': group_id,
                'auto.offset.reset': 'earliest',
                'enable.auto.commit': auto_commit,
                }
        self.client = Consumer(conf)

    def start(self):
        self.client.subscribe(list(self.subscriptions.keys()))
        try:
            while True:
                msg = self.client.poll(timeout=1.0)
                if msg is None:
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        logging.info('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    topic = msg.topic()
                    try:
                        self.subscriptions[topic](msg)
                        if not self.auto_commit:
                            self.client.commit()
                    except Exception as e:
                        # TODO implement
                        raise e

        finally:
            self.client.close()

    def stop(self):
        self.client.close()

    def subscribe(self, topic, handler):
        self.subscriptions[topic] = handler
