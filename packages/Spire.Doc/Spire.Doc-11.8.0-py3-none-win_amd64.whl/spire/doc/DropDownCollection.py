from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DropDownCollection (  DocumentSerializableCollection) :
    """
    <summary>
        Represent a collection of <see cref="!:Spire.Doc.DropDownItem" /> objects.
    </summary>
    """

    def get_Item(self ,index:int)->'DropDownItem':
        """
    <summary>
        Gets the <see cref="!:Spire.Doc.DropDownItem" /> at the specified index.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().DropDownCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().DropDownCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().DropDownCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else DropDownItem(intPtr)
        return ret



    def Add(self ,text:str)->'DropDownItem':
        """
    <summary>
        Adds the item.
    </summary>
    <param name="text">The text.</param>
    <returns></returns>
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().DropDownCollection_Add.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().DropDownCollection_Add.restype=c_void_p
        intPtr = GetDllLibDoc().DropDownCollection_Add(self.Ptr, textPtr)
        from spire.doc import DropDownItem
        ret = None if intPtr==None else DropDownItem(intPtr)
        return ret



    def Remove(self ,index:int):
        """
    <summary>
        Removes DropDownItems by index.
    </summary>
    <param name="index">The index.</param>
        """
        
        GetDllLibDoc().DropDownCollection_Remove.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().DropDownCollection_Remove(self.Ptr, index)

    def Clear(self):
        """
    <summary>
        Clears this instance.
    </summary>
        """
        GetDllLibDoc().DropDownCollection_Clear.argtypes=[c_void_p]
        GetDllLibDoc().DropDownCollection_Clear(self.Ptr)

