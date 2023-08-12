from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PictureColor(Enum):
    """
    <summary>
        Picture color types.
    </summary>
    """
    Automatic = 0
    Grayscale = 1
    BlackAndWhite = 2
    Washout = 3

