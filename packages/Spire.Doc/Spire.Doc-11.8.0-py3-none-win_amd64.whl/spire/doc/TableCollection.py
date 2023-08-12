from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TableCollection (  DocumentSubsetCollection, ITableCollection) :
    """
    <summary>
        Represents a collection of <see cref="!:Spire.Doc.ITable" /> objects.
    </summary>
    """

    def get_Item(self ,index:int)->'ITable':
        """

        """
        
        GetDllLibDoc().TableCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TableCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().TableCollection_get_Item(self.Ptr, index)
        #ret = None if intPtr==None else ITable(intPtr)
        ret = None if intPtr==None else Table(intPtr)
        return ret



    def Add(self ,table:'ITable')->int:
        """
    <summary>
        Adds a table to end of text body.
    </summary>
    <param name="table">The table.</param>
    <returns></returns>
        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().TableCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TableCollection_Add.restype=c_int
        ret = GetDllLibDoc().TableCollection_Add(self.Ptr, intPtrtable)
        return ret


    def Contains(self ,table:'ITable')->bool:
        """
    <summary>
        Determines whether the <see cref="!:Spire.Doc.ITableCollection" /> contains a specific value.
    </summary>
    <param name="table">The table.</param>
    <returns>
            	If table found, set to <c>true</c>.
            </returns>
        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().TableCollection_Contains.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TableCollection_Contains.restype=c_bool
        ret = GetDllLibDoc().TableCollection_Contains(self.Ptr, intPtrtable)
        return ret


    def IndexOf(self ,table:'ITable')->int:
        """
    <summary>
        Determines the index of a specific item in the <see cref="!:Spire.Doc.ITableCollection" />.
    </summary>
    <param name="table">The table.</param>
    <returns></returns>
        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().TableCollection_IndexOf.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TableCollection_IndexOf.restype=c_int
        ret = GetDllLibDoc().TableCollection_IndexOf(self.Ptr, intPtrtable)
        return ret


    def Insert(self ,index:int,table:'ITable')->int:
        """
    <summary>
        Inserts a table into collection at the specified index.
    </summary>
    <param name="index">The index.</param>
    <param name="table">The table.</param>
    <returns></returns>
        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().TableCollection_Insert.argtypes=[c_void_p ,c_int,c_void_p]
        GetDllLibDoc().TableCollection_Insert.restype=c_int
        ret = GetDllLibDoc().TableCollection_Insert(self.Ptr, index,intPtrtable)
        return ret


    def Remove(self ,table:'ITable'):
        """
    <summary>
        Removes the specified table.
    </summary>
    <param name="table">The table.</param>
        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().TableCollection_Remove.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TableCollection_Remove(self.Ptr, intPtrtable)


    def RemoveAt(self ,index:int):
        """
    <summary>
        Removes the table at the specified index from the collection.
    </summary>
    <param name="index">The index.</param>
        """
        
        GetDllLibDoc().TableCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TableCollection_RemoveAt(self.Ptr, index)

