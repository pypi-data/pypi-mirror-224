from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class OdsoRecipientDataCollection (  IEnumerable) :
    """

    """
    @property
    def Count(self)->int:
        """

        """
        GetDllLibDoc().OdsoRecipientDataCollection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().OdsoRecipientDataCollection_get_Count.restype=c_int
        ret = GetDllLibDoc().OdsoRecipientDataCollection_get_Count(self.Ptr)
        return ret


    def get_Item(self ,index:int)->'OdsoRecipientData':
        """

        """
        
        GetDllLibDoc().OdsoRecipientDataCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().OdsoRecipientDataCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().OdsoRecipientDataCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else OdsoRecipientData(intPtr)
        return ret



    def set_Item(self ,index:int,value:'OdsoRecipientData'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().OdsoRecipientDataCollection_set_Item.argtypes=[c_void_p ,c_int,c_void_p]
        GetDllLibDoc().OdsoRecipientDataCollection_set_Item(self.Ptr, index,intPtrvalue)


    def GetEnumerator(self)->'IEnumerator':
        """

        """
        GetDllLibDoc().OdsoRecipientDataCollection_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().OdsoRecipientDataCollection_GetEnumerator.restype=c_void_p
        intPtr = GetDllLibDoc().OdsoRecipientDataCollection_GetEnumerator(self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret



    def Add(self ,value:'OdsoRecipientData')->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().OdsoRecipientDataCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().OdsoRecipientDataCollection_Add.restype=c_int
        ret = GetDllLibDoc().OdsoRecipientDataCollection_Add(self.Ptr, intPtrvalue)
        return ret

    def Clear(self):
        """

        """
        GetDllLibDoc().OdsoRecipientDataCollection_Clear.argtypes=[c_void_p]
        GetDllLibDoc().OdsoRecipientDataCollection_Clear(self.Ptr)


    def RemoveAt(self ,index:int):
        """

        """
        
        GetDllLibDoc().OdsoRecipientDataCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().OdsoRecipientDataCollection_RemoveAt(self.Ptr, index)

