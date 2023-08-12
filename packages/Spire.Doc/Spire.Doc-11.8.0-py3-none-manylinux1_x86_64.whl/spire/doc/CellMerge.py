from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CellMerge(Enum):
    """
    <summary>
        Specifies the way of cell merging.
    </summary>
    """
    none = 0
    Start = 1
    Continue = 2

