from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListType(Enum):
    """
    <summary>
        Specifies type of the list format.
    </summary>
    """
    Numbered = 0
    Bulleted = 1
    NoList = 2

