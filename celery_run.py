
from app.celery_task.celery_app import celery

if __name__ == '__main__':
    celery.worker_main()
