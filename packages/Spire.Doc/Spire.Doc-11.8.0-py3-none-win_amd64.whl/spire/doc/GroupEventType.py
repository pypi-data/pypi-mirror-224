from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class GroupEventType(Enum):
    """

    """
    GroupStart = 0
    GroupEnd = 1
    TableStart = 2
    TableEnd = 3

