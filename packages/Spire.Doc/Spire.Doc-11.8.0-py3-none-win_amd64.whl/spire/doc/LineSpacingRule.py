from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LineSpacingRule(Enum):
    """
    <summary>
        Paragraph line spacing rule
    </summary>
    """
    AtLeast = 0
    Exactly = 1
    Multiple = 2

