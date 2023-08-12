from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PageBorderOffsetFrom(Enum):
    """
    <summary>
        Specifies the position of page border.
    </summary>
    """
    Text = 0
    PageEdge = 1

