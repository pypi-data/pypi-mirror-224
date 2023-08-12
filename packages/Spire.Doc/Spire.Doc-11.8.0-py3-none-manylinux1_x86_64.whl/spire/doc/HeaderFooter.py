from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HeaderFooter (  Body, IDocumentObject) :
    """

    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
        """
        GetDllLibDoc().HeaderFooter_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().HeaderFooter_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().HeaderFooter_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def LinkToPrevious(self)->bool:
        """

        """
        GetDllLibDoc().HeaderFooter_get_LinkToPrevious.argtypes=[c_void_p]
        GetDllLibDoc().HeaderFooter_get_LinkToPrevious.restype=c_bool
        ret = GetDllLibDoc().HeaderFooter_get_LinkToPrevious(self.Ptr)
        return ret

    @LinkToPrevious.setter
    def LinkToPrevious(self, value:bool):
        GetDllLibDoc().HeaderFooter_set_LinkToPrevious.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().HeaderFooter_set_LinkToPrevious(self.Ptr, value)

