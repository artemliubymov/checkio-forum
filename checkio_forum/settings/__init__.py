# flake8: noqa
from .django import *
from .django_custom import *
from .social import *
from .checkio import *

try:
    from .local import *
except ImportError:
    pass
