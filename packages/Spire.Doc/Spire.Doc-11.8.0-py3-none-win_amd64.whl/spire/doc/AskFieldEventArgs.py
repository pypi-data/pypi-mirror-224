from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class AskFieldEventArgs (  IFieldsEventArgs) :
    """
    <summary>
        Class AskFieldEventArgs;
    </summary>
    """
    @property

    def Field(self)->'Field':
        """
    <summary>
        Gets 
    </summary>
        """
        GetDllLibDoc().AskFieldEventArgs_get_Field.argtypes=[c_void_p]
        GetDllLibDoc().AskFieldEventArgs_get_Field.restype=c_void_p
        intPtr = GetDllLibDoc().AskFieldEventArgs_get_Field(self.Ptr)
        ret = None if intPtr==None else Field(intPtr)
        return ret


    @property

    def PromptText(self)->str:
        """
    <summary>
        Gets the prompt text;
    </summary>
        """
        GetDllLibDoc().AskFieldEventArgs_get_PromptText.argtypes=[c_void_p]
        GetDllLibDoc().AskFieldEventArgs_get_PromptText.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().AskFieldEventArgs_get_PromptText(self.Ptr))
        return ret


    @property

    def DefaultResponse(self)->str:
        """
    <summary>
        Gets the default response.
    </summary>
        """
        GetDllLibDoc().AskFieldEventArgs_get_DefaultResponse.argtypes=[c_void_p]
        GetDllLibDoc().AskFieldEventArgs_get_DefaultResponse.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().AskFieldEventArgs_get_DefaultResponse(self.Ptr))
        return ret


    @property

    def ResponseText(self)->str:
        """
    <summary>
        Gets or sets the response text.
    </summary>
        """
        GetDllLibDoc().AskFieldEventArgs_get_ResponseText.argtypes=[c_void_p]
        GetDllLibDoc().AskFieldEventArgs_get_ResponseText.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().AskFieldEventArgs_get_ResponseText(self.Ptr))
        return ret


    @ResponseText.setter
    def ResponseText(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().AskFieldEventArgs_set_ResponseText.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().AskFieldEventArgs_set_ResponseText(self.Ptr, valuePtr)

    @property
    def Cancel(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether cancel to answer the question.
    </summary>
        """
        GetDllLibDoc().AskFieldEventArgs_get_Cancel.argtypes=[c_void_p]
        GetDllLibDoc().AskFieldEventArgs_get_Cancel.restype=c_bool
        ret = GetDllLibDoc().AskFieldEventArgs_get_Cancel(self.Ptr)
        return ret

    @Cancel.setter
    def Cancel(self, value:bool):
        GetDllLibDoc().AskFieldEventArgs_set_Cancel.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().AskFieldEventArgs_set_Cancel(self.Ptr, value)

    @property

    def BookmarkName(self)->str:
        """
    <summary>
        Gets the name of bookmark.
    </summary>
        """
        GetDllLibDoc().AskFieldEventArgs_get_BookmarkName.argtypes=[c_void_p]
        GetDllLibDoc().AskFieldEventArgs_get_BookmarkName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().AskFieldEventArgs_get_BookmarkName(self.Ptr))
        return ret


