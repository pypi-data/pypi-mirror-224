from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBoxItemCollection (  DocumentObjectCollection, ITextBoxItemCollection) :
    """
    <summary>
        Represents a collection of <see cref="!:Spire.Doc.TextBox" /> objects.
    </summary>
    """

    def get_Item(self ,index:int)->'ITextBox':
        """

        """
        
        GetDllLibDoc().TextBoxItemCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TextBoxItemCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().TextBoxItemCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else ITextBox(intPtr)
        return ret



    def Add(self ,textBox:'ITextBox')->int:
        """
    <summary>
        Adds a textbox to the collection.
    </summary>
    <param name="textBox">The text box.</param>
    <returns></returns>
        """
        intPtrtextBox:c_void_p = textBox.Ptr

        GetDllLibDoc().TextBoxItemCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TextBoxItemCollection_Add.restype=c_int
        ret = GetDllLibDoc().TextBoxItemCollection_Add(self.Ptr, intPtrtextBox)
        return ret

