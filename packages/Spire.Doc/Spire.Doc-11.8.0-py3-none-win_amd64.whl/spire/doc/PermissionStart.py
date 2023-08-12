from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PermissionStart (  ParagraphBase, IDocumentObject) :
    """

    """
    @dispatch
    def __init__(self, doc:IDocument, idStr:str):
        idStrPtr = StrToPtr(idStr)
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().PermissionStart_CreatePermissionStartDI.argtypes=[c_void_p,c_char_p]
        GetDllLibDoc().PermissionStart_CreatePermissionStartDI.restype=c_void_p
        intPtr = GetDllLibDoc().PermissionStart_CreatePermissionStartDI(intPdoc,idStrPtr)
        super(PermissionStart, self).__init__(intPtr)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().PermissionStart_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().PermissionStart_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().PermissionStart_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Id(self)->str:
        """
    <summary>
        Gets the permissionstart id.
    </summary>
        """
        GetDllLibDoc().PermissionStart_get_Id.argtypes=[c_void_p]
        GetDllLibDoc().PermissionStart_get_Id.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().PermissionStart_get_Id(self.Ptr))
        return ret


    @property

    def EditorGroup(self)->'EditingGroup':
        """
    <summary>
        Gets permission editorgroup.
    </summary>
        """
        GetDllLibDoc().PermissionStart_get_EditorGroup.argtypes=[c_void_p]
        GetDllLibDoc().PermissionStart_get_EditorGroup.restype=c_int
        ret = GetDllLibDoc().PermissionStart_get_EditorGroup(self.Ptr)
        objwraped = EditingGroup(ret)
        return objwraped

    @EditorGroup.setter
    def EditorGroup(self, value:'EditingGroup'):
        GetDllLibDoc().PermissionStart_set_EditorGroup.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PermissionStart_set_EditorGroup(self.Ptr, value.value)

