from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PreferredWidth (SpireObject) :
    """
    <summary>
        An PreferredWidth class that specifies the preferred total width of the table
            of which this row is a part.
    </summary>
    """
    @dispatch
    def __init__(self,widthType:WidthType, value:int):
        iTypetype:c_int = widthType.value

        GetDllLibDoc().PreferredWidth_CreatePreferredWidthTV.argtypes=[c_int,c_int]
        GetDllLibDoc().PreferredWidth_CreatePreferredWidthTV.restype=c_void_p
        intPtr = GetDllLibDoc().PreferredWidth_CreatePreferredWidthTV(iTypetype,value)
        super(PreferredWidth, self).__init__(intPtr)

    @property
    def Value(self)->float:
        """
    <summary>
        An double value that specifies the preferred width
    </summary>
        """
        GetDllLibDoc().PreferredWidth_get_Value.argtypes=[c_void_p]
        GetDllLibDoc().PreferredWidth_get_Value.restype=c_float
        ret = GetDllLibDoc().PreferredWidth_get_Value(self.Ptr)
        return ret

    @property

    def Type(self)->'WidthType':
        """
    <summary>
        A enum element from WidthType that specifies the units of measurement for the Value.
    </summary>
        """
        GetDllLibDoc().PreferredWidth_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().PreferredWidth_get_Type.restype=c_int
        ret = GetDllLibDoc().PreferredWidth_get_Type(self.Ptr)
        objwraped = WidthType(ret)
        return objwraped

    @staticmethod

    def get_Auto()->'PreferredWidth':
        """
    <summary>
        Get an instance of PreferredWidth, this instance indicates
            thie preferred width is auto.
    </summary>
        """
        #GetDllLibDoc().PreferredWidth_get_Auto.argtypes=[]
        GetDllLibDoc().PreferredWidth_get_Auto.restype=c_void_p
        intPtr = GetDllLibDoc().PreferredWidth_get_Auto()
        ret = None if intPtr==None else PreferredWidth(intPtr)
        return ret


    @staticmethod

    def get_None()->'PreferredWidth':
        """
    <summary>
        Get an instance of PreferredWidth, this instance indicates
            thie preferred width is not specified.
    </summary>
        """
        #GetDllLibDoc().PreferredWidth_get_None.argtypes=[]
        GetDllLibDoc().PreferredWidth_get_None.restype=c_void_p
        intPtr = GetDllLibDoc().PreferredWidth_get_None()
        ret = None if intPtr==None else PreferredWidth(intPtr)
        return ret



    def Equals(self ,obj:'SpireObject')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        GetDllLibDoc().PreferredWidth_Equals.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().PreferredWidth_Equals.restype=c_bool
        ret = GetDllLibDoc().PreferredWidth_Equals(self.Ptr, intPtrobj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        GetDllLibDoc().PreferredWidth_GetHashCode.argtypes=[c_void_p]
        GetDllLibDoc().PreferredWidth_GetHashCode.restype=c_int
        ret = GetDllLibDoc().PreferredWidth_GetHashCode(self.Ptr)
        return ret

