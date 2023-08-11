""" simple-licence-plugin: plugin for pyarmor for checking and auditing licenses """

from .models import AuditEventBase
from .utils import check_licence, get_licence_data

__author__ = "Alex Hunt"
__email__ = "alex.hunt@csiro.au"
__version__ = "1.0.1"
