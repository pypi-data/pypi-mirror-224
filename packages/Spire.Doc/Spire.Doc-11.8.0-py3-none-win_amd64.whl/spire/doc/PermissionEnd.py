from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PermissionEnd (  ParagraphBase, IDocumentObject) :
    """

    """
    @dispatch
    def __init__(self, document:IDocument, idStr:str):
        idStrPtr = StrToPtr(idStr)
        intPdocument:c_void_p =  document.Ptr

        GetDllLibDoc().PermissionEnd_CreatePermissionEndDI.argtypes=[c_void_p,c_char_p]
        GetDllLibDoc().PermissionEnd_CreatePermissionEndDI.restype=c_void_p
        intPtr = GetDllLibDoc().PermissionEnd_CreatePermissionEndDI(intPdocument,idStrPtr)
        super(PermissionEnd, self).__init__(intPtr)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().PermissionEnd_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().PermissionEnd_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().PermissionEnd_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Id(self)->str:
        """
    <summary>
        Gets the permission id.
    </summary>
<value>The name.</value>
        """
        GetDllLibDoc().PermissionEnd_get_Id.argtypes=[c_void_p]
        GetDllLibDoc().PermissionEnd_get_Id.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().PermissionEnd_get_Id(self.Ptr))
        return ret


    @property

    def EditorGroup(self)->'EditingGroup':
        """
    <summary>
        Gets permission editorgroup.
    </summary>
        """
        GetDllLibDoc().PermissionEnd_get_EditorGroup.argtypes=[c_void_p]
        GetDllLibDoc().PermissionEnd_get_EditorGroup.restype=c_int
        ret = GetDllLibDoc().PermissionEnd_get_EditorGroup(self.Ptr)
        objwraped = EditingGroup(ret)
        return objwraped

    @EditorGroup.setter
    def EditorGroup(self, value:'EditingGroup'):
        GetDllLibDoc().PermissionEnd_set_EditorGroup.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PermissionEnd_set_EditorGroup(self.Ptr, value.value)

