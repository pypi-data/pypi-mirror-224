from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CustomXmlPartCollection (  IEnumerable) :
    """

    """
    @property
    def Count(self)->int:
        """

        """
        GetDllLibDoc().CustomXmlPartCollection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().CustomXmlPartCollection_get_Count.restype=c_int
        ret = GetDllLibDoc().CustomXmlPartCollection_get_Count(self.Ptr)
        return ret


    def get_Item(self ,index:int)->'CustomXmlPart':
        """

        """
        
        GetDllLibDoc().CustomXmlPartCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().CustomXmlPartCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().CustomXmlPartCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else CustomXmlPart(intPtr)
        return ret



    def set_Item(self ,index:int,value:'CustomXmlPart'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().CustomXmlPartCollection_set_Item.argtypes=[c_void_p ,c_int,c_void_p]
        GetDllLibDoc().CustomXmlPartCollection_set_Item(self.Ptr, index,intPtrvalue)


    def GetEnumerator(self)->'IEnumerator':
        """

        """
        GetDllLibDoc().CustomXmlPartCollection_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().CustomXmlPartCollection_GetEnumerator.restype=c_void_p
        intPtr = GetDllLibDoc().CustomXmlPartCollection_GetEnumerator(self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret



    def Add(self ,part:'CustomXmlPart'):
        """

        """
        intPtrpart:c_void_p = part.Ptr

        GetDllLibDoc().CustomXmlPartCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().CustomXmlPartCollection_Add(self.Ptr, intPtrpart)


    def RemoveAt(self ,index:int):
        """

        """
        
        GetDllLibDoc().CustomXmlPartCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().CustomXmlPartCollection_RemoveAt(self.Ptr, index)

    def Clear(self):
        """

        """
        GetDllLibDoc().CustomXmlPartCollection_Clear.argtypes=[c_void_p]
        GetDllLibDoc().CustomXmlPartCollection_Clear(self.Ptr)


    def GetById(self ,id:str)->'CustomXmlPart':
        """

        """
        idPtr = StrToPtr(id)
        GetDllLibDoc().CustomXmlPartCollection_GetById.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().CustomXmlPartCollection_GetById.restype=c_void_p
        intPtr = GetDllLibDoc().CustomXmlPartCollection_GetById(self.Ptr, idPtr)
        ret = None if intPtr==None else CustomXmlPart(intPtr)
        return ret



    def Clone(self)->'CustomXmlPartCollection':
        """

        """
        GetDllLibDoc().CustomXmlPartCollection_Clone.argtypes=[c_void_p]
        GetDllLibDoc().CustomXmlPartCollection_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().CustomXmlPartCollection_Clone(self.Ptr)
        ret = None if intPtr==None else CustomXmlPartCollection(intPtr)
        return ret


