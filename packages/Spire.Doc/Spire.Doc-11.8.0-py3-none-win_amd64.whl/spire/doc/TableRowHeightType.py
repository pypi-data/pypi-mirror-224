from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TableRowHeightType(Enum):
    """
    <summary>
        Specifies the table row height type.
    </summary>
    """
    AtLeast = 0
    Exactly = 1
    Auto = 2

