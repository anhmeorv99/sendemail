import settings
from celery.schedules import crontab
broker_conf = settings.BROKER

broker_url = broker_conf['URL']
include = ['workers.tasks']
task_default_delivery_mode = 'transient'


task_routes = {
    'workers.tasks.send_email': {'queue': broker_conf['SEND_EMAIL_QUEUE']},
}

beat_schedule = {
    # tuấn anh thêm send mail
    'run-send-mail-every-{}-seconds'.format(broker_conf['TIME_SEND_EMAIL']): {
        'task': 'workers.tasks.send_email',
        'schedule': broker_conf['TIME_SEND_EMAIL']
    }
}

