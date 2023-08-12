from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class WrapMode(Enum):
    """
    <summary>
        Specifies Wrap mode.
    </summary>
    """
    Square = 0
    ByPoints = 1
    none = 2
    TopBottom = 3
    Through = 4
    Inline = 5

