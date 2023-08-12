from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TableCell (  Body, IDocumentObject) :
    """

    """
    @dispatch
    def __init__(self, document:'IDocument'):
        intPdocument:c_void_p = document.Ptr

        GetDllLibDoc().TableCell_CreateTableCellD.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_CreateTableCellD.restype=c_void_p
        intPtr = GetDllLibDoc().TableCell_CreateTableCellD(intPdocument)
        super(TableCell, self).__init__(intPtr)

    @property

    def GridSpan(self)->int:
        """

        """
        GetDllLibDoc().TableCell_get_GridSpan.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_GridSpan.restype=c_void_p
        intPtr = GetDllLibDoc().TableCell_get_GridSpan(self.Ptr)
        return intPtr


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """

        """
        GetDllLibDoc().TableCell_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().TableCell_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def OwnerRow(self)->'TableRow':
        """
    <summary>
        Gets owner row of the cell.
    </summary>
        """
        GetDllLibDoc().TableCell_get_OwnerRow.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_OwnerRow.restype=c_void_p
        intPtr = GetDllLibDoc().TableCell_get_OwnerRow(self.Ptr)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @property

    def CellFormat(self)->'CellFormat':
        """
    <summary>
        Gets cell format.
    </summary>
        """
        GetDllLibDoc().TableCell_get_CellFormat.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_CellFormat.restype=c_void_p
        intPtr = GetDllLibDoc().TableCell_get_CellFormat(self.Ptr)
        from spire.doc import CellFormat
        ret = None if intPtr==None else CellFormat(intPtr)
        return ret


    @property
    def Width(self)->float:
        """
    <summary>
        Gets the width of the cell.
    </summary>
        """
        GetDllLibDoc().TableCell_get_Width.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_Width.restype=c_float
        ret = GetDllLibDoc().TableCell_get_Width(self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:float):
        GetDllLibDoc().TableCell_set_Width.argtypes=[c_void_p, c_float]
        GetDllLibDoc().TableCell_set_Width(self.Ptr, value)

    @property

    def CellWidthType(self)->'CellWidthType':
        """
    <summary>
        Gets the width type of the cell.
    </summary>
        """
        GetDllLibDoc().TableCell_get_CellWidthType.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_CellWidthType.restype=c_int
        ret = GetDllLibDoc().TableCell_get_CellWidthType(self.Ptr)
        objwraped = CellWidthType(ret)
        return objwraped

    @CellWidthType.setter
    def CellWidthType(self, value:'CellWidthType'):
        GetDllLibDoc().TableCell_set_CellWidthType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().TableCell_set_CellWidthType(self.Ptr, value.value)

    @property
    def Scaling(self)->float:
        """
    <summary>
        Gets or sets the cell scaling.
    </summary>
<value>The scaling.</value>
        """
        GetDllLibDoc().TableCell_get_Scaling.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_Scaling.restype=c_float
        ret = GetDllLibDoc().TableCell_get_Scaling(self.Ptr)
        return ret

    @Scaling.setter
    def Scaling(self, value:float):
        GetDllLibDoc().TableCell_set_Scaling.argtypes=[c_void_p, c_float]
        GetDllLibDoc().TableCell_set_Scaling(self.Ptr, value)


    def Clone(self)->'DocumentObject':
        """

        """
        GetDllLibDoc().TableCell_Clone.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().TableCell_Clone(self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


    def GetCellIndex(self)->int:
        """

        """
        GetDllLibDoc().TableCell_GetCellIndex.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_GetCellIndex.restype=c_int
        ret = GetDllLibDoc().TableCell_GetCellIndex(self.Ptr)
        return ret


    def SetCellWidth(self ,width:float,widthType:'CellWidthType'):
        """
    <summary>
        Set the width and type of the cell.
    </summary>
    <param name="width">Width of the cell.</param>
    <param name="widthType">Width type of the cell.</param>
        """
        enumwidthType:c_int = widthType.value

        GetDllLibDoc().TableCell_SetCellWidth.argtypes=[c_void_p ,c_float,c_int]
        GetDllLibDoc().TableCell_SetCellWidth(self.Ptr, width,enumwidthType)

    def GetCellWidth(self)->float:
        """
    <summary>
        Gets the width of the cell.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().TableCell_GetCellWidth.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_GetCellWidth.restype=c_float
        ret = GetDllLibDoc().TableCell_GetCellWidth(self.Ptr)
        return ret


    def GetCellWidthType(self)->'CellWidthType':
        """
    <summary>
        Gets the width type of the cell.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().TableCell_GetCellWidthType.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_GetCellWidthType.restype=c_int
        ret = GetDllLibDoc().TableCell_GetCellWidthType(self.Ptr)
        objwraped = CellWidthType(ret)
        return objwraped


    def SplitCell(self ,columnNum:int,rowNum:int):
        """
    <summary>
        The one cell splits into two or more cells.
    </summary>
    <param name="columnNum">The split column number. Must be greater than or equal to 1 is only valid. </param>
    <param name="rowNum">The split row number. Must be greater than or equal to 1 is only valid. </param>
        """
        
        GetDllLibDoc().TableCell_SplitCell.argtypes=[c_void_p ,c_int,c_int]
        GetDllLibDoc().TableCell_SplitCell(self.Ptr, columnNum,rowNum)

