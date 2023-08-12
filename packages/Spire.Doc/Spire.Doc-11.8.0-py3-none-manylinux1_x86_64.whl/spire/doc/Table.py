from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Table (  BodyRegion, IBodyRegion, ITable, ICompositeObject) :
    """

    """
    @dispatch
    def __init__(self, doc:'IDocument'):
		
       intPdoc:c_void_p = doc.Ptr

       GetDllLibDoc().Table_CreateTableD.argtypes=[c_void_p]
       GetDllLibDoc().Table_CreateTableD.restype=c_void_p
       intPtr = GetDllLibDoc().Table_CreateTableD(intPdoc)
       super(Table, self).__init__(intPtr)
			
    @dispatch
    def __init__(self, doc:'IDocument', showBorder:bool):
		
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().Table_CreateTableDS.argtypes=[c_void_p,c_bool]
        GetDllLibDoc().Table_CreateTableDS.restype=c_void_p
        intPtr = GetDllLibDoc().Table_CreateTableDS(intPdoc,showBorder)
        super(Table, self).__init__(intPtr)
    @dispatch
    def __init__(self, doc:'IDocument', showBorder:bool, lineWidth:float):
		
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().Table_CreateTableDSL.argtypes=[c_void_p,c_bool,c_float]
        GetDllLibDoc().Table_CreateTableDSL.restype=c_void_p
        intPtr = GetDllLibDoc().Table_CreateTableDSL(intPdoc,showBorder,lineWidth)
        super(Table, self).__init__(intPtr)

		
    @property
    def DefaultRowHeight(self)->float:
        """
    <summary>
        Gets or sets the default row height, the unit of measure is point, 1point = 0.3528 mm
    </summary>
        """
        GetDllLibDoc().Table_get_DefaultRowHeight.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_DefaultRowHeight.restype=c_float
        ret = GetDllLibDoc().Table_get_DefaultRowHeight(self.Ptr)
        return ret

    @DefaultRowHeight.setter
    def DefaultRowHeight(self, value:float):
        GetDllLibDoc().Table_set_DefaultRowHeight.argtypes=[c_void_p, c_float]
        GetDllLibDoc().Table_set_DefaultRowHeight(self.Ptr, value)

    @property
    def DefaultColumnsNumber(self)->int:
        """

        """
        GetDllLibDoc().Table_get_DefaultColumnsNumber.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_DefaultColumnsNumber.restype=c_int
        ret = GetDllLibDoc().Table_get_DefaultColumnsNumber(self.Ptr)
        return ret

    @DefaultColumnsNumber.setter
    def DefaultColumnsNumber(self, value:int):
        GetDllLibDoc().Table_set_DefaultColumnsNumber.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Table_set_DefaultColumnsNumber(self.Ptr, value)

    @property
    def DefaultColumnWidth(self)->float:
        """
    <summary>
        Gets or sets the default width of each column.
    </summary>
        """
        GetDllLibDoc().Table_get_DefaultColumnWidth.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_DefaultColumnWidth.restype=c_float
        ret = GetDllLibDoc().Table_get_DefaultColumnWidth(self.Ptr)
        return ret

    @DefaultColumnWidth.setter
    def DefaultColumnWidth(self, value:float):
        GetDllLibDoc().Table_set_DefaultColumnWidth.argtypes=[c_void_p, c_float]
        GetDllLibDoc().Table_set_DefaultColumnWidth(self.Ptr, value)

    @property

    def ColumnWidth(self)->List[float]:
        """
    <summary>
        Gets or sets the width of each column. 
    </summary>
        """
        GetDllLibDoc().Table_get_ColumnWidth.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_ColumnWidth.restype=IntPtrArray
        intPtrArray = GetDllLibDoc().Table_get_ColumnWidth(self.Ptr)
        ret = GetVectorFromArray(intPtrArray, c_float)
        return ret

    @ColumnWidth.setter
    def ColumnWidth(self, value:List[float]):
        vCount = len(value)
        ArrayType = c_float * vCount
        vArray = ArrayType()
        for i in range(0, vCount):
            vArray[i] = value[i]
        GetDllLibDoc().Table_set_ColumnWidth.argtypes=[c_void_p, ArrayType, c_int]
        GetDllLibDoc().Table_set_ColumnWidth(self.Ptr, vArray, vCount)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
        """
        GetDllLibDoc().Table_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().Table_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Rows(self)->'RowCollection':
        """
    <summary>
        Get the table rows
    </summary>
