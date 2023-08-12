from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class NumberSpaceType(Enum):
    """
    <summary>
        Specifies the number spacing type.
    </summary>
    """
    Default = 0
    Proportional = 1
    Tabular = 2

