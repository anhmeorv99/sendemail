from celery import Celery
from celery.signals import setup_logging
from log import LOGGING

app = Celery(
    'mail_sender',
)


@setup_logging.connect
def config_loggers(*args, **kwags):
    from logging.config import dictConfig
    dictConfig(LOGGING)


app.config_from_object('workers.celeryconfig')

if __name__ == '__main__':
    app.start()
