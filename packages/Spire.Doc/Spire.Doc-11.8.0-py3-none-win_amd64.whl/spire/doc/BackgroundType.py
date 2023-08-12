from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BackgroundType(Enum):
    """
    <summary>
        Specifies BackgroundType
    </summary>
    """
    NoBackground = 0
    Gradient = 1
    Picture = 2
    Texture = 3
    Color = 4

