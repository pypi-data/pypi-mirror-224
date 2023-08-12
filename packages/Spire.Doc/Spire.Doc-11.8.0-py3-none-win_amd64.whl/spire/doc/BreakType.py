from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BreakType(Enum):
    """
    <summary>
        Document's break type.
    </summary>
    """
    PageBreak = 0
    ColumnBreak = 1
    LineBreak = 2

