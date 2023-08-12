from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class WatermarkType(Enum):
    """
    <summary>
        Specifies the watermark type.
    </summary>
    """
    NoWatermark = 0
    PictureWatermark = 1
    TextWatermark = 2

