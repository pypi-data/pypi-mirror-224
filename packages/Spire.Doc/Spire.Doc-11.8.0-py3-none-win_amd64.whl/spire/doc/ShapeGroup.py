from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ShapeGroup (  ShapeBase, IDocumentObject) :
    """

    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """

        """
        GetDllLibDoc().ShapeGroup_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().ShapeGroup_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().ShapeGroup_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

