import sys
from pathlib import Path

sys.path.append((Path(__file__).parent / "src").as_posix())

from clean_confluent_kafka.application import KafkaApplication
from clean_confluent_kafka.tools import KafkaConfigsGenerator

path = Path(__file__).parent / "kafka.yaml"

conn = KafkaApplication(path)
# print(conn.get_topics_list())
# message = conn.consume()


# print(type(message.value()))

# print(conn.get_topics_list())

print(KafkaConfigsGenerator("localhost:10808")
      .add_producer(producer_topic="mytopic")
      .add_consumer(consumer_topics="myconsumer")
      .save("ali.yaml"))
