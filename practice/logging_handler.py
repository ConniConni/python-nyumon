import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


h = logging.FileHandler('133_test.log')
logger.addHandler(h)

def do_something():
    logging.info('from test info')
    logger.info('from test')
    logger.debug('from test debug')
