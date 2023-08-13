import logging
from typing import Any, Dict, List, Optional

from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient

from clean_confluent_kafka.config import KafkaConfigParser
from clean_confluent_kafka.utils import flatten_dict, serializers

logger = logging.getLogger(__name__)


class KafkaAction:
    def __init__(self, kafka_config, action, debug_mode: Optional[bool] = None):
        self.user_configs = kafka_config
        self.debug_mode = debug_mode if debug_mode is not None \
            else self.user_configs.app.get("debug", False)
        if self.debug_mode:
            logger.debug(self.user_configs.config)
        self.confluent = action(self.user_configs.config)


class KafkaAdmin:
    def __init__(self, data_servers: List[str] | Dict[str, Any] | str):
        if isinstance(data_servers, str):
            self.user_configs = {"bootstrap.servers": data_servers}
        elif isinstance(data_servers, list):
            self.user_configs = {"bootstrap.servers": ",".join(data_servers)}
        elif isinstance(data_servers, dict):
            self.user_configs = flatten_dict(data_servers)
        else:
            msg = "Invalid Configuration"
            raise ValueError(msg)

        self.confluent = AdminClient(self.user_configs)

    def get_topic(self):
        topics = self.confluent.list_topics().topics
        return topics


class KafkaConsumer(KafkaAction):
    def __init__(self, kafka_config_consumer, topics: Optional[str | List] = None,
                 consumer_group: Optional[str] = None, debug_mode: Optional[bool] = None):
        kafka_config_consumer["group.id"] = consumer_group
        super().__init__(kafka_config_consumer, Consumer, debug_mode)
        self.topics = topics if topics is not None else self.user_configs.topic
        self.confluent.subscribe(self.topics)

    def consume(self):
        while True:
            message = self.confluent.poll(timeout=1)
            if message is not None:
                break
        return message


class KafkaProducer(KafkaAction):
    DEFAULT_MAX_FOR_FLUSH: int = 100
    KEY_MAX_FOR_FLUSH: str = "max_for_flush"

    def __init__(self, kafka_config_producer, topic=None, debug_mode: Optional[bool] = None):
        super().__init__(kafka_config_producer, Producer, debug_mode)
        self.topic = topic if topic is not None else self.user_configs.topic
        self.serializer = serializers.json_serializer
        self._flush_counter = 0
        self._max_for_flush = self.user_configs.app.get(self.KEY_MAX_FOR_FLUSH,
                                                        self.DEFAULT_MAX_FOR_FLUSH)

    def produce(self, data, key=None, auto_flush: bool = True):
        self._flush_counter = 0
        try:
            self.confluent.produce(self.user_configs.topic, key=key, value=self.serializer(data))
            self.confluent.poll(0)
            self._flush_counter += 1
            if self._flush_counter >= self._max_for_flush:
                self.confluent.flush()
                self._flush_counter = 0
        except BufferError as bfer:
            logger.warning(
                "Error of full producer queue: %s",
                str(bfer))
            self.confluent.flush()
            self.confluent.produce(self.user_configs.topic, key=key, value=self.serializer(data))
        if auto_flush:
            self.confluent.flush()

    def set_max_for_flush(self, value: int):
        self._max_for_flush = value


class KafkaBroker:
    def __init__(self, config_path: str = "kafka.yaml", extra_configs: Optional[Dict[str, Any]] = None,
                 consumer_topics: Optional[str] = None, consumer_groups: Optional[str] = None,
                 producer_topic: Optional[str] = None):
        conf = KafkaConfigParser.from_path(config_path)
        if extra_configs is not None:
            conf.update_config(extra_configs)
        self.kafka_config = conf.parse()
        self.consumer = KafkaConsumer(self.kafka_config.consumer, topics=consumer_topics,
                                      consumer_group=consumer_groups)
        self.producer = KafkaProducer(self.kafka_config.producer, topic=producer_topic)
        self.admin = KafkaAdmin(self.kafka_config.producer.config["bootstrap.servers"])


def consume(self, *args, **kwargs):
    return self.consumer.consume(*args, **kwargs)


def produce(self, *args, **kwargs):
    return self.producer.produce(*args, **kwargs)


def get_topics(self):
    return self.admin.get_topic()


def get_topics_list(self):
    return list(self.admin.get_topic())
