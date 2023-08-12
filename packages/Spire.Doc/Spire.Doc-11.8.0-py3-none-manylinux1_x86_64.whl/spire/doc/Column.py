from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Column (  DocumentSerializable) :
    """

    """
    @property
    def Width(self)->float:
        """
    <summary>
        Returns or sets column width.
    </summary>
        """
        GetDllLibDoc().Column_get_Width.argtypes=[c_void_p]
        GetDllLibDoc().Column_get_Width.restype=c_float
        ret = GetDllLibDoc().Column_get_Width(self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:float):
        GetDllLibDoc().Column_set_Width.argtypes=[c_void_p, c_float]
        GetDllLibDoc().Column_set_Width(self.Ptr, value)

    @property
    def Space(self)->float:
        """
    <summary>
        Gets or setss pacing between current and next column.
    </summary>
        """
        GetDllLibDoc().Column_get_Space.argtypes=[c_void_p]
        GetDllLibDoc().Column_get_Space.restype=c_float
        ret = GetDllLibDoc().Column_get_Space(self.Ptr)
        return ret

    @Space.setter
    def Space(self, value:float):
        GetDllLibDoc().Column_set_Space.argtypes=[c_void_p, c_float]
        GetDllLibDoc().Column_set_Space(self.Ptr, value)

