from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CellWidthType(Enum):
    """
    <summary>
        Specifies preferred width type
    </summary>
    """
    Auto = 1
    Percentage = 2
    Point = 3

