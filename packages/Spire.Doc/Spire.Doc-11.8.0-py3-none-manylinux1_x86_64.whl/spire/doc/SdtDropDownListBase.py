from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtDropDownListBase (  SdtControlProperties) :
    """

    """
    @property

    def ListItems(self)->'SdtListItemCollection':
        """
    <summary>
        Provides access to all list items <see cref="T:Spire.Doc.Documents.SdtListItem" /> of this <b>Sdt</b></summary>
        """
        GetDllLibDoc().SdtDropDownListBase_get_ListItems.argtypes=[c_void_p]
        GetDllLibDoc().SdtDropDownListBase_get_ListItems.restype=c_void_p
        intPtr = GetDllLibDoc().SdtDropDownListBase_get_ListItems(self.Ptr)
        from spire.doc import SdtListItemCollection
        ret = None if intPtr==None else SdtListItemCollection(intPtr)
        return ret


    @property

    def LastValue(self)->str:
        """

        """
        GetDllLibDoc().SdtDropDownListBase_get_LastValue.argtypes=[c_void_p]
        GetDllLibDoc().SdtDropDownListBase_get_LastValue.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SdtDropDownListBase_get_LastValue(self.Ptr))
        return ret


    @LastValue.setter
    def LastValue(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtDropDownListBase_set_LastValue.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SdtDropDownListBase_set_LastValue(self.Ptr, valuePtr)

