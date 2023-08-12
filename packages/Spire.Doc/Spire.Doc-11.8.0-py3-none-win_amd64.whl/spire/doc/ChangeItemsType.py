from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ChangeItemsType(Enum):
    """
    <summary>
        Specifies Item DocumentObject type.
    </summary>
    """
    Add = 0
    Remove = 1
    Clear = 2

