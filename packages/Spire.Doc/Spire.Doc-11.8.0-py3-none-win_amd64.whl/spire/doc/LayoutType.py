from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LayoutType(Enum):
    """
    <summary>
        This simple type defines the possible type of layout algorthms which can be used
            to layout a table within a WordprocessingML document.
    </summary>
    """
    Fixed = 0
    AutoFit = 1

