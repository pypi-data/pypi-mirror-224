from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class GroupedShapeOrigin(Enum):
    """
    <summary>
          Specify vertical/horizontal origin the object in the GroupedShape.
    </summary>
    """
    UpperLeftCorner = 0
    Center = 1

