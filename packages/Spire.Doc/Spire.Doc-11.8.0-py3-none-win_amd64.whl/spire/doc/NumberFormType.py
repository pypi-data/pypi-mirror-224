from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class NumberFormType(Enum):
    """
    <summary>
        Specifies the number form type.
    </summary>
    """
    Default = 0
    Lining = 1
    Old = 2

