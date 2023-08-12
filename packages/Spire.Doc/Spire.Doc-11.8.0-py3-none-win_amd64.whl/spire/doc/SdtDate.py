from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtDate (  SdtControlProperties) :
    """

    """
    @dispatch
    def __init__(self):
        GetDllLibDoc().SdtDate_CreateSdtDate.restype = c_void_p
        intPtr = GetDllLibDoc().SdtDate_CreateSdtDate()
        super(SdtDate, self).__init__(intPtr)

    @property
    def Lid(self)->int:
        """

        """
        GetDllLibDoc().SdtDate_get_Lid.argtypes=[c_void_p]
        GetDllLibDoc().SdtDate_get_Lid.restype=c_int
        ret = GetDllLibDoc().SdtDate_get_Lid(self.Ptr)
        return ret

    @Lid.setter
    def Lid(self, value:int):
        GetDllLibDoc().SdtDate_set_Lid.argtypes=[c_void_p, c_int]
        GetDllLibDoc().SdtDate_set_Lid(self.Ptr, value)

    @property

    def DateFormat(self)->str:
        """

        """
        GetDllLibDoc().SdtDate_get_DateFormat.argtypes=[c_void_p]
        GetDllLibDoc().SdtDate_get_DateFormat.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SdtDate_get_DateFormat(self.Ptr))
        return ret


    @DateFormat.setter
    def DateFormat(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtDate_set_DateFormat.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SdtDate_set_DateFormat(self.Ptr, valuePtr)

    @property

    def CalendarType(self)->'CalendarType':
        """

        """
        GetDllLibDoc().SdtDate_get_CalendarType.argtypes=[c_void_p]
        GetDllLibDoc().SdtDate_get_CalendarType.restype=c_int
        ret = GetDllLibDoc().SdtDate_get_CalendarType(self.Ptr)
        objwraped = CalendarType(ret)
        return objwraped

    @CalendarType.setter
    def CalendarType(self, value:'CalendarType'):
        GetDllLibDoc().SdtDate_set_CalendarType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().SdtDate_set_CalendarType(self.Ptr, value.value)

    @property

    def FullDate(self)->'DateTime':
        """

        """
        GetDllLibDoc().SdtDate_get_FullDate.argtypes=[c_void_p]
        GetDllLibDoc().SdtDate_get_FullDate.restype=c_void_p
        intPtr = GetDllLibDoc().SdtDate_get_FullDate(self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @FullDate.setter
    def FullDate(self, value:'DateTime'):
        GetDllLibDoc().SdtDate_set_FullDate.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().SdtDate_set_FullDate(self.Ptr, value.Ptr)

