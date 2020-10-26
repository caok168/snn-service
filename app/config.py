import os
import os.path

env = os.environ.get

CELERY_NAME = env('CELERY_NAME', "celery")
CELERY_BROKER_URL = env('CELERY_BROKER_URL', "redis://127.0.0.1:6380/0")
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', "redis://127.0.0.1:6380/0")
CELERYD_PREFETCH_MULTIPLIER = int(env('CELERYD_PREFETCH_MULTIPLIER', 1))
CELERYD_CONCURRENCY = int(env('CELERYD_CONCURRENCY', 1))

DETECT_API_URL = env('DETECT_API_URL', "http://192.168.11.17:9090/api/v1/detect/ct-detect-save")
# DETECT_API_URL = env('DETECT_API_URL', "http://192.168.12.213:9090/api/v1/detect/ct-detect-save")

RESULT_DATA = env('RESULT_DATA', "/home/lynxi/snn/DataLuna/results")
CASE_DATA = env('CASE_DATA', "/home/lynxi/snn/DataLuna")
TASK_TIMEOUT = int(env('TASK_TIMEOUT', 3600))

TASK_CASE_FILEPATH = env('TASK_CASE_FILEPATH', "./app/data/task_case.json")


class BaseConfig:
    """基础配置"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = env('DATABASE_URL', "postgresql://admin:admin123456@127.0.0.1:5432/manager")


class TestingConfig(BaseConfig):
    """测试环境配置"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = env('DATABASE_TEST_URL', "postgresql://admin:admin123456@127.0.0.1:5432/manager")


class ProductionConfig(BaseConfig):
    """生产环境配置"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = env('DATABASE_URL', "postgresql://admin:admin123456@127.0.0.1:5432/manager")