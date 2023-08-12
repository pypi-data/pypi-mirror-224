from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TabLeader(Enum):
    """
    <summary>
        Specifies Tab leader.
    </summary>
    """
    NoLeader = 0
    Dotted = 1
    Hyphenated = 2
    Single = 3
    Heavy = 4
    MiddleDot = 5

