from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Hyperlink (SpireObject) :
    """

    """
    @property

    def FilePath(self)->str:
        """
    <summary>
        Gets or sets file path.
    </summary>
        """
        GetDllLibDoc().Hyperlink_get_FilePath.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_FilePath.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Hyperlink_get_FilePath(self.Ptr))
        return ret


    @FilePath.setter
    def FilePath(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Hyperlink_set_FilePath.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Hyperlink_set_FilePath(self.Ptr, valuePtr)

    @property

    def Uri(self)->str:
        """
    <summary>
        Returns or sets url link. 
    </summary>
        """
        GetDllLibDoc().Hyperlink_get_Uri.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_Uri.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Hyperlink_get_Uri(self.Ptr))
        return ret


    @Uri.setter
    def Uri(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Hyperlink_set_Uri.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Hyperlink_set_Uri(self.Ptr, valuePtr)

    @property

    def BookmarkName(self)->str:
        """
    <summary>
        Returns or sets bookmark.
    </summary>
        """
        GetDllLibDoc().Hyperlink_get_BookmarkName.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_BookmarkName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Hyperlink_get_BookmarkName(self.Ptr))
        return ret


    @BookmarkName.setter
    def BookmarkName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Hyperlink_set_BookmarkName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Hyperlink_set_BookmarkName(self.Ptr, valuePtr)

    @property

    def Type(self)->'HyperlinkType':
        """
    <summary>
        Returns or sets a HyperlinkType object that indicates the link type. 
    </summary>
        """
        GetDllLibDoc().Hyperlink_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_Type.restype=c_int
        ret = GetDllLibDoc().Hyperlink_get_Type(self.Ptr)
        objwraped = HyperlinkType(ret)
        return objwraped

    @Type.setter
    def Type(self, value:'HyperlinkType'):
        GetDllLibDoc().Hyperlink_set_Type.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Hyperlink_set_Type(self.Ptr, value.value)

    @property

    def TextToDisplay(self)->str:
        """
    <summary>
        Gets or sets the specified hyperlink's visible text in a document.
    </summary>
<value>The text to display.</value>
        """
        GetDllLibDoc().Hyperlink_get_TextToDisplay.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_TextToDisplay.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Hyperlink_get_TextToDisplay(self.Ptr))
        return ret


    @TextToDisplay.setter
    def TextToDisplay(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Hyperlink_set_TextToDisplay.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Hyperlink_set_TextToDisplay(self.Ptr, valuePtr)

    @property

    def PictureToDisplay(self)->'ShapeObject':
        """
    <summary>
        Gets or sets the image which will be displayed on the place of hyperlink.
    </summary>
        """
        GetDllLibDoc().Hyperlink_get_PictureToDisplay.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_PictureToDisplay.restype=c_void_p
        intPtr = GetDllLibDoc().Hyperlink_get_PictureToDisplay(self.Ptr)
        ret = None if intPtr==None else ShapeObject(intPtr)
        return ret


    @PictureToDisplay.setter
    def PictureToDisplay(self, value:'ShapeObject'):
        GetDllLibDoc().Hyperlink_set_PictureToDisplay.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().Hyperlink_set_PictureToDisplay(self.Ptr, value.Ptr)

    def Dispose(self):
        """

        """
        GetDllLibDoc().Hyperlink_Dispose.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_Dispose(self.Ptr)