<value></value>
        """
        GetDllLibDoc().Table_get_Rows.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_Rows.restype=c_void_p
        intPtr = GetDllLibDoc().Table_get_Rows(self.Ptr)
        from spire.doc import RowCollection
        ret = None if intPtr==None else RowCollection(intPtr)
        return ret


    @property

    def TableFormat(self)->'RowFormat':
        """
    <summary>
        Gets the table formatting after ResetCells call.
    </summary>
<value>The table format.</value>
        """
        GetDllLibDoc().Table_get_TableFormat.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_TableFormat.restype=c_void_p
        intPtr = GetDllLibDoc().Table_get_TableFormat(self.Ptr)
        ret = None if intPtr==None else RowFormat(intPtr)
        return ret


    @property

    def PreferredWidth(self)->'PreferredWidth':
        """
    <summary>
        This property specifies the preferred horizontal width of a table.
    </summary>
        """
        GetDllLibDoc().Table_get_PreferredWidth.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_PreferredWidth.restype=c_void_p
        intPtr = GetDllLibDoc().Table_get_PreferredWidth(self.Ptr)
        ret = None if intPtr==None else PreferredWidth(intPtr)
        return ret


    @PreferredWidth.setter
    def PreferredWidth(self, value:'PreferredWidth'):
        GetDllLibDoc().Table_set_PreferredWidth.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().Table_set_PreferredWidth(self.Ptr, value.Ptr)

    @property

    def TableStyleName(self)->str:
        """
    <summary>
        Gets table style name.
    </summary>
<value></value>
        """
        GetDllLibDoc().Table_get_TableStyleName.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_TableStyleName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Table_get_TableStyleName(self.Ptr))
        return ret


    @property

    def LastCell(self)->'TableCell':
        """
    <summary>
        Get last cell of the table
    </summary>
<value></value>
        """
        GetDllLibDoc().Table_get_LastCell.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_LastCell.restype=c_void_p
        intPtr = GetDllLibDoc().Table_get_LastCell(self.Ptr)
        ret = None if intPtr==None else TableCell(intPtr)
        return ret


    @property

    def FirstRow(self)->'TableRow':
        """
    <summary>
        Get first row of the table.
    </summary>
<value></value>
        """
        GetDllLibDoc().Table_get_FirstRow.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_FirstRow.restype=c_void_p
        intPtr = GetDllLibDoc().Table_get_FirstRow(self.Ptr)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @property

    def LastRow(self)->'TableRow':
        """
    <summary>
        Get last row of the table.
    </summary>
<value></value>
        """
        GetDllLibDoc().Table_get_LastRow.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_LastRow.restype=c_void_p
        intPtr = GetDllLibDoc().Table_get_LastRow(self.Ptr)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret



    def get_Item(self ,row:int,column:int)->'TableCell':
        """
    <summary>
        Get table cell by row and column indexes.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().Table_get_Item.argtypes=[c_void_p ,c_int,c_int]
        GetDllLibDoc().Table_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().Table_get_Item(self.Ptr, row,column)
        ret = None if intPtr==None else TableCell(intPtr)
        return ret


    @property
    def Width(self)->float:
        """
    <summary>
        Gets the table width
    </summary>
<value></value>
        """
        GetDllLibDoc().Table_get_Width.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_Width.restype=c_float
        ret = GetDllLibDoc().Table_get_Width(self.Ptr)
        return ret

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
    <summary>
        Gets the child entities.
    </summary>
<value>The child entities.</value>
        """
        GetDllLibDoc().Table_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().Table_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property
    def IndentFromLeft(self)->float:
        """
    <summary>
        Gets or sets indent from left for the table.
    </summary>
        """
        GetDllLibDoc().Table_get_IndentFromLeft.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_IndentFromLeft.restype=c_float
        ret = GetDllLibDoc().Table_get_IndentFromLeft(self.Ptr)
        return ret

    @IndentFromLeft.setter
    def IndentFromLeft(self, value:float):
        GetDllLibDoc().Table_set_IndentFromLeft.argtypes=[c_void_p, c_float]
        GetDllLibDoc().Table_set_IndentFromLeft(self.Ptr, value)

    @property

    def Title(self)->str:
        """
    <summary>
        Gets or sets the table title.
    </summary>
