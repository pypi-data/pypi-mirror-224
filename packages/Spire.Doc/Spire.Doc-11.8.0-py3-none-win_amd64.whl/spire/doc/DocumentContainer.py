from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentContainer (  DocumentBase) :
    """

    """
    @property
    def Count(self)->int:
        """
    <summary>
        Gets count of child object.
    </summary>
<value></value>
        """
        GetDllLibDoc().DocumentContainer_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().DocumentContainer_get_Count.restype=c_int
        ret = GetDllLibDoc().DocumentContainer_get_Count(self.Ptr)
        return ret


    def GetIndex(self ,entity:'IDocumentObject')->int:
        """

        """
        intPtrentity:c_void_p = entity.Ptr

        GetDllLibDoc().DocumentContainer_GetIndex.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().DocumentContainer_GetIndex.restype=c_int
        ret = GetDllLibDoc().DocumentContainer_GetIndex(self.Ptr, intPtrentity)
        return ret

