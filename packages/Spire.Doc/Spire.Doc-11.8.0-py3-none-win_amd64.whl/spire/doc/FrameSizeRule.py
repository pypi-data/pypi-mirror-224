from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FrameSizeRule(Enum):
    """
    <summary>
        Frame size rule.
    </summary>
    """
    AtLeast = 0
    Exact = 1
    Auto = 2

