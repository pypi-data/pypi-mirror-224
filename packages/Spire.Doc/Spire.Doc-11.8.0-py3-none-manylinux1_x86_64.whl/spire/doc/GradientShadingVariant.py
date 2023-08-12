from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class GradientShadingVariant(Enum):
    """
    <summary>
        Shading variants for background gradient.
    </summary>
    """
    ShadingUp = 0
    ShadingDown = 1
    ShadingOut = 2
    ShadingMiddle = 3

