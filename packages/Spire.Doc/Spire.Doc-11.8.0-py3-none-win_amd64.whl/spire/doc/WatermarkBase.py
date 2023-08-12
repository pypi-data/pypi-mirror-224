from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class WatermarkBase (  ParagraphBase, IDocumentObject) :
    """

    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
        """
        GetDllLibDoc().WatermarkBase_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().WatermarkBase_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().WatermarkBase_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Type(self)->'WatermarkType':
        """
    <summary>
        Gets the watermark type.
    </summary>
        """
        GetDllLibDoc().WatermarkBase_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().WatermarkBase_get_Type.restype=c_int
        ret = GetDllLibDoc().WatermarkBase_get_Type(self.Ptr)
        objwraped = WatermarkType(ret)
        return objwraped

