#!/usr/bin/env python

from addressbook import AddressBook
from person import Person


__version__ = "1.0.0"


# Set default logging handler to avoid "No handler found" warnings.
import logging
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(logging.NullHandler())


#numeric_level = getattr(logging, loglevel.upper(), None)
#if not isinstance(numeric_level, int):
#    raise ValueError('Invalid log level: %s' % loglevel)


#CRITICAL    50
#ERROR   40
#WARNING     30
#INFO    20
#DEBUG   10
#NOTSET  0


#Handler.createLock()
#Initializes a thread lock which can be used to serialize access to underlying I/O functionality which may not be threadsafe.

#Handler.acquire()
#Acquires the thread lock created with createLock().


# APPLICATION
#logName = "log"
#level = logging.DEBUG
#
##logging.config.fileConfig('logging.conf')
#logging.basicConfig(
#    filename=logName,
#    filemode='a',
#    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#    datefmt='%H:%M:%S',
#    level=level)
#
#
#handler = logging.StreamHandler()
#formatter = logging.Formatter(
#        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
#handler.setFormatter(formatter)
#logger.addHandler(handler)
#logger.setLevel(logging.DEBUG)
#
#logger.critical('This is a critical message.')
#logger.error('This is an error message.')
#logger.warning('This is a warning message.')
#logger.info('This is an informative message.')
#logger.debug('This is a low-level debug message.')
#

