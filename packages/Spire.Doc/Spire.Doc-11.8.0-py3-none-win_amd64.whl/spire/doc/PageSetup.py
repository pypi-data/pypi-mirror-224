from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PageSetup (  DocumentSerializable) :
    """

    """
    @property
    def DefaultTabWidth(self)->float:
        """
    <summary>
        Gets or sets the length of the auto tab.
    </summary>
<value>The length of the auto tab.</value>
        """
        GetDllLibDoc().PageSetup_get_DefaultTabWidth.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_DefaultTabWidth.restype=c_float
        ret = GetDllLibDoc().PageSetup_get_DefaultTabWidth(self.Ptr)
        return ret

    @DefaultTabWidth.setter
    def DefaultTabWidth(self, value:float):
        GetDllLibDoc().PageSetup_set_DefaultTabWidth.argtypes=[c_void_p, c_float]
        GetDllLibDoc().PageSetup_set_DefaultTabWidth(self.Ptr, value)

    @property

    def PageSize(self)->'SizeF':
        """
    <summary>
        Gets or sets page size in points.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_PageSize.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageSize.restype=c_void_p
        intPtr = GetDllLibDoc().PageSetup_get_PageSize(self.Ptr)
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @PageSize.setter
    def PageSize(self, value:'SizeF'):
        GetDllLibDoc().PageSetup_set_PageSize.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().PageSetup_set_PageSize(self.Ptr, value.Ptr)

    @property

    def Orientation(self)->'PageOrientation':
        """
    <summary>
        Returns or sets orientation of a page.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_Orientation.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_Orientation.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_Orientation(self.Ptr)
        objwraped = PageOrientation(ret)
        return objwraped

    @Orientation.setter
    def Orientation(self, value:'PageOrientation'):
        GetDllLibDoc().PageSetup_set_Orientation.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_Orientation(self.Ptr, value.value)

    @property

    def VerticalAlignment(self)->'PageAlignment':
        """
    <summary>
        Gets or setsvertical alignment.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_VerticalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_VerticalAlignment.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_VerticalAlignment(self.Ptr)
        objwraped = PageAlignment(ret)
        return objwraped

    @VerticalAlignment.setter
    def VerticalAlignment(self, value:'PageAlignment'):
        GetDllLibDoc().PageSetup_set_VerticalAlignment.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_VerticalAlignment(self.Ptr, value.value)

    @property

    def Margins(self)->'MarginsF':
        """
    <summary>
        Gets or sets page margins in points.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_Margins.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_Margins.restype=c_void_p
        intPtr = GetDllLibDoc().PageSetup_get_Margins(self.Ptr)
        ret = None if intPtr==None else MarginsF(intPtr)
        return ret


    @Margins.setter
    def Margins(self, value:'MarginsF'):
        GetDllLibDoc().PageSetup_set_Margins.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().PageSetup_set_Margins(self.Ptr, value.Ptr)

    @property
    def Gutter(self)->float:
        """
    <summary>
        Gets or sets extra space added to the margin for document binding in points.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_Gutter.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_Gutter.restype=c_float
        ret = GetDllLibDoc().PageSetup_get_Gutter(self.Ptr)
        return ret

    @Gutter.setter
    def Gutter(self, value:float):
        GetDllLibDoc().PageSetup_set_Gutter.argtypes=[c_void_p, c_float]
        GetDllLibDoc().PageSetup_set_Gutter(self.Ptr, value)

    @property
    def HeaderDistance(self)->float:
        """
    <summary>
        Gets or sets height of header in points.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_HeaderDistance.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_HeaderDistance.restype=c_float
        ret = GetDllLibDoc().PageSetup_get_HeaderDistance(self.Ptr)
        return ret

    @HeaderDistance.setter
    def HeaderDistance(self, value:float):
        GetDllLibDoc().PageSetup_set_HeaderDistance.argtypes=[c_void_p, c_float]
        GetDllLibDoc().PageSetup_set_HeaderDistance(self.Ptr, value)

    @property
    def FooterDistance(self)->float:
        """
    <summary>
        Gets or sets footer height in points.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_FooterDistance.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_FooterDistance.restype=c_float
        ret = GetDllLibDoc().PageSetup_get_FooterDistance(self.Ptr)
        return ret

    @FooterDistance.setter
    def FooterDistance(self, value:float):
        GetDllLibDoc().PageSetup_set_FooterDistance.argtypes=[c_void_p, c_float]
        GetDllLibDoc().PageSetup_set_FooterDistance(self.Ptr, value)

    @property
    def ClientWidth(self)->float:
        """
    <summary>
        Gets width of client area.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_ClientWidth.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_ClientWidth.restype=c_float
        ret = GetDllLibDoc().PageSetup_get_ClientWidth(self.Ptr)
        return ret

    @property
    def ClientHeight(self)->float:
        """
    <summary>
        Gets width of client area.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_ClientHeight.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_ClientHeight.restype=c_float
        ret = GetDllLibDoc().PageSetup_get_ClientHeight(self.Ptr)
        return ret

    @property
    def DifferentFirstPageHeaderFooter(self)->bool:
        """
    <summary>
        Setting to specify that the current section has a different header/footer for first page.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_DifferentFirstPageHeaderFooter.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_DifferentFirstPageHeaderFooter.restype=c_bool
        ret = GetDllLibDoc().PageSetup_get_DifferentFirstPageHeaderFooter(self.Ptr)
        return ret

    @DifferentFirstPageHeaderFooter.setter
    def DifferentFirstPageHeaderFooter(self, value:bool):
        GetDllLibDoc().PageSetup_set_DifferentFirstPageHeaderFooter.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().PageSetup_set_DifferentFirstPageHeaderFooter(self.Ptr, value)

    @property
    def DifferentOddAndEvenPagesHeaderFooter(self)->bool:
        """
    <summary>
        True if the document has different headers and footers 
            for odd-numbered and even-numbered pages. 
    </summary>
        """
        GetDllLibDoc().PageSetup_get_DifferentOddAndEvenPagesHeaderFooter.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_DifferentOddAndEvenPagesHeaderFooter.restype=c_bool
        ret = GetDllLibDoc().PageSetup_get_DifferentOddAndEvenPagesHeaderFooter(self.Ptr)
        return ret

    @DifferentOddAndEvenPagesHeaderFooter.setter
    def DifferentOddAndEvenPagesHeaderFooter(self, value:bool):
        GetDllLibDoc().PageSetup_set_DifferentOddAndEvenPagesHeaderFooter.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().PageSetup_set_DifferentOddAndEvenPagesHeaderFooter(self.Ptr, value)

    @property

    def LineNumberingRestartMode(self)->'LineNumberingRestartMode':
        """
    <summary>
        Returns or sets line numbering mode
    </summary>
        """
        GetDllLibDoc().PageSetup_get_LineNumberingRestartMode.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_LineNumberingRestartMode.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_LineNumberingRestartMode(self.Ptr)
        objwraped = LineNumberingRestartMode(ret)
        return objwraped

    @LineNumberingRestartMode.setter
    def LineNumberingRestartMode(self, value:'LineNumberingRestartMode'):
        GetDllLibDoc().PageSetup_set_LineNumberingRestartMode.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_LineNumberingRestartMode(self.Ptr, value.value)

    @property
    def LineNumberingStep(self)->int:
        """
    <summary>
        Gets or sets line numbering step
    </summary>
        """
        GetDllLibDoc().PageSetup_get_LineNumberingStep.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_LineNumberingStep.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_LineNumberingStep(self.Ptr)
        return ret

    @LineNumberingStep.setter
    def LineNumberingStep(self, value:int):
        GetDllLibDoc().PageSetup_set_LineNumberingStep.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_LineNumberingStep(self.Ptr, value)

    @property
    def LineNumberingStartValue(self)->int:
        """
    <summary>
        Gets or setsline numbering start value
    </summary>
        """
        GetDllLibDoc().PageSetup_get_LineNumberingStartValue.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_LineNumberingStartValue.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_LineNumberingStartValue(self.Ptr)
        return ret

    @LineNumberingStartValue.setter
    def LineNumberingStartValue(self, value:int):
        GetDllLibDoc().PageSetup_set_LineNumberingStartValue.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_LineNumberingStartValue(self.Ptr, value)

    @property
    def LineNumberingDistanceFromText(self)->float:
        """
    <summary>
        Gets or setsdistance from text in lines numbering
    </summary>
        """
        GetDllLibDoc().PageSetup_get_LineNumberingDistanceFromText.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_LineNumberingDistanceFromText.restype=c_float
        ret = GetDllLibDoc().PageSetup_get_LineNumberingDistanceFromText(self.Ptr)
        return ret

    @LineNumberingDistanceFromText.setter
    def LineNumberingDistanceFromText(self, value:float):
        GetDllLibDoc().PageSetup_set_LineNumberingDistanceFromText.argtypes=[c_void_p, c_float]
        GetDllLibDoc().PageSetup_set_LineNumberingDistanceFromText(self.Ptr, value)

    @property

    def PageBordersApplyType(self)->'PageBordersApplyType':
        """
    <summary>
        Gets or sets the value that determine on which pages border is applied
    </summary>
        """
        GetDllLibDoc().PageSetup_get_PageBordersApplyType.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageBordersApplyType.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_PageBordersApplyType(self.Ptr)
        objwraped = PageBordersApplyType(ret)
        return objwraped

    @PageBordersApplyType.setter
    def PageBordersApplyType(self, value:'PageBordersApplyType'):
        GetDllLibDoc().PageSetup_set_PageBordersApplyType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_PageBordersApplyType(self.Ptr, value.value)

    @property

    def PageBorderOffsetFrom(self)->'PageBorderOffsetFrom':
        """
    <summary>
        Gets or sets the position of page border
    </summary>
        """
        GetDllLibDoc().PageSetup_get_PageBorderOffsetFrom.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageBorderOffsetFrom.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_PageBorderOffsetFrom(self.Ptr)
        objwraped = PageBorderOffsetFrom(ret)
        return objwraped

    @PageBorderOffsetFrom.setter
    def PageBorderOffsetFrom(self, value:'PageBorderOffsetFrom'):
        GetDllLibDoc().PageSetup_set_PageBorderOffsetFrom.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_PageBorderOffsetFrom(self.Ptr, value.value)

    @property
    def IsFrontPageBorder(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether this instance is front page border.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_IsFrontPageBorder.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_IsFrontPageBorder.restype=c_bool
        ret = GetDllLibDoc().PageSetup_get_IsFrontPageBorder(self.Ptr)
        return ret

    @IsFrontPageBorder.setter
    def IsFrontPageBorder(self, value:bool):
        GetDllLibDoc().PageSetup_set_IsFrontPageBorder.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().PageSetup_set_IsFrontPageBorder(self.Ptr, value)

    @property
    def PageBorderIncludeHeader(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether the page border include the header.
            If the page border is not measured from the text extents using a value of text in the PageBorderOffsetFrome, then it can be ignored.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_PageBorderIncludeHeader.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageBorderIncludeHeader.restype=c_bool
        ret = GetDllLibDoc().PageSetup_get_PageBorderIncludeHeader(self.Ptr)
        return ret

    @PageBorderIncludeHeader.setter
    def PageBorderIncludeHeader(self, value:bool):
        GetDllLibDoc().PageSetup_set_PageBorderIncludeHeader.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().PageSetup_set_PageBorderIncludeHeader(self.Ptr, value)

    @property
    def PageBorderIncludeFooter(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether the page border include the footer.
            If the page border is not measured from the text extents using a value of text in the PageBorderOffsetFrome, then it can be ignored.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_PageBorderIncludeFooter.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageBorderIncludeFooter.restype=c_bool
        ret = GetDllLibDoc().PageSetup_get_PageBorderIncludeFooter(self.Ptr)
        return ret

    @PageBorderIncludeFooter.setter
    def PageBorderIncludeFooter(self, value:bool):
        GetDllLibDoc().PageSetup_set_PageBorderIncludeFooter.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().PageSetup_set_PageBorderIncludeFooter(self.Ptr, value)

    @property

    def Borders(self)->'Borders':
        """
    <summary>
        Gets page borders collection
    </summary>
        """
        GetDllLibDoc().PageSetup_get_Borders.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_Borders.restype=c_void_p
        intPtr = GetDllLibDoc().PageSetup_get_Borders(self.Ptr)
        ret = None if intPtr==None else Borders(intPtr)
        return ret


    @property
    def Bidi(self)->bool:
        """
    <summary>
        Gets or sets whether section contains right-to-left text. 
    </summary>
        """
        GetDllLibDoc().PageSetup_get_Bidi.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_Bidi.restype=c_bool
        ret = GetDllLibDoc().PageSetup_get_Bidi(self.Ptr)
        return ret

    @Bidi.setter
    def Bidi(self, value:bool):
        GetDllLibDoc().PageSetup_set_Bidi.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().PageSetup_set_Bidi(self.Ptr, value)

    @property
    def EqualColumnWidth(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether equal column width.
    </summary>
<value>
  <c>true</c> if equal column width; otherwise, <c>false</c>.</value>
        """
        GetDllLibDoc().PageSetup_get_EqualColumnWidth.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_EqualColumnWidth.restype=c_bool
        ret = GetDllLibDoc().PageSetup_get_EqualColumnWidth(self.Ptr)
        return ret

    @EqualColumnWidth.setter
    def EqualColumnWidth(self, value:bool):
        GetDllLibDoc().PageSetup_set_EqualColumnWidth.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().PageSetup_set_EqualColumnWidth(self.Ptr, value)

    @property

    def PageNumberStyle(self)->'PageNumberStyle':
        """
    <summary>
        Gets or sets the page number style.
    </summary>
<value>The page number style.</value>
        """
        GetDllLibDoc().PageSetup_get_PageNumberStyle.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageNumberStyle.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_PageNumberStyle(self.Ptr)
        objwraped = PageNumberStyle(ret)
        return objwraped

    @PageNumberStyle.setter
    def PageNumberStyle(self, value:'PageNumberStyle'):
        GetDllLibDoc().PageSetup_set_PageNumberStyle.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_PageNumberStyle(self.Ptr, value.value)

    @property
    def PageStartingNumber(self)->int:
        """
    <summary>
        Gets or sets the page starting number.
    </summary>
<value>The page starting number.</value>
        """
        GetDllLibDoc().PageSetup_get_PageStartingNumber.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageStartingNumber.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_PageStartingNumber(self.Ptr)
        return ret

    @PageStartingNumber.setter
    def PageStartingNumber(self, value:int):
        GetDllLibDoc().PageSetup_set_PageStartingNumber.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_PageStartingNumber(self.Ptr, value)

    @property
    def RestartPageNumbering(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to restart page numbering.
    </summary>
<value>
            	if restart page numbering, set to <c>true</c>.
            </value>
        """
        GetDllLibDoc().PageSetup_get_RestartPageNumbering.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_RestartPageNumbering.restype=c_bool
        ret = GetDllLibDoc().PageSetup_get_RestartPageNumbering(self.Ptr)
        return ret

    @RestartPageNumbering.setter
    def RestartPageNumbering(self, value:bool):
        GetDllLibDoc().PageSetup_set_RestartPageNumbering.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().PageSetup_set_RestartPageNumbering(self.Ptr, value)

    @property

    def GridType(self)->'GridPitchType':
        """
    <summary>
        Gets or Sets the grid type of this section.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_GridType.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_GridType.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_GridType(self.Ptr)
        objwraped = GridPitchType(ret)
        return objwraped

    @GridType.setter
    def GridType(self, value:'GridPitchType'):
        GetDllLibDoc().PageSetup_set_GridType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_GridType(self.Ptr, value.value)

    @property
    def LinesPerPage(self)->int:
        """
    <summary>
        Gets or sets the number of lines per page in the document grid.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_LinesPerPage.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_LinesPerPage.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_LinesPerPage(self.Ptr)
        return ret

    @LinesPerPage.setter
    def LinesPerPage(self, value:int):
        GetDllLibDoc().PageSetup_set_LinesPerPage.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_LinesPerPage(self.Ptr, value)

    @property
    def ColumnsLineBetween(self)->bool:
        """
    <summary>
        Gets or sets the value specifies if a vertical line is draw between each 
            of the text columns in the this section.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_ColumnsLineBetween.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_ColumnsLineBetween.restype=c_bool
        ret = GetDllLibDoc().PageSetup_get_ColumnsLineBetween(self.Ptr)
        return ret

    @ColumnsLineBetween.setter
    def ColumnsLineBetween(self, value:bool):
        GetDllLibDoc().PageSetup_set_ColumnsLineBetween.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().PageSetup_set_ColumnsLineBetween(self.Ptr, value)

    @property

    def CharacterSpacingControl(self)->'CharacterSpacing':
        """
    <summary>
        Character Spacing Control.
    </summary>
        """
        GetDllLibDoc().PageSetup_get_CharacterSpacingControl.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_CharacterSpacingControl.restype=c_int
        ret = GetDllLibDoc().PageSetup_get_CharacterSpacingControl(self.Ptr)
        objwraped = CharacterSpacing(ret)
        return objwraped

    @CharacterSpacingControl.setter
    def CharacterSpacingControl(self, value:'CharacterSpacing'):
        GetDllLibDoc().PageSetup_set_CharacterSpacingControl.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageSetup_set_CharacterSpacingControl(self.Ptr, value.value)


    def InsertPageNumbers(self ,fromTopPage:bool,horizontalAlignment:'PageNumberAlignment'):
        """
    <summary>
        Inserts the page numbers.
    </summary>
    <param name="fromTopPage">if it specifies the top of page, set to <c>true</c>.</param>
    <param name="horizontalAlignment">The horizontal alignment.</param>
        """
        enumhorizontalAlignment:c_int = horizontalAlignment.value

        GetDllLibDoc().PageSetup_InsertPageNumbers.argtypes=[c_void_p ,c_bool,c_int]
        GetDllLibDoc().PageSetup_InsertPageNumbers(self.Ptr, fromTopPage,enumhorizontalAlignment)


    def ToString(self)->str:
        """

        """
        GetDllLibDoc().PageSetup_ToString.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_ToString.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().PageSetup_ToString(self.Ptr))
        return ret


