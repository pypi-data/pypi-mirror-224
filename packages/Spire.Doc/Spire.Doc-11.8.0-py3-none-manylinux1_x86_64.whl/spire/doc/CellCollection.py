from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CellCollection (  DocumentObjectCollection) :
    """
    <summary>
        Represents a collection of <see cref="T:Spire.Doc.TableCell" /> objects.
    </summary>
    """

    def get_Item(self ,index:int)->'TableCell':
        """

        """
        
        GetDllLibDoc().CellCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().CellCollection_get_Item.restype=IntPtrWithTypeName
        intPtr = GetDllLibDoc().CellCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else self._create(intPtr)
        return ret


    def _create(self, intPtrWithTypeName:IntPtrWithTypeName)->'TableCell':
        ret= None
        if intPtrWithTypeName == None :
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Documents.StructureDocumentTagCell"):
            ret = StructureDocumentTagCell(intPtr)
        else:
            ret = TableCell(intPtr)
        return ret


    def Add(self ,cell:'TableCell')->int:
        """
    <summary>
        Adds the specified cell.
    </summary>
    <param name="cell">The cell.</param>
    <returns></returns>
        """
        intPtrcell:c_void_p = cell.Ptr

        GetDllLibDoc().CellCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().CellCollection_Add.restype=c_int
        ret = GetDllLibDoc().CellCollection_Add(self.Ptr, intPtrcell)
        return ret


    def Insert(self ,index:int,cell:'TableCell'):
        """
    <summary>
        Inserts a specified table cell into collection.
    </summary>
    <param name="index">The index.</param>
    <param name="cell">The cell.</param>
        """
        intPtrcell:c_void_p = cell.Ptr

        GetDllLibDoc().CellCollection_Insert.argtypes=[c_void_p ,c_int,c_void_p]
        GetDllLibDoc().CellCollection_Insert(self.Ptr, index,intPtrcell)


    def IndexOf(self ,cell:'TableCell')->int:
        """
    <summary>
        Returns index of a specified cell in collection.
    </summary>
    <param name="cell">The cell.</param>
    <returns></returns>
        """
        intPtrcell:c_void_p = cell.Ptr

        GetDllLibDoc().CellCollection_IndexOf.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().CellCollection_IndexOf.restype=c_int
        ret = GetDllLibDoc().CellCollection_IndexOf(self.Ptr, intPtrcell)
        return ret


    def Remove(self ,cell:'TableCell'):
        """
    <summary>
        Removes the specified cell.
    </summary>
    <param name="cell">The cell.</param>
        """
        intPtrcell:c_void_p = cell.Ptr

        GetDllLibDoc().CellCollection_Remove.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().CellCollection_Remove(self.Ptr, intPtrcell)


    def RemoveAt(self ,index:int):
        """
    <summary>
        Removes the document object at the specified index from the collection.
    </summary>
    <param name="index">The index.</param>
        """
        
        GetDllLibDoc().CellCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().CellCollection_RemoveAt(self.Ptr, index)

