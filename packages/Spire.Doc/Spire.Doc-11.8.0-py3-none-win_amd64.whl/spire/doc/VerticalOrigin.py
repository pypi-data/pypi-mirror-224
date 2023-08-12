from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class VerticalOrigin(Enum):
    """
    <summary>
        Specify vertical origin of the object
    </summary>
    """
    Margin = 0
    Page = 1
    Paragraph = 2
    Line = 3
    TopMarginArea = 4
    BottomMarginArea = 5
    InnerMarginArea = 6
    OuterMarginArea = 7
    TextFrameDefault = 2

