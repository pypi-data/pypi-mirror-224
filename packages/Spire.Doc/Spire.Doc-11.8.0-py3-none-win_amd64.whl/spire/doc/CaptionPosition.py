from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CaptionPosition(Enum):
    """
    <summary>
        Position of Image Caption Numbering
    </summary>
    """
    AboveImage = 0
    AfterImage = 1
    AboveItem = 0
    BelowItem = 1

