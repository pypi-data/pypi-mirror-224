from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BookmarkEnd (  ParagraphBase, IDocumentObject) :
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
        GetDllLibDoc().BookmarkEnd_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().BookmarkEnd_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().BookmarkEnd_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Name(self)->str:
        """
    <summary>
        Gets the bookmark name.
    </summary>
<value>The name.</value>
        """
        GetDllLibDoc().BookmarkEnd_get_Name.argtypes=[c_void_p]
        GetDllLibDoc().BookmarkEnd_get_Name.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().BookmarkEnd_get_Name(self.Ptr))
        return ret


