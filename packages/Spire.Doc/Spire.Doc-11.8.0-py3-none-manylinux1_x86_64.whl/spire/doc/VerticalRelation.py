from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class VerticalRelation(Enum):
    """
    <summary>
        The enum defines the vertical relation
    </summary>
    """
    Margin = 0
    Page = 1
    Paragraph = 2

