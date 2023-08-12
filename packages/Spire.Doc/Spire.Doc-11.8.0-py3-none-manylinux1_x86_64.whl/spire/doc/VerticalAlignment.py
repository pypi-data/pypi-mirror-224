from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class VerticalAlignment(Enum):
    """
    <summary>
        Specifies type of the vertical alignment.
    </summary>
    """
    Top = 0
    Middle = 1
    Bottom = 2

