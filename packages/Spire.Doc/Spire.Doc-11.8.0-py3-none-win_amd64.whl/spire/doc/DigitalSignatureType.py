from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DigitalSignatureType(Enum):
    """

    """
    Unknown = 0
    CryptoApi = 1
    XmlDsig = 2

