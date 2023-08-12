from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FrameHorzAnchor(Enum):
    """
    <summary>
        Specifies the horizontal frame anchor.
    </summary>
    """
    Column = 0
    Margin = 1
    Page = 2

