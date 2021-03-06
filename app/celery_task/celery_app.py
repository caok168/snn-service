from celery import Celery

from app.config import CELERY_NAME, CELERY_BROKER_URL, CELERY_RESULT_BACKEND, CELERYD_PREFETCH_MULTIPLIER, \
    CELERYD_CONCURRENCY

celery = Celery(CELERY_NAME, broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

config = {
    'CELERY_BROKER_URL': CELERY_BROKER_URL,
    'CELERY_RESULT_BACKEND': CELERY_RESULT_BACKEND,
    'CELERYD_PREFETCH_MULTIPLIER': CELERYD_PREFETCH_MULTIPLIER,
    'CELERYD_CONCURRENCY': CELERYD_CONCURRENCY,
}

celery.conf.update(config)

