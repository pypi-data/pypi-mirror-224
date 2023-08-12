from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBoxCollection (  CollectionEx) :
    """
    <summary>
        Summary description for TextBoxCollection.
    </summary>
    """

    def get_Item(self ,index:int)->'TextBox':
        """
    <summary>
        Gets the textbox at the specified index.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().TextBoxCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TextBoxCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().TextBoxCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else TextBox(intPtr)
        return ret



    def RemoveAt(self ,index:int):
        """
    <summary>
        Removes a textbox at the specified index.
    </summary>
    <param name="index">The index.</param>
        """
        
        GetDllLibDoc().TextBoxCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TextBoxCollection_RemoveAt(self.Ptr, index)

    def Clear(self):
        """
    <summary>
        Removes all textboxes from the document. 
    </summary>
        """
        GetDllLibDoc().TextBoxCollection_Clear.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxCollection_Clear(self.Ptr)

