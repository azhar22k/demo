import logging
from os import getenv

logging.basicConfig(level=getenv('LEVEL', 'WARNING'))

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')

with open(getenv('FILE', 'out.txt'), 'w') as f:
    f.write('hello')