<value>The title.</value>
        """
        GetDllLibDoc().Table_get_Title.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_Title.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Table_get_Title(self.Ptr))
        return ret


    @Title.setter
    def Title(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Table_set_Title.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Table_set_Title(self.Ptr, valuePtr)

    @property

    def TableDescription(self)->str:
        """
    <summary>
        Gets or sets the table description.
    </summary>
        """
        GetDllLibDoc().Table_get_TableDescription.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_TableDescription.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Table_get_TableDescription(self.Ptr))
        return ret


    @TableDescription.setter
    def TableDescription(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Table_set_TableDescription.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Table_set_TableDescription(self.Ptr, valuePtr)


    def AddCaption(self ,name:str,format:'CaptionNumberingFormat',captionPosition:'CaptionPosition')->'IParagraph':
        """
    <summary>
        Add Caption for current Table
    </summary>
    <param name="captionPosition"></param>
    <param name="name"></param>
    <param name="format"></param>
    <returns></returns>
        """
        namePtr = StrToPtr(name)
        enumformat:c_int = format.value
        enumcaptionPosition:c_int = captionPosition.value

        GetDllLibDoc().Table_AddCaption.argtypes=[c_void_p ,c_char_p,c_int,c_int]
        GetDllLibDoc().Table_AddCaption.restype=c_void_p
        intPtr = GetDllLibDoc().Table_AddCaption(self.Ptr, namePtr,enumformat,enumcaptionPosition)
        #ret = None if intPtr==None else IParagraph(intPtr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret



    def Clone(self)->'Table':
        """
    <summary>
        Clones this instance.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Table_Clone.argtypes=[c_void_p]
        GetDllLibDoc().Table_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().Table_Clone(self.Ptr)
        ret = None if intPtr==None else Table(intPtr)
        return ret


    @dispatch

    def ResetCells(self ,rowsNum:int,columnsNum:int):
        """
    <summary>
        Resets rows / columns numbers.
    </summary>
    <param name="rowsNum">The rows number.</param>
    <param name="columnsNum">The columns number.</param>
        """
        
        GetDllLibDoc().Table_ResetCells.argtypes=[c_void_p ,c_int,c_int]
        GetDllLibDoc().Table_ResetCells(self.Ptr, rowsNum,columnsNum)

    @dispatch

    def ResetCells(self ,rowsNum:int,columnsNum:int,format:RowFormat,cellWidth:float):
        """
    <summary>
        Resets rows / columns numbers.
    </summary>
    <param name="rowsNum">The rows num.</param>
    <param name="columnsNum">The columns num.</param>
    <param name="format"></param>
    <param name="cellWidth">Width of the cell.</param>
        """
        intPtrformat:c_void_p = format.Ptr

        GetDllLibDoc().Table_ResetCellsRCFC.argtypes=[c_void_p ,c_int,c_int,c_void_p,c_float]
        GetDllLibDoc().Table_ResetCellsRCFC(self.Ptr, rowsNum,columnsNum,intPtrformat,cellWidth)


    def ApplyStyle(self ,builtinTableStyle:'DefaultTableStyle'):
        """
    <summary>
        Applies the built-in table style.
    </summary>
    <param name="builtinStyle">The built-in table style.</param>
        """
        enumbuiltinTableStyle:c_int = builtinTableStyle.value

        GetDllLibDoc().Table_ApplyStyle.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Table_ApplyStyle(self.Ptr, enumbuiltinTableStyle)

    def ApplyTableStyle(self):
        """
    <summary>
        Applies the table style properties to table and cell.
    </summary>
        """
        GetDllLibDoc().Table_ApplyTableStyle.argtypes=[c_void_p]
        GetDllLibDoc().Table_ApplyTableStyle(self.Ptr)

    @dispatch

    def AddRow(self)->TableRow:
        """
    <summary>
        Adds a row to table
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Table_AddRow.argtypes=[c_void_p]
        GetDllLibDoc().Table_AddRow.restype=c_void_p
        intPtr = GetDllLibDoc().Table_AddRow(self.Ptr)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def AddRow(self ,columnsNum:int)->TableRow:
        """
    <summary>
        Adds a row to table with copy format from the current last row, and then add columnsNum cells to the new row.
    </summary>
    <param name="columnsNum">The number of the count of the new row, it's must be -1 &lt; columnsNum &lt; 64.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().Table_AddRowC.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Table_AddRowC.restype=c_void_p
        intPtr = GetDllLibDoc().Table_AddRowC(self.Ptr, columnsNum)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def AddRow(self ,isCopyFormat:bool)->TableRow:
        """
    <summary>
        Adds new row to table.
    </summary>
    <param name="isCopyFormat"></param>
    <returns></returns>
        """
        
        GetDllLibDoc().Table_AddRowI.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().Table_AddRowI.restype=c_void_p
        intPtr = GetDllLibDoc().Table_AddRowI(self.Ptr, isCopyFormat)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def AddRow(self ,isCopyFormat:bool,autoPopulateCells:bool)->TableRow:
        """
    <summary>
        Adds a row to table with copy format option
    </summary>
    <param name="isCopyFormat">Indicates whether copy format from previous row or not</param>
    <param name="autoPopulateCells">if specifies to populate cells automatically, set to <c>true</c>.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().Table_AddRowIA.argtypes=[c_void_p ,c_bool,c_bool]
        GetDllLibDoc().Table_AddRowIA.restype=c_void_p
        intPtr = GetDllLibDoc().Table_AddRowIA(self.Ptr, isCopyFormat,autoPopulateCells)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def AddRow(self ,isCopyFormat:bool,columnsNum:int)->TableRow:
        """
    <summary>
        Adds a row to table with copy format option
    </summary>
    <param name="isCopyFormat">Indicates whether copy format from previous row or not</param>
    <param name="columnsNum">The number of the count of the new row, it's must be -1 &lt; columnsNum &lt; 64.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().Table_AddRowIC.argtypes=[c_void_p ,c_bool,c_int]
        GetDllLibDoc().Table_AddRowIC.restype=c_void_p
        intPtr = GetDllLibDoc().Table_AddRowIC(self.Ptr, isCopyFormat,columnsNum)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def Replace(self ,pattern:Regex,replace:str)->int:
        """
    <summary>
        Replaces all entries of matchString regular expression with newValue string.
    </summary>
    <param name="pattern">Pattern</param>
    <param name="newValue">Replace text</param>
    <returns></returns>
        """
        replacePtr = StrToPtr(replace)
        intPtrpattern:c_void_p = pattern.Ptr

        GetDllLibDoc().Table_Replace.argtypes=[c_void_p ,c_void_p,c_char_p]
        GetDllLibDoc().Table_Replace.restype=c_int
        ret = GetDllLibDoc().Table_Replace(self.Ptr, intPtrpattern,replacePtr)
        return ret


    @dispatch

    def Replace(self ,given:str,replace:str,caseSensitive:bool,wholeWord:bool)->int:
        """
    <summary>
        Replaces by specified matchString string.
    </summary>
    <param name="matchString">The matchString text.</param>
    <param name="newValue">The newValue text.</param>
    <param name="caseSensitive">if it specifies case sensitive, set to <c>true</c>.</param>
    <param name="wholeWord">if it specifies to search a whole word, set to <c>true</c>.</param>
    <returns></returns>
        """
        givenPtr = StrToPtr(given)
        replacePtr = StrToPtr(replace)
        GetDllLibDoc().Table_ReplaceGRCW.argtypes=[c_void_p ,c_char_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Table_ReplaceGRCW.restype=c_int
        ret = GetDllLibDoc().Table_ReplaceGRCW(self.Ptr, givenPtr,replacePtr,caseSensitive,wholeWord)
        return ret

    @dispatch

    def Replace(self ,pattern:Regex,textSelection:'TextSelection')->int:
        """
    <summary>
        Replaces by specified pattern.
    </summary>
    <param name="pattern">The pattern.</param>
    <param name="textSelection">The text selection.</param>
    <returns></returns>
        """
        intPtrpattern:c_void_p = pattern.Ptr
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Table_ReplacePT.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().Table_ReplacePT.restype=c_int
        ret = GetDllLibDoc().Table_ReplacePT(self.Ptr, intPtrpattern,intPtrtextSelection)
        return ret


    @dispatch

    def Replace(self ,pattern:Regex,textSelection:'TextSelection',saveFormatting:bool)->int:
        """
    <summary>
        Replaces by specified pattern.
    </summary>
    <param name="pattern">The pattern.</param>
    <param name="textSelection">The text selection.</param>
    <param name="saveFormatting">if it specifies save source formatting, set to <c>true</c>.</param>
    <returns></returns>
        """
        intPtrpattern:c_void_p = pattern.Ptr
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Table_ReplacePTS.argtypes=[c_void_p ,c_void_p,c_void_p,c_bool]
        GetDllLibDoc().Table_ReplacePTS.restype=c_int
        ret = GetDllLibDoc().Table_ReplacePTS(self.Ptr, intPtrpattern,intPtrtextSelection,saveFormatting)
        return ret



    def Find(self ,pattern:'Regex')->'TextSelection':
        """
    <summary>
        Finds text by specified pattern.
    </summary>
    <param name="pattern">The pattern.</param>
    <returns></returns>
        """
        intPtrpattern:c_void_p = pattern.Ptr

        GetDllLibDoc().Table_Find.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Table_Find.restype=c_void_p
        intPtr = GetDllLibDoc().Table_Find(self.Ptr, intPtrpattern)
        ret = None if intPtr==None else TextSelection(intPtr)
        return ret




    def ApplyVerticalMerge(self ,columnIndex:int,startRowIndex:int,endRowIndex:int):
        """
    <summary>
        Applies the vertical merge for table cells.
    </summary>
    <param name="columnIndex">Index of the column.</param>
    <param name="startRowIndex">Start index of the row.</param>
    <param name="endRowIndex">End index of the row.</param>
        """
        
        GetDllLibDoc().Table_ApplyVerticalMerge.argtypes=[c_void_p ,c_int,c_int,c_int]
        GetDllLibDoc().Table_ApplyVerticalMerge(self.Ptr, columnIndex,startRowIndex,endRowIndex)


    def ApplyHorizontalMerge(self ,rowIndex:int,startCellIndex:int,endCellIndex:int):
        """
    <summary>
        Applies horizontal merging for cells of table row.
    </summary>
    <param name="rowIndex">Index of the row.</param>
    <param name="startCellIndex">Start index of the cell.</param>
    <param name="endCellIndex">End index of the cell.</param>
        """
        
        GetDllLibDoc().Table_ApplyHorizontalMerge.argtypes=[c_void_p ,c_int,c_int,c_int]
        GetDllLibDoc().Table_ApplyHorizontalMerge(self.Ptr, rowIndex,startCellIndex,endCellIndex)

    def RemoveAbsPosition(self):
        """
    <summary>
        Removes the absolute position data. If table has absolute position in the document,
            all position data will be erased.  
    </summary>
        """
        GetDllLibDoc().Table_RemoveAbsPosition.argtypes=[c_void_p]
        GetDllLibDoc().Table_RemoveAbsPosition(self.Ptr)


    def SetColumnWidth(self ,columnIndex:int,columnWidth:float,columnWidthType:'CellWidthType'):
        """
    <summary>
        Sets the width of all cells in the current column of the table.
    </summary>
    <param name="columnIndex">Index of the column.</param>
    <param name="columnWidth">The column width.</param>
    <param name="columnWidthType">The column width type.</param>
        """
        enumcolumnWidthType:c_int = columnWidthType.value

        GetDllLibDoc().Table_SetColumnWidth.argtypes=[c_void_p ,c_int,c_float,c_int]
        GetDllLibDoc().Table_SetColumnWidth(self.Ptr, columnIndex,columnWidth,enumcolumnWidthType)


    def AutoFit(self ,behavior:'AutoFitBehaviorType'):
        """
    <summary>
        Determines how Microsoft Word resizes a table when the AutoFit feature is used.
    </summary>
    <param name="behavior">How Word resizes the specified table with the AutoFit feature is used.</param>
        """
        enumbehavior:c_int = behavior.value

        GetDllLibDoc().Table_AutoFit.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Table_AutoFit(self.Ptr, enumbehavior)

