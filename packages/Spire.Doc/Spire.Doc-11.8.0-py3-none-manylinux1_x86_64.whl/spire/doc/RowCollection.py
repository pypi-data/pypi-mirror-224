from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class RowCollection (  DocumentObjectCollection) :
    """

    """

    def get_Item(self ,index:int)->'TableRow':
        """

        """
        
        GetDllLibDoc().RowCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().RowCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().RowCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret



    def Add(self ,row:'TableRow')->int:
        """
    <summary>
        Adds a table row to collection.
    </summary>
    <param name="row">The row.</param>
    <returns></returns>
        """
        intPtrrow:c_void_p = row.Ptr

        GetDllLibDoc().RowCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().RowCollection_Add.restype=c_int
        ret = GetDllLibDoc().RowCollection_Add(self.Ptr, intPtrrow)
        return ret


    def Insert(self ,index:int,row:'TableRow'):
        """
    <summary>
        Inserts a table row into collection.
    </summary>
    <param name="index">The index.</param>
    <param name="row">The row.</param>
        """
        intPtrrow:c_void_p = row.Ptr

        GetDllLibDoc().RowCollection_Insert.argtypes=[c_void_p ,c_int,c_void_p]
        GetDllLibDoc().RowCollection_Insert(self.Ptr, index,intPtrrow)


    def IndexOf(self ,row:'TableRow')->int:
        """
    <summary>
        Returns index of a specified row in collection.
    </summary>
    <param name="row">The row.</param>
    <returns></returns>
        """
        intPtrrow:c_void_p = row.Ptr

        GetDllLibDoc().RowCollection_IndexOf.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().RowCollection_IndexOf.restype=c_int
        ret = GetDllLibDoc().RowCollection_IndexOf(self.Ptr, intPtrrow)
        return ret


    def Remove(self ,row:'TableRow'):
        """
    <summary>
        Removes a specified row.
    </summary>
    <param name="row">The row.</param>
        """
        intPtrrow:c_void_p = row.Ptr

        GetDllLibDoc().RowCollection_Remove.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().RowCollection_Remove(self.Ptr, intPtrrow)

