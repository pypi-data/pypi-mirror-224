from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ControlField (  Field, IDocumentObject) :
    """

    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().ControlField_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().ControlField_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().ControlField_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

