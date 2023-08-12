from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBoxLineStyle(Enum):
    """
    <summary>
        Specify object's line style
    </summary>
    """
    Simple = 0
    Double = 1
    ThickThin = 2
    ThinThick = 3
    Triple = 4

