from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HttpContentType(Enum):
    """
    <summary>
        Http content to browser.
    </summary>
    """
    InBrowser = 0
    Attachment = 1

