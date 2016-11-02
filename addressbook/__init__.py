#!/usr/bin/env python

"""
    Init script for addressbook API.
"""

import logging
from .addressbook import AddressBook
from .person import Person

__all__ = ["AddressBook", "Person"]
__author__ = "Luigi Riefolo"
__version__ = "1.0.0"


try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        """
        Set default logging handler.

        It avoids "No handler found" warnings.
        """
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(logging.NullHandler())
