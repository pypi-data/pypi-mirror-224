from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ColumnCollection (  DocumentSerializableCollection) :
    """
    <summary>
        A collection of <see cref="T:Spire.Doc.Column" /> objects that 
            represent all the columns of text in a section of a document.
    </summary>
    """

    def get_Item(self ,index:int)->'Column':
        """
    <summary>
        Gets the <see cref="T:Spire.Doc.Column" /> at the specified index.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().ColumnCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ColumnCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().ColumnCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else Column(intPtr)
        return ret



    def Add(self ,column:'Column')->int:
        """
    <summary>
        Adds <see cref="T:Spire.Doc.Column" /> object to the collection.
    </summary>
    <param name="column">The column.</param>
    <returns></returns>
        """
        intPtrcolumn:c_void_p = column.Ptr

        GetDllLibDoc().ColumnCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ColumnCollection_Add.restype=c_int
        ret = GetDllLibDoc().ColumnCollection_Add(self.Ptr, intPtrcolumn)
        return ret


    def Populate(self ,count:int,spacing:float):
        """
    <summary>
        Populates the specified number of columns with specified spacing.
    </summary>
    <param name="count">The count.</param>
    <param name="spacing">The spacing.</param>
        """
        
        GetDllLibDoc().ColumnCollection_Populate.argtypes=[c_void_p ,c_int,c_float]
        GetDllLibDoc().ColumnCollection_Populate(self.Ptr, count,spacing)

    def Clear(self):
        """
    <summary>
        Removes all item.
    </summary>
        """
        GetDllLibDoc().ColumnCollection_Clear.argtypes=[c_void_p]
        GetDllLibDoc().ColumnCollection_Clear(self.Ptr)

