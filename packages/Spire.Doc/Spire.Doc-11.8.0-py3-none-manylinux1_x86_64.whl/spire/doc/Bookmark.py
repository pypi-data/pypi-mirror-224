from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Bookmark (SpireObject) :
    """

    """
    @property

    def Name(self)->str:
        """
    <summary>
        Gets bookmark name.
    </summary>
        """
        GetDllLibDoc().Bookmark_get_Name.argtypes=[c_void_p]
        GetDllLibDoc().Bookmark_get_Name.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Bookmark_get_Name(self.Ptr))
        return ret


    @property

    def BookmarkStart(self)->'BookmarkStart':
        """
    <summary>
        Gets the bookmark start.
    </summary>
        """
        GetDllLibDoc().Bookmark_get_BookmarkStart.argtypes=[c_void_p]
        GetDllLibDoc().Bookmark_get_BookmarkStart.restype=c_void_p
        intPtr = GetDllLibDoc().Bookmark_get_BookmarkStart(self.Ptr)
        from spire.doc import BookmarkStart
        ret = None if intPtr==None else BookmarkStart(intPtr)
        return ret


    @property

    def BookmarkEnd(self)->'BookmarkEnd':
        """
    <summary>
        Gets the bookmark end.
    </summary>
        """
        GetDllLibDoc().Bookmark_get_BookmarkEnd.argtypes=[c_void_p]
        GetDllLibDoc().Bookmark_get_BookmarkEnd.restype=c_void_p
        intPtr = GetDllLibDoc().Bookmark_get_BookmarkEnd(self.Ptr)
        from spire.doc import BookmarkEnd
        ret = None if intPtr==None else BookmarkEnd(intPtr)
        return ret


