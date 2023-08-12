from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class InternalMargin (SpireObject) :
    """

    """
    def SetAll(self, value:float):
        GetDllLibDoc().InternalMargin_set_All.argtypes=[c_void_p, c_float]
        GetDllLibDoc().InternalMargin_set_All(self.Ptr, value)

    @property
    def Left(self)->float:
        """
    <summary>
        Gets or sets the internal left margin (in points).
    </summary>
<value>The internal left margin.</value>
        """
        GetDllLibDoc().InternalMargin_get_Left.argtypes=[c_void_p]
        GetDllLibDoc().InternalMargin_get_Left.restype=c_float
        ret = GetDllLibDoc().InternalMargin_get_Left(self.Ptr)
        return ret

    @Left.setter
    def Left(self, value:float):
        GetDllLibDoc().InternalMargin_set_Left.argtypes=[c_void_p, c_float]
        GetDllLibDoc().InternalMargin_set_Left(self.Ptr, value)

    @property
    def Right(self)->float:
        """
    <summary>
        Gets or sets the internal right margin (in points).
    </summary>
<value>The internal right margin.</value>
        """
        GetDllLibDoc().InternalMargin_get_Right.argtypes=[c_void_p]
        GetDllLibDoc().InternalMargin_get_Right.restype=c_float
        ret = GetDllLibDoc().InternalMargin_get_Right(self.Ptr)
        return ret

    @Right.setter
    def Right(self, value:float):
        GetDllLibDoc().InternalMargin_set_Right.argtypes=[c_void_p, c_float]
        GetDllLibDoc().InternalMargin_set_Right(self.Ptr, value)

    @property
    def Top(self)->float:
        """
    <summary>
        Gets or sets the internal top margin (in points).
    </summary>
<value>The internal top margin.</value>
        """
        GetDllLibDoc().InternalMargin_get_Top.argtypes=[c_void_p]
        GetDllLibDoc().InternalMargin_get_Top.restype=c_float
        ret = GetDllLibDoc().InternalMargin_get_Top(self.Ptr)
        return ret

    @Top.setter
    def Top(self, value:float):
        GetDllLibDoc().InternalMargin_set_Top.argtypes=[c_void_p, c_float]
        GetDllLibDoc().InternalMargin_set_Top(self.Ptr, value)

    @property
    def Bottom(self)->float:
        """
    <summary>
        Gets or sets the internal bottom margin (in points).
    </summary>
<value>The internal bottom margin.</value>
        """
        GetDllLibDoc().InternalMargin_get_Bottom.argtypes=[c_void_p]
        GetDllLibDoc().InternalMargin_get_Bottom.restype=c_float
        ret = GetDllLibDoc().InternalMargin_get_Bottom(self.Ptr)
        return ret

    @Bottom.setter
    def Bottom(self, value:float):
        GetDllLibDoc().InternalMargin_set_Bottom.argtypes=[c_void_p, c_float]
        GetDllLibDoc().InternalMargin_set_Bottom(self.Ptr, value)

