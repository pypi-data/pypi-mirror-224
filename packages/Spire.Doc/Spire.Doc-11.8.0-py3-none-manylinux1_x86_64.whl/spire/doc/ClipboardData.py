from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ClipboardData (SpireObject) :
    """

    """
    @property
    def Format(self)->int:
        """
    <summary>
        Clipboard format.
    </summary>
        """
        GetDllLibDoc().ClipboardData_get_Format.argtypes=[c_void_p]
        GetDllLibDoc().ClipboardData_get_Format.restype=c_int
        ret = GetDllLibDoc().ClipboardData_get_Format(self.Ptr)
        return ret

    @Format.setter
    def Format(self, value:int):
        GetDllLibDoc().ClipboardData_set_Format.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ClipboardData_set_Format(self.Ptr, value)

#    @property
#
#    def Data(self)->List['Byte']:
#        """
#    <summary>
#        Clipboard data.
#    </summary>
#        """
#        GetDllLibDoc().ClipboardData_get_Data.argtypes=[c_void_p]
#        GetDllLibDoc().ClipboardData_get_Data.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().ClipboardData_get_Data(self.Ptr)
#        ret = GetVectorFromArray(intPtrArray, Byte)
#        return ret


#    @Data.setter
#    def Data(self, value:List['Byte']):
#        vCount = len(value)
#        ArrayType = c_void_p * vCount
#        vArray = ArrayType()
#        for i in range(0, vCount):
#            vArray[i] = value[i].Ptr
#        GetDllLibDoc().ClipboardData_set_Data.argtypes=[c_void_p, ArrayType, c_int]
#        GetDllLibDoc().ClipboardData_set_Data(self.Ptr, vArray, vCount)



    def Clone(self)->'SpireObject':
        """
    <summary>
        Createas copy of the current object.
    </summary>
    <returns>A copy of the current object.</returns>
        """
        GetDllLibDoc().ClipboardData_Clone.argtypes=[c_void_p]
        GetDllLibDoc().ClipboardData_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().ClipboardData_Clone(self.Ptr)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret



    def Serialize(self ,stream:'Stream')->int:
        """

        """
        intPtrstream:c_void_p = stream.Ptr

        GetDllLibDoc().ClipboardData_Serialize.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ClipboardData_Serialize.restype=c_int
        ret = GetDllLibDoc().ClipboardData_Serialize(self.Ptr, intPtrstream)
        return ret


    def Parse(self ,stream:'Stream'):
        """

        """
        intPtrstream:c_void_p = stream.Ptr

        GetDllLibDoc().ClipboardData_Parse.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ClipboardData_Parse(self.Ptr, intPtrstream)

