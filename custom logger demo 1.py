import logging
logger=logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)
consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(msg)s',datefmt=('%d/%m/%Y %I:%M:%S %p'))
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)
logger.critical('this is critical message')
logger.error('this is error message')
logger.warning('this is warning message')
logger.info('this is info message')
logger.debug('this is debug message')
