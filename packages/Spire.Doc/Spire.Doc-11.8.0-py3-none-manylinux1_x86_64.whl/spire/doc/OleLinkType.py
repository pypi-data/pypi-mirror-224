from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class OleLinkType(Enum):
    """
    <summary>
        Defines types of the ole object field
    </summary>
    """
    Embed = 0
    Link = 1

