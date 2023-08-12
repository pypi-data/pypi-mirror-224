from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtDropDownList (  SdtDropDownListBase) :
    """

    """
    @dispatch
    def __init__(self):
        GetDllLibDoc().SdtDropDownList_CreateSdtDropDownList.restype = c_void_p
        intPtr = GetDllLibDoc().SdtDropDownList_CreateSdtDropDownList()
        super(SdtDropDownList, self).__init__(intPtr)
