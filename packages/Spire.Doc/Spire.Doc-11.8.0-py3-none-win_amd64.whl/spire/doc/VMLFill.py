from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class VMLFill (SpireObject) :
    """

    """
    @property

    def Color(self)->'Color':
        """

        """
        GetDllLibDoc().VMLFill_get_Color.argtypes=[c_void_p]
        GetDllLibDoc().VMLFill_get_Color.restype=c_void_p
        intPtr = GetDllLibDoc().VMLFill_get_Color(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @Color.setter
    def Color(self, value:'Color'):
        GetDllLibDoc().VMLFill_set_Color.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().VMLFill_set_Color(self.Ptr, value.Ptr)

    @property
    def Opacity(self)->float:
        """

        """
        GetDllLibDoc().VMLFill_get_Opacity.argtypes=[c_void_p]
        GetDllLibDoc().VMLFill_get_Opacity.restype=c_double
        ret = GetDllLibDoc().VMLFill_get_Opacity(self.Ptr)
        return ret

    @Opacity.setter
    def Opacity(self, value:float):
        GetDllLibDoc().VMLFill_set_Opacity.argtypes=[c_void_p, c_double]
        GetDllLibDoc().VMLFill_set_Opacity(self.Ptr, value)

    @property
    def On(self)->bool:
        """

        """
        GetDllLibDoc().VMLFill_get_On.argtypes=[c_void_p]
        GetDllLibDoc().VMLFill_get_On.restype=c_bool
        ret = GetDllLibDoc().VMLFill_get_On(self.Ptr)
        return ret

    @On.setter
    def On(self, value:bool):
        GetDllLibDoc().VMLFill_set_On.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().VMLFill_set_On(self.Ptr, value)

#    @property
#
#    def ImageBytes(self)->List['Byte']:
#        """
#
#        """
#        GetDllLibDoc().VMLFill_get_ImageBytes.argtypes=[c_void_p]
#        GetDllLibDoc().VMLFill_get_ImageBytes.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().VMLFill_get_ImageBytes(self.Ptr)
#        ret = GetVectorFromArray(intPtrArray, Byte)
#        return ret


