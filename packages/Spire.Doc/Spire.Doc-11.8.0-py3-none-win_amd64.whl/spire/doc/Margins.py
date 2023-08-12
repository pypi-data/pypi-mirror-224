from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Margins (SpireObject) :
    """

    """
    @property
    def All(self)->int:
        """

        """
        GetDllLibDoc().Margins_get_All.argtypes=[c_void_p]
        GetDllLibDoc().Margins_get_All.restype=c_int
        ret = GetDllLibDoc().Margins_get_All(self.Ptr)
        return ret

    @All.setter
    def All(self, value:int):
        GetDllLibDoc().Margins_set_All.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Margins_set_All(self.Ptr, value)

    @property
    def Left(self)->int:
        """

        """
        GetDllLibDoc().Margins_get_Left.argtypes=[c_void_p]
        GetDllLibDoc().Margins_get_Left.restype=c_int
        ret = GetDllLibDoc().Margins_get_Left(self.Ptr)
        return ret

    @Left.setter
    def Left(self, value:int):
        GetDllLibDoc().Margins_set_Left.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Margins_set_Left(self.Ptr, value)

    @property
    def Right(self)->int:
        """

        """
        GetDllLibDoc().Margins_get_Right.argtypes=[c_void_p]
        GetDllLibDoc().Margins_get_Right.restype=c_int
        ret = GetDllLibDoc().Margins_get_Right(self.Ptr)
        return ret

    @Right.setter
    def Right(self, value:int):
        GetDllLibDoc().Margins_set_Right.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Margins_set_Right(self.Ptr, value)

    @property
    def Top(self)->int:
        """

        """
        GetDllLibDoc().Margins_get_Top.argtypes=[c_void_p]
        GetDllLibDoc().Margins_get_Top.restype=c_int
        ret = GetDllLibDoc().Margins_get_Top(self.Ptr)
        return ret

    @Top.setter
    def Top(self, value:int):
        GetDllLibDoc().Margins_set_Top.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Margins_set_Top(self.Ptr, value)

    @property
    def Bottom(self)->int:
        """

        """
        GetDllLibDoc().Margins_get_Bottom.argtypes=[c_void_p]
        GetDllLibDoc().Margins_get_Bottom.restype=c_int
        ret = GetDllLibDoc().Margins_get_Bottom(self.Ptr)
        return ret

    @Bottom.setter
    def Bottom(self, value:int):
        GetDllLibDoc().Margins_set_Bottom.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Margins_set_Bottom(self.Ptr, value)

