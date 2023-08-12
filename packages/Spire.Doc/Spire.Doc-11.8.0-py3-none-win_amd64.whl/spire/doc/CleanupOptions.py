from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CleanupOptions (SpireObject) :
    """

    """
    @property
    def UnusedStyles(self)->bool:
        """

        """
        GetDllLibDoc().CleanupOptions_get_UnusedStyles.argtypes=[c_void_p]
        GetDllLibDoc().CleanupOptions_get_UnusedStyles.restype=c_bool
        ret = GetDllLibDoc().CleanupOptions_get_UnusedStyles(self.Ptr)
        return ret

    @UnusedStyles.setter
    def UnusedStyles(self, value:bool):
        GetDllLibDoc().CleanupOptions_set_UnusedStyles.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CleanupOptions_set_UnusedStyles(self.Ptr, value)

    @property
    def UnusedLists(self)->bool:
        """

        """
        GetDllLibDoc().CleanupOptions_get_UnusedLists.argtypes=[c_void_p]
        GetDllLibDoc().CleanupOptions_get_UnusedLists.restype=c_bool
        ret = GetDllLibDoc().CleanupOptions_get_UnusedLists(self.Ptr)
        return ret

    @UnusedLists.setter
    def UnusedLists(self, value:bool):
        GetDllLibDoc().CleanupOptions_set_UnusedLists.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CleanupOptions_set_UnusedLists(self.Ptr, value)

