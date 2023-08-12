from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ObjectEntry (SpireObject) :
    """

    """
    @property

    def Current(self)->'DocumentObject':
        """

        """
        GetDllLibDoc().ObjectEntry_get_Current.argtypes=[c_void_p]
        GetDllLibDoc().ObjectEntry_get_Current.restype=c_void_p
        intPtr = GetDllLibDoc().ObjectEntry_get_Current(self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


    @Current.setter
    def Current(self, value:'DocumentObject'):
        GetDllLibDoc().ObjectEntry_set_Current.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().ObjectEntry_set_Current(self.Ptr, value.Ptr)

    @property
    def Index(self)->int:
        """

        """
        GetDllLibDoc().ObjectEntry_get_Index.argtypes=[c_void_p]
        GetDllLibDoc().ObjectEntry_get_Index.restype=c_int
        ret = GetDllLibDoc().ObjectEntry_get_Index(self.Ptr)
        return ret

    @Index.setter
    def Index(self, value:int):
        GetDllLibDoc().ObjectEntry_set_Index.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ObjectEntry_set_Index(self.Ptr, value)

    def Fetch(self)->bool:
        """

        """
        GetDllLibDoc().ObjectEntry_Fetch.argtypes=[c_void_p]
        GetDllLibDoc().ObjectEntry_Fetch.restype=c_bool
        ret = GetDllLibDoc().ObjectEntry_Fetch(self.Ptr)
        return ret

