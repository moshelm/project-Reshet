from confluent_kafka import Producer, Consumer, s
import json 
import os 

def json_serializer(data: dict|list|str):
    return json.dumps(data).encode("utf-8")

def json_deserializer(data:dict|list|str):
    if data is None:
        return None
    return json.loads(data.decode("utf-8"))

class KafkaConfig():
    def __init__(self):
        kafka_host = os.getenv("KAFKA_HOST","localhost")
        kafka_port = os.getenv("KAFKA_PORT","9092")
        self.base_config = {"bootstrap.servers":f"{kafka_host}:{kafka_port}"}

class KafkaProducerConfig(KafkaConfig):
    def __init__(self):
        super().__init__()
        self.base_config["retries"] = 5
        self.base_config["value.serializer"] = json_serializer

class KafkaConsumerConfig(KafkaConfig):
    def __init__(self):
        super().__init__()
        self.base_config["value.serializer"] = json_deserializer
        self.base_config["group.id"] = os.getenv("KAFKA_GROUP_ID","dddd")
        self.base_config["auto.offset.reset"] = 'earliest'
        self.base_config["value.serializer"] = json_deserializer
