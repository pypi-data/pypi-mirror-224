from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class AutoFitBehaviorType(Enum):
    """
    <summary>
        Specifies how Microsoft Word resizes a table when the AutoFit feature is used.
    </summary>
    """
    AutoFitToContents = 1
    AutoFitToWindow = 2
    FixedColumnWidths = 0

