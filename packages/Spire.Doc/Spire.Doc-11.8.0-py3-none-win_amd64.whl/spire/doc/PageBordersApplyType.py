from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PageBordersApplyType(Enum):
    """
    <summary>
        Specifies on which pages border is applied.
    </summary>
    """
    AllPages = 0
    FirstPage = 1
    AllExceptFirstPage = 2

