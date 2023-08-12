from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TableRow (  DocumentBase, ICompositeObject) :
    """

    """
    @dispatch
    def __init__(self, document:'IDocument'):
        intPdocument:c_void_p =  document.Ptr

        GetDllLibDoc().TableRow_CreateTableRowD.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_CreateTableRowD.restype=c_void_p
        intPtr = GetDllLibDoc().TableRow_CreateTableRowD(intPdocument)
        super(TableRow, self).__init__(intPtr)

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
    <summary>
        Gets the child object.
    </summary>
<value>The child object.</value>
        """
        GetDllLibDoc().TableRow_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().TableRow_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().TableRow_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().TableRow_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Cells(self)->'CellCollection':
        """
    <summary>
        Returns or sets cell collection.
    </summary>
        """
        GetDllLibDoc().TableRow_get_Cells.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_Cells.restype=c_void_p
        intPtr = GetDllLibDoc().TableRow_get_Cells(self.Ptr)
        from spire.doc import CellCollection
        ret = None if intPtr==None else CellCollection(intPtr)
        return ret


    @Cells.setter
    def Cells(self, value:'CellCollection'):
        GetDllLibDoc().TableRow_set_Cells.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().TableRow_set_Cells(self.Ptr, value.Ptr)

    @property

    def HeightType(self)->'TableRowHeightType':
        """
    <summary>
        Get / set table row height type
    </summary>
        """
        GetDllLibDoc().TableRow_get_HeightType.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_HeightType.restype=c_int
        ret = GetDllLibDoc().TableRow_get_HeightType(self.Ptr)
        objwraped = TableRowHeightType(ret)
        return objwraped

    @HeightType.setter
    def HeightType(self, value:'TableRowHeightType'):
        GetDllLibDoc().TableRow_set_HeightType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().TableRow_set_HeightType(self.Ptr, value.value)

    @property

    def RowFormat(self)->'RowFormat':
        """
    <summary>
        Gets table format
    </summary>
        """
        GetDllLibDoc().TableRow_get_RowFormat.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_RowFormat.restype=c_void_p
        intPtr = GetDllLibDoc().TableRow_get_RowFormat(self.Ptr)
        from spire.doc import RowFormat
        ret = None if intPtr==None else RowFormat(intPtr)
        return ret


    @property
    def Height(self)->float:
        """
    <summary>
        Returns or setsheight of the row.
    </summary>
        """
        GetDllLibDoc().TableRow_get_Height.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_Height.restype=c_float
        ret = GetDllLibDoc().TableRow_get_Height(self.Ptr)
        return ret

    @Height.setter
    def Height(self, value:float):
        GetDllLibDoc().TableRow_set_Height.argtypes=[c_void_p, c_float]
        GetDllLibDoc().TableRow_set_Height(self.Ptr, value)

    @property
    def IsHeader(self)->bool:
        """
    <summary>
        Returns or sets whether the row is a table header.
    </summary>
        """
        GetDllLibDoc().TableRow_get_IsHeader.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_IsHeader.restype=c_bool
        ret = GetDllLibDoc().TableRow_get_IsHeader(self.Ptr)
        return ret

    @IsHeader.setter
    def IsHeader(self, value:bool):
        GetDllLibDoc().TableRow_set_IsHeader.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().TableRow_set_IsHeader(self.Ptr, value)


    def Clone(self)->'TableRow':
        """
    <summary>
        Clones this instance.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().TableRow_Clone.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().TableRow_Clone(self.Ptr)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def AddCell(self)->TableCell:
        """
    <summary>
        Adds the cell.
    </summary>
        """
        GetDllLibDoc().TableRow_AddCell.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_AddCell.restype=c_void_p
        intPtr = GetDllLibDoc().TableRow_AddCell(self.Ptr)
        ret = None if intPtr==None else TableCell(intPtr)
        return ret


    @dispatch

    def AddCell(self ,isCopyFormat:bool)->TableCell:
        """
    <summary>
        Adds the cell.
    </summary>
    <param name="isCopyFormat">Specifies whether to apply the parent row format.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().TableRow_AddCellI.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().TableRow_AddCellI.restype=c_void_p
        intPtr = GetDllLibDoc().TableRow_AddCellI(self.Ptr, isCopyFormat)
        ret = None if intPtr==None else TableCell(intPtr)
        return ret


    def GetRowIndex(self)->int:
        """
    <summary>
        Returns index of the row in owner table.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().TableRow_GetRowIndex.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_GetRowIndex.restype=c_int
        ret = GetDllLibDoc().TableRow_GetRowIndex(self.Ptr)
        return ret

