from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CustomDocumentProperties (  DocumentSerializable) :
    """

    """
#    @property
#
#    def CustomHash(self)->'Dictionary2':
#        """
#
#        """
#        GetDllLibDoc().CustomDocumentProperties_get_CustomHash.argtypes=[c_void_p]
#        GetDllLibDoc().CustomDocumentProperties_get_CustomHash.restype=c_void_p
#        intPtr = GetDllLibDoc().CustomDocumentProperties_get_CustomHash(self.Ptr)
#        ret = None if intPtr==None else Dictionary2(intPtr)
#        return ret
#


    @dispatch

    def get_Item(self ,name:str)->DocumentProperty:
        """
    <summary>
        Gets or sets property by specified name.
    </summary>
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().CustomDocumentProperties_get_Item.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().CustomDocumentProperties_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().CustomDocumentProperties_get_Item(self.Ptr, namePtr)
        ret = None if intPtr==None else DocumentProperty(intPtr)
        return ret


    @dispatch

    def get_Item(self ,index:int)->DocumentProperty:
        """
    <summary>
        Gets or sets property by specified index.
    </summary>
        """
        
        GetDllLibDoc().CustomDocumentProperties_get_ItemI.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().CustomDocumentProperties_get_ItemI.restype=c_void_p
        intPtr = GetDllLibDoc().CustomDocumentProperties_get_ItemI(self.Ptr, index)
        ret = None if intPtr==None else DocumentProperty(intPtr)
        return ret


    @property
    def Count(self)->int:
        """
    <summary>
        Gets count of the properties.
    </summary>
        """
        GetDllLibDoc().CustomDocumentProperties_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().CustomDocumentProperties_get_Count.restype=c_int
        ret = GetDllLibDoc().CustomDocumentProperties_get_Count(self.Ptr)
        return ret


    def Add(self ,name:str,value:'SpireObject')->'DocumentProperty':
        """
    <summary>
        Adds the specified name.
    </summary>
    <param name="name">The name.</param>
    <param name="value">The value.</param>
    <returns></returns>
        """
        namePtr = StrToPtr(name)
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().CustomDocumentProperties_Add.argtypes=[c_void_p ,c_char_p,c_void_p]
        GetDllLibDoc().CustomDocumentProperties_Add.restype=c_void_p
        intPtr = GetDllLibDoc().CustomDocumentProperties_Add(self.Ptr, namePtr,intPtrvalue)
        ret = None if intPtr==None else DocumentProperty(intPtr)
        return ret



    def Remove(self ,name:str):
        """
    <summary>
        Remove property specified by name.
    </summary>
    <param name="name">The name.</param>
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().CustomDocumentProperties_Remove.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().CustomDocumentProperties_Remove(self.Ptr, namePtr)


    def Clone(self)->'CustomDocumentProperties':
        """
    <summary>
        Clones this instance.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().CustomDocumentProperties_Clone.argtypes=[c_void_p]
        GetDllLibDoc().CustomDocumentProperties_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().CustomDocumentProperties_Clone(self.Ptr)
        ret = None if intPtr==None else CustomDocumentProperties(intPtr)
        return ret


