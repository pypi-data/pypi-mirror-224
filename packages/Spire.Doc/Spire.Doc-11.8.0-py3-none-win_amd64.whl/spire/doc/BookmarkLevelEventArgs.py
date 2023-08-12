from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BookmarkLevelEventArgs (SpireObject) :
    """
    <summary>
        BookmarkLevelEventArgs is the class containg event data.
    </summary>
    """
    @property

    def BookmarkStart(self)->'BookmarkStart':
        """
    <summary>
        Represents the current bookmark.
    </summary>
        """
        GetDllLibDoc().BookmarkLevelEventArgs_get_BookmarkStart.argtypes=[c_void_p]
        GetDllLibDoc().BookmarkLevelEventArgs_get_BookmarkStart.restype=c_void_p
        intPtr = GetDllLibDoc().BookmarkLevelEventArgs_get_BookmarkStart(self.Ptr)
        ret = None if intPtr==None else BookmarkStart(intPtr)
        return ret


    @BookmarkStart.setter
    def BookmarkStart(self, value:'BookmarkStart'):
        GetDllLibDoc().BookmarkLevelEventArgs_set_BookmarkStart.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().BookmarkLevelEventArgs_set_BookmarkStart(self.Ptr, value.Ptr)

    @property

    def BookmarkLevel(self)->'BookmarkLevel':
        """
    <summary>
        Represents the current bookmark level informations.
    </summary>
        """
        GetDllLibDoc().BookmarkLevelEventArgs_get_BookmarkLevel.argtypes=[c_void_p]
        GetDllLibDoc().BookmarkLevelEventArgs_get_BookmarkLevel.restype=c_void_p
        intPtr = GetDllLibDoc().BookmarkLevelEventArgs_get_BookmarkLevel(self.Ptr)
        ret = None if intPtr==None else BookmarkLevel(intPtr)
        return ret


    @BookmarkLevel.setter
    def BookmarkLevel(self, value:'BookmarkLevel'):
        GetDllLibDoc().BookmarkLevelEventArgs_set_BookmarkLevel.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().BookmarkLevelEventArgs_set_BookmarkLevel(self.Ptr, value.Ptr)

