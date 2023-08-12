from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class StyleType(Enum):
    """
    <summary>
        Specifies type of the Style.
    </summary>
    """
    ParagraphStyle = 1
    CharacterStyle = 2
    TableStyle = 3
    ListStyle = 4
    OtherStyle = 4

