from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtListItem (SpireObject) :
    """

    """
    @dispatch
    def __init__(self, displayText:str, value:str):
        displayTextPtr = StrToPtr(displayText)
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtListItem_CreateSdtListItemDV.argtypes=[c_char_p,c_char_p]
        GetDllLibDoc().SdtListItem_CreateSdtListItemDV.restype=c_void_p
        intPtr = GetDllLibDoc().SdtListItem_CreateSdtListItemDV(displayTextPtr,valuePtr)
        super(SdtListItem, self).__init__(intPtr)

    @dispatch
    def __init__(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtListItem_CreateSdtListItemV.argtypes=[c_char_p]
        GetDllLibDoc().SdtListItem_CreateSdtListItemV.restype=c_void_p
        intPtr = GetDllLibDoc().SdtListItem_CreateSdtListItemV(valuePtr)
        super(SdtListItem, self).__init__(intPtr)

    @property

    def DisplayText(self)->str:
        """

        """
        GetDllLibDoc().SdtListItem_get_DisplayText.argtypes=[c_void_p]
        GetDllLibDoc().SdtListItem_get_DisplayText.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SdtListItem_get_DisplayText(self.Ptr))
        return ret


    @DisplayText.setter
    def DisplayText(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtListItem_set_DisplayText.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SdtListItem_set_DisplayText(self.Ptr, valuePtr)

    @property

    def Value(self)->str:
        """

        """
        GetDllLibDoc().SdtListItem_get_Value.argtypes=[c_void_p]
        GetDllLibDoc().SdtListItem_get_Value.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SdtListItem_get_Value(self.Ptr))
        return ret


    @Value.setter
    def Value(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtListItem_set_Value.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SdtListItem_set_Value(self.Ptr, valuePtr)

