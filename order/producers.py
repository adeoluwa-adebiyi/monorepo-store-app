from kafka import KafkaProducer
from django.conf import settings
import multiprocessing
from redis import Redis


TOPIC_ID = getattr(settings, "KAFKA_TOPIC_ID", "5myef1xu-messages")

SERVERS = getattr(
    settings, 
    "KAFKA_SERVERS", 
    "rocket-01.srvs.cloudkafka.com:9094,rocket-02.srvs.cloudkafka.com:9094,rocket-03.srvs.cloudkafka.com:9094"
    ).split(",")

print(SERVERS)

producer: KafkaProducer = KafkaProducer(
        bootstrap_servers=[
            *SERVERS
        ], 
        security_protocol="SASL_PLAINTEXT",
        sasl_mechanism="PLAIN",
        sasl_plain_username="5myef1xu",
        sasl_plain_password="p9XeeG6glskK4uuN3zWhwInjXHSPhrsE",
        api_version=(2,5,0),
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

redis: Redis = Redis(
    host="redis-18735.c44.us-east-1-2.ec2.cloud.redislabs.com", 
    port=18735,
    password="VBvc6yBGT0T2GAwn64aZLkh4ioNS8Z8v"
)

pubsub  = redis.pubsub()
