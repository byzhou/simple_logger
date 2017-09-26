import logging
logger  = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger_handler = logging.StreamHandler()
logger_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s [%(lineno)d]: %(funcName)s(): %(message)s'))
logger.addHandler(logger_handler)

def test():
    logger.info('424242424')
test()
