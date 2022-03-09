import logging
import logging.config

# create logger
logger = logging.getLogger('serverLogger')
logger.setLevel(logging.DEBUG)

# Create Handlers
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create file handler
fh = logging.FileHandler('httpPYTHON/logSever.log')
fh.setLevel(logging.ERROR)


# create Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')