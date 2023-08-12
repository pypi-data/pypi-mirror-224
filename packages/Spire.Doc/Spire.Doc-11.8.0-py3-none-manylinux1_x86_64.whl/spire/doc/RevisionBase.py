from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class RevisionBase (SpireObject) :
    """

    """
    @property

    def Author(self)->str:
        """
    <summary>
        Gets the author.
            Specifies the author for an annotation within a Word document.
    </summary>
        """
        GetDllLibDoc().RevisionBase_get_Author.argtypes=[c_void_p]
        GetDllLibDoc().RevisionBase_get_Author.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().RevisionBase_get_Author(self.Ptr))
        return ret


    @property

    def DateTime(self)->'DateTime':
        """
    <summary>
        Gets the date time.
            Specifies the date information for an annotation within a Word document.
    </summary>
        """
        GetDllLibDoc().RevisionBase_get_DateTime.argtypes=[c_void_p]
        GetDllLibDoc().RevisionBase_get_DateTime.restype=c_void_p
        intPtr = GetDllLibDoc().RevisionBase_get_DateTime(self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @DateTime.setter
    def DateTime(self, value:'DateTime'):
        GetDllLibDoc().RevisionBase_set_DateTime.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().RevisionBase_set_DateTime(self.Ptr, value.Ptr)

