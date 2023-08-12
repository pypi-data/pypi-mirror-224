from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CompareOptions (SpireObject) :
    """
    <summary>
        Document comparison parameter settings.
    </summary>
    """
    @dispatch
    def __init__(self):
        GetDllLibDoc().CompareOptions_CreateCompareOptions.restype=c_void_p
        intPtr = GetDllLibDoc().CompareOptions_CreateCompareOptions()
        super(CompareOptions, self).__init__(intPtr)

    @property
    def IgnoreFormatting(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to ignore format comparisons when comparing documents.
            The default is false.
    </summary>
        """
        GetDllLibDoc().CompareOptions_get_IgnoreFormatting.argtypes=[c_void_p]
        GetDllLibDoc().CompareOptions_get_IgnoreFormatting.restype=c_bool
        ret = GetDllLibDoc().CompareOptions_get_IgnoreFormatting(self.Ptr)
        return ret

    @IgnoreFormatting.setter
    def IgnoreFormatting(self, value:bool):
        GetDllLibDoc().CompareOptions_set_IgnoreFormatting.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CompareOptions_set_IgnoreFormatting(self.Ptr, value)

