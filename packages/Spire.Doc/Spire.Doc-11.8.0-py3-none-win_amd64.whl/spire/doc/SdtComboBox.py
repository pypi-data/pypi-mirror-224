from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtComboBox (  SdtDropDownListBase) :
    """

    """
    @dispatch
    def __init__(self):
        GetDllLibDoc().SdtComboBox_CreateSdtComboBox.restype=c_void_p
        intPtr = GetDllLibDoc().SdtComboBox_CreateSdtComboBox()
        super(SdtComboBox, self).__init__(intPtr)

