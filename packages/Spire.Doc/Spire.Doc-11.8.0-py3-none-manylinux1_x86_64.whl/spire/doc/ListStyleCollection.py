from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListStyleCollection (  DocumentSerializableCollection) :
    """
    <summary>
        Represents a collection of list style
    </summary>
    """

    def get_Item(self ,index:int)->'ListStyle':
        """
    <summary>
        Gets the <see cref="!:Spire.Doc.ListStyle" /> at the specified index.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().ListStyleCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ListStyleCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().ListStyleCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else ListStyle(intPtr)
        return ret



    def Add(self ,style:'ListStyle')->int:
        """
    <summary>
        Adds the list style into collection.
    </summary>
    <param name="style">The style.</param>
    <returns></returns>
        """
        intPtrstyle:c_void_p = style.Ptr

        GetDllLibDoc().ListStyleCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ListStyleCollection_Add.restype=c_int
        ret = GetDllLibDoc().ListStyleCollection_Add(self.Ptr, intPtrstyle)
        return ret


    def FindByName(self ,name:str)->'ListStyle':
        """
    <summary>
        Finds list style by name.
    </summary>
    <param name="name">The name.</param>
    <returns></returns>
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().ListStyleCollection_FindByName.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().ListStyleCollection_FindByName.restype=c_void_p
        intPtr = GetDllLibDoc().ListStyleCollection_FindByName(self.Ptr, namePtr)
        ret = None if intPtr==None else ListStyle(intPtr)
        return ret


