from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class GridPitchType(Enum):
    """
    <summary>
        Defines how tall a grid unit is up/down
    </summary>
    """
    NoGrid = 0
    CharsAndLine = 1
    LinesOnly = 2
    SnapToChars = 3

