import logging
import types
import sys


LOGGER_NAME = 'snn-api'


def init_logger_handler():
    logger_ = logging.getLogger(LOGGER_NAME)  # type: logging.Logger
    logger_.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger_.addHandler(handler)
    return logger_


def log_response_error(self, resp):
    if sys.exc_info() != (None, None, None):
        self.exception('request failed')

    if resp is None:
        self.error('request hasn\'t been sent out')
    else:
        try:
            self.error(resp.json())
        except Exception:
            try:
                self.error(resp.text)
            except Exception:
                self.error('unknown resp content (status code {code})'.format(code=resp.status_code))


logger = init_logger_handler()
logger.log_response_error = types.MethodType(log_response_error, logger)
