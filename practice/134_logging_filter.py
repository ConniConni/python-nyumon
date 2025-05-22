import logging

logging.basicConfig(level=logging.INFO)

class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


# logger定義
logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
# 'from info'表示
logger.info('from info')
# 'from main password = "test"'表示
logger.info('from main password = "test"')