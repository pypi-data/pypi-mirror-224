from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CaptionNumberingFormat(Enum):
    """
    <summary>
        Type of Caption Numbering
    </summary>
    """
    Number = 0
    Roman = 1
    Alphabetic = 2

