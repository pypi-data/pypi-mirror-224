from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PageNumberAlignment(Enum):
    """
    <summary>
        Specifies PageNumber alignment.
    </summary>
    """
    Left = 0
    Center = -4
    Right = -8
    Inside = -12
    Outside = -16

