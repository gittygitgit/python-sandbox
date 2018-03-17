#!/usr/bin/python

import logging
logging.basicConfig(filename='foo.txt', level=logging.DEBUG)
logging.debug('Logging to logfile')
logging.info('Logging info')
logging.warn('warning')

