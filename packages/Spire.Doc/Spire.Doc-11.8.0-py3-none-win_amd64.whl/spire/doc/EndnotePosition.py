from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class EndnotePosition(Enum):
    """
    <summary>
        Endnote position of the Document.
    </summary>
    """
    DisplayEndOfSection = 0
    DisplayEndOfDocument = 3

