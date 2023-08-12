from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PermissionCollection (  CollectionEx) :
    """
    <summary>
        A collection of <see cref="T:Spire.Doc.Permission" /> objects that 
            represent the permission in the document.
    </summary>
    """
    @dispatch

    def get_Item(self ,id:str)->Permission:
        """
    <summary>
        Gets the <see cref="T:Spire.Doc.Permission" /> with the specified id.
    </summary>
<value></value>
        """
        idPtr = StrToPtr(id)
        GetDllLibDoc().PermissionCollection_get_Item.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().PermissionCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().PermissionCollection_get_Item(self.Ptr, idPtr)
        ret = None if intPtr==None else Permission(intPtr)
        return ret


    @dispatch

    def get_Item(self ,index:int)->Permission:
        """
    <summary>
        Gets the <see cref="T:Spire.Doc.Permission" /> at the specified index.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().PermissionCollection_get_ItemI.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().PermissionCollection_get_ItemI.restype=c_void_p
        intPtr = GetDllLibDoc().PermissionCollection_get_ItemI(self.Ptr, index)
        ret = None if intPtr==None else Permission(intPtr)
        return ret



    def FindById(self ,id:str)->'Permission':
        """
    <summary>
        Finds <see cref="T:Spire.Doc.Permission" /> object by specified id
    </summary>
    <param name="name">The Permission id</param>
    <returns></returns>
        """
        idPtr = StrToPtr(id)
        GetDllLibDoc().PermissionCollection_FindById.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().PermissionCollection_FindById.restype=c_void_p
        intPtr = GetDllLibDoc().PermissionCollection_FindById(self.Ptr, idPtr)
        ret = None if intPtr==None else Permission(intPtr)
        return ret



    def RemoveAt(self ,index:int):
        """
    <summary>
        Removes a permission at the specified index.
    </summary>
    <param name="index">The index.</param>
        """
        
        GetDllLibDoc().PermissionCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().PermissionCollection_RemoveAt(self.Ptr, index)


    def Remove(self ,permission:'Permission'):
        """
    <summary>
        Removes the specified permission.
    </summary>
    <param name="permission">The permission.</param>
        """
        intPtrpermission:c_void_p = permission.Ptr

        GetDllLibDoc().PermissionCollection_Remove.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().PermissionCollection_Remove(self.Ptr, intPtrpermission)

    def Clear(self):
        """
    <summary>
        Removes all permissions from the document. 
    </summary>
        """
        GetDllLibDoc().PermissionCollection_Clear.argtypes=[c_void_p]
        GetDllLibDoc().PermissionCollection_Clear(self.Ptr)

