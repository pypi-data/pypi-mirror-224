import sys
from pathlib import Path

sys.path.append((Path(__file__).parent / "src").as_posix())

from clean_confluent_kafka.application import KafkaBroker
from clean_confluent_kafka.tools import KafkaConfigsGenerator

# path = Path(__file__).parent / "kafka.yaml"

# conn = KafkaApplication(path)
# print(conn.get_topics_list())
# message = conn.consume()


# print(type(message.value()))

# print(conn.get_topics_list())

# print(KafkaConfigsGenerator("localhost:10808")
#       .add_producer(producer_topic="mytopic")
#       .add_consumer(consumer_topics="myconsumer")
#       .save("ali.yaml"))


#
# app = KafkaApplication()
#
# @app.consume()
# def consume(message):
#       print(message)
#
#
# @app.produce()
# def produce():
#       print(app.broker.get_topics_list())
#       return "hi"
#
#
# if __name__ == "__main__":
#       app()

from clean_confluent_kafka.utils import reverse_flatten_dict

# config = {'consumer.session.timeout.ms': 250000, 'consumer.message.max.bytes': 10000000, 'consumer.message.copy.max.bytes': 65535, 'consumer.receive.message.max.bytes': 200000000, 'consumer.max.in.flight': 1000000, 'consumer.max.in.flight.requests.per.connection': 1000000, 'consumer.max.poll.interval.ms': 500000, 'consumer.metadata.max.age.ms': 900000, 'consumer.topic.metadata.refresh.sparse': True, 'consumer.topic.metadata.refresh.interval.ms': 50, 'consumer.topic.metadata.refresh.fast.interval.ms': 250, 'consumer.topic.metadata.propagation.max.ms': 30000, 'consumer.broker.address.ttl': 1000, 'consumer.connections.max.idle.ms': 0, 'consumer.reconnect.backoff.ms': 100, 'consumer.reconnect.backoff.max.ms': 10000, 'consumer.statistics.interval.ms': 0, 'consumer.log_level': 6, 'consumer.log.queue': 0, 'consumer.log.thread.name': 1, 'consumer.log.connection.close': True, 'consumer.internal.termination.signal': 0, 'consumer.api.version.request': True, 'consumer.api.version.request.timeout.ms': 1000, 'consumer.api.version.fallback.ms': 0, 'consumer.broker.version.fallback': '0.10.0', 'consumer.security.protocol': 'plaintext', 'consumer.ssl.engine.id': 'dynamic', 'consumer.heartbeat.interval.ms': 80000, 'consumer.auto.offset.reset': 'earliest', 'consumer.enable.auto.commit': True, 'consumer.fetch.max.bytes': 100000000, 'consumer.fetch.message.max.bytes': 50, 'consumer.partition.assignment.strategy': 'range,roundrobin', 'producer.app.max_for_flush': 200, 'producer.message.max.bytes': 50000000, 'producer.batch.size': 5000000, 'producer.linger.ms': 5, 'producer.compression.type': 'snappy', 'producer.acks': 1, 'consumer.app.debug': True, 'consumer.topics': 'da-content-quality', 'consumer.group.id': 'a', 'consumer.bootstrap.servers': '172.17.0.141:9092', 'producer.topic': 'test-produce', 'producer.bootstrap.servers': '172.17.0.141:9092', 'app': None}

# print(reverse_flatten_dict(config))

broker = KafkaBroker(consumer_groups="a")

# print("broker")
# message = broker.consume()
# print(message.value())
