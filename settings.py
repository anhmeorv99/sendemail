import os
###########################################################
# BROKER CONFIGURATION
###########################################################
BROKER = {
    'URL': 'amqp://{}:{}@{}:{}//'.format(
        os.environ.get('BROKER_USER', 'rabbitmq'),
        os.environ.get('BROKER_PASS', 'rabbitmq'),
        os.environ.get('BROKER_HOST', 'localhost'),
        os.environ.get('BROKER_PORT', 5672)
    ),
    'TIME_SEND_EMAIL': float(os.environ.get('TIME_SEND_EMAIL', 30)),
#send mail
    'SEND_EMAIL_QUEUE': os.environ.get("BROKER_SEND_MAIL_QUEUE", "send_email"),
}

###########################################################
# ELASTICSEARCH CONFIGURATION
###########################################################
es_hosts_txt = os.environ.get("ELASTIC_HOST", "localhost")
es_hosts = [item.strip() for item in es_hosts_txt.split(",")]

ELASTICSEARCH = {
    "HOST": es_hosts,
    "PORT": os.environ.get("ELASTIC_PORT", "9200"),
    'MAX_CONN_SIZE': int(os.environ.get("ELASTIC_MAX_CONN_SIZE", 25)),
    'SCHEME': os.environ.get("ELASTIC_SCHEME", "http"),
    "YOUTUBE_VIDEO_INDEX": os.environ.get("ELASTIC_YOUTUBE_VIDEO_INDEX", "youtube_video_2020_10")
}
