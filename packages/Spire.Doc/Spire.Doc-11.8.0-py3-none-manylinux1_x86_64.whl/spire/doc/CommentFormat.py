from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CommentFormat (  DocumentSerializable) :
    """

    """
    @property

    def DateTime(self)->'DateTime':
        """
    <summary>
        Gets or sets the DateTime.
    </summary>
<value>The DateTime.</value>
        """
        GetDllLibDoc().CommentFormat_get_DateTime.argtypes=[c_void_p]
        GetDllLibDoc().CommentFormat_get_DateTime.restype=c_void_p
        intPtr = GetDllLibDoc().CommentFormat_get_DateTime(self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @DateTime.setter
    def DateTime(self, value:'DateTime'):
        GetDllLibDoc().CommentFormat_set_DateTime.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().CommentFormat_set_DateTime(self.Ptr, value.Ptr)

    @property

    def Initial(self)->str:
        """
    <summary>
        Gets or sets the user initials.
    </summary>
<value>The user initials.</value>
        """
        GetDllLibDoc().CommentFormat_get_Initial.argtypes=[c_void_p]
        GetDllLibDoc().CommentFormat_get_Initial.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().CommentFormat_get_Initial(self.Ptr))
        return ret


    @Initial.setter
    def Initial(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().CommentFormat_set_Initial.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().CommentFormat_set_Initial(self.Ptr, valuePtr)

    @property

    def Author(self)->str:
        """
    <summary>
        Gets or sets the user.
    </summary>
<value>The user.</value>
        """
        GetDllLibDoc().CommentFormat_get_Author.argtypes=[c_void_p]
        GetDllLibDoc().CommentFormat_get_Author.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().CommentFormat_get_Author(self.Ptr))
        return ret


    @Author.setter
    def Author(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().CommentFormat_set_Author.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().CommentFormat_set_Author(self.Ptr, valuePtr)

    @property
    def CommentId(self)->int:
        """
    <summary>
        Gets or sets the id of the comment.
    </summary>
<value>The comment id.</value>
        """
        GetDllLibDoc().CommentFormat_get_CommentId.argtypes=[c_void_p]
        GetDllLibDoc().CommentFormat_get_CommentId.restype=c_int
        ret = GetDllLibDoc().CommentFormat_get_CommentId(self.Ptr)
        return ret

    @CommentId.setter
    def CommentId(self, value:int):
        GetDllLibDoc().CommentFormat_set_CommentId.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CommentFormat_set_CommentId(self.Ptr, value)


    def Clone(self ,doc:'IDocument')->'CommentFormat':
        """
    <summary>
        Creates a new object that is a copy of the current instance.
    </summary>
    <returns>
            A new object that is a copy of this instance.
            </returns>
        """
        intPtrdoc:c_void_p = doc.Ptr

        GetDllLibDoc().CommentFormat_Clone.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().CommentFormat_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().CommentFormat_Clone(self.Ptr, intPtrdoc)
        ret = None if intPtr==None else CommentFormat(intPtr)
        return ret


