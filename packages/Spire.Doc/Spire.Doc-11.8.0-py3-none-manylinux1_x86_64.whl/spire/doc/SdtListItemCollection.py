from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtListItemCollection (  IEnumerable) :
    """

    """

    def GetEnumerator(self)->'IEnumerator':
        """

        """
        GetDllLibDoc().SdtListItemCollection_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().SdtListItemCollection_GetEnumerator.restype=c_void_p
        intPtr = GetDllLibDoc().SdtListItemCollection_GetEnumerator(self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret



    def Add(self ,item:'SdtListItem'):
        """

        """
        intPtritem:c_void_p = item.Ptr

        GetDllLibDoc().SdtListItemCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().SdtListItemCollection_Add(self.Ptr, intPtritem)


    def RemoveAt(self ,index:int):
        """

        """
        
        GetDllLibDoc().SdtListItemCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().SdtListItemCollection_RemoveAt(self.Ptr, index)

    def Clear(self):
        """

        """
        GetDllLibDoc().SdtListItemCollection_Clear.argtypes=[c_void_p]
        GetDllLibDoc().SdtListItemCollection_Clear(self.Ptr)

    @property

    def SelectedValue(self)->'SdtListItem':
        """

        """
        GetDllLibDoc().SdtListItemCollection_get_SelectedValue.argtypes=[c_void_p]
        GetDllLibDoc().SdtListItemCollection_get_SelectedValue.restype=c_void_p
        intPtr = GetDllLibDoc().SdtListItemCollection_get_SelectedValue(self.Ptr)
        ret = None if intPtr==None else SdtListItem(intPtr)
        return ret


    @SelectedValue.setter
    def SelectedValue(self, value:'SdtListItem'):
        GetDllLibDoc().SdtListItemCollection_set_SelectedValue.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().SdtListItemCollection_set_SelectedValue(self.Ptr, value.Ptr)


    def get_Item(self ,index:int)->'SdtListItem':
        """

        """
        
        GetDllLibDoc().SdtListItemCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().SdtListItemCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().SdtListItemCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else SdtListItem(intPtr)
        return ret


    @property
    def Count(self)->int:
        """

        """
        GetDllLibDoc().SdtListItemCollection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().SdtListItemCollection_get_Count.restype=c_int
        ret = GetDllLibDoc().SdtListItemCollection_get_Count(self.Ptr)
        return ret

