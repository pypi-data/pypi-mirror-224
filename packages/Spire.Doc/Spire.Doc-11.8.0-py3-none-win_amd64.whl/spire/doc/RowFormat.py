from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class RowFormat (  WordAttrCollection) :
    """

    """
    @property

    def BackColor(self)->'Color':
        """
    <summary>
        Gets or sets background color.
    </summary>
        """
        GetDllLibDoc().RowFormat_get_BackColor.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_BackColor.restype=c_void_p
        intPtr = GetDllLibDoc().RowFormat_get_BackColor(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @BackColor.setter
    def BackColor(self, value:'Color'):
        GetDllLibDoc().RowFormat_set_BackColor.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().RowFormat_set_BackColor(self.Ptr, value.Ptr)

    @property

    def Borders(self)->'Borders':
        """
    <summary>
        Gets borders.
    </summary>
        """
        GetDllLibDoc().RowFormat_get_Borders.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_Borders.restype=c_void_p
        intPtr = GetDllLibDoc().RowFormat_get_Borders(self.Ptr)
        from spire.doc import Borders
        ret = None if intPtr==None else Borders(intPtr)
        return ret


    @property

    def Paddings(self)->'Paddings':
        """
    <summary>
        Gets paddings.
    </summary>
        """
        GetDllLibDoc().RowFormat_get_Paddings.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_Paddings.restype=c_void_p
        intPtr = GetDllLibDoc().RowFormat_get_Paddings(self.Ptr)
        from spire.doc import Paddings
        ret = None if intPtr==None else Paddings(intPtr)
        return ret


    @property
    def CellSpacing(self)->float:
        """
    <summary>
        Returns or sets spacing between cells.
            The setting value must be between 0 pt and 264.5 pt. 
            The value will not be applied to this property if it is set out of range.
            This property will be cleared if the set value is less than 0. 
    </summary>
        """
        GetDllLibDoc().RowFormat_get_CellSpacing.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_CellSpacing.restype=c_float
        ret = GetDllLibDoc().RowFormat_get_CellSpacing(self.Ptr)
        return ret

    @CellSpacing.setter
    def CellSpacing(self, value:float):
        GetDllLibDoc().RowFormat_set_CellSpacing.argtypes=[c_void_p, c_float]
        GetDllLibDoc().RowFormat_set_CellSpacing(self.Ptr, value)

    @property
    def LeftIndent(self)->float:
        """
    <summary>
        Returns or sets table indent.
    </summary>
        """
        GetDllLibDoc().RowFormat_get_LeftIndent.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_LeftIndent.restype=c_float
        ret = GetDllLibDoc().RowFormat_get_LeftIndent(self.Ptr)
        return ret

    @LeftIndent.setter
    def LeftIndent(self, value:float):
        GetDllLibDoc().RowFormat_set_LeftIndent.argtypes=[c_void_p, c_float]
        GetDllLibDoc().RowFormat_set_LeftIndent(self.Ptr, value)

    @property
    def IsAutoResized(self)->bool:
        """
    <summary>
        Returns or sets the boolean value indicating if table is auto resized
    </summary>
        """
        GetDllLibDoc().RowFormat_get_IsAutoResized.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_IsAutoResized.restype=c_bool
        ret = GetDllLibDoc().RowFormat_get_IsAutoResized(self.Ptr)
        return ret

    @IsAutoResized.setter
    def IsAutoResized(self, value:bool):
        GetDllLibDoc().RowFormat_set_IsAutoResized.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().RowFormat_set_IsAutoResized(self.Ptr, value)

    @property
    def IsBreakAcrossPages(self)->bool:
        """
    <summary>
        Returns or sets the boolean value indicating if there is a break across pages
    </summary>
        """
        GetDllLibDoc().RowFormat_get_IsBreakAcrossPages.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_IsBreakAcrossPages.restype=c_bool
        ret = GetDllLibDoc().RowFormat_get_IsBreakAcrossPages(self.Ptr)
        return ret

    @IsBreakAcrossPages.setter
    def IsBreakAcrossPages(self, value:bool):
        GetDllLibDoc().RowFormat_set_IsBreakAcrossPages.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().RowFormat_set_IsBreakAcrossPages(self.Ptr, value)

    @property
    def Bidi(self)->bool:
        """
    <summary>
        Returns or sets whether table is right to left. 
    </summary>
        """
        GetDllLibDoc().RowFormat_get_Bidi.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_Bidi.restype=c_bool
        ret = GetDllLibDoc().RowFormat_get_Bidi(self.Ptr)
        return ret

    @Bidi.setter
    def Bidi(self, value:bool):
        GetDllLibDoc().RowFormat_set_Bidi.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().RowFormat_set_Bidi(self.Ptr, value)

    @property

    def HorizontalAlignment(self)->'RowAlignment':
        """
    <summary>
        Gets or sets horizontal alignment for the table. 
    </summary>
        """
        GetDllLibDoc().RowFormat_get_HorizontalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_HorizontalAlignment.restype=c_int
        ret = GetDllLibDoc().RowFormat_get_HorizontalAlignment(self.Ptr)
        objwraped = RowAlignment(ret)
        return objwraped

    @HorizontalAlignment.setter
    def HorizontalAlignment(self, value:'RowAlignment'):
        GetDllLibDoc().RowFormat_set_HorizontalAlignment.argtypes=[c_void_p, c_int]
        GetDllLibDoc().RowFormat_set_HorizontalAlignment(self.Ptr, value.value)

    @property
    def WrapTextAround(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to use "Around" text wrapping.
    </summary>
<value>
  <c>true</c> if wrap text around; otherwise, <c>false</c>.</value>
        """
        GetDllLibDoc().RowFormat_get_WrapTextAround.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_WrapTextAround.restype=c_bool
        ret = GetDllLibDoc().RowFormat_get_WrapTextAround(self.Ptr)
        return ret

    @WrapTextAround.setter
    def WrapTextAround(self, value:bool):
        GetDllLibDoc().RowFormat_set_WrapTextAround.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().RowFormat_set_WrapTextAround(self.Ptr, value)

    @property

    def Positioning(self)->'TablePositioning':
        """
    <summary>
        the positioning.
    </summary>
<value>The positioning.</value>
        """
        GetDllLibDoc().RowFormat_get_Positioning.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_Positioning.restype=c_void_p
        intPtr = GetDllLibDoc().RowFormat_get_Positioning(self.Ptr)
        from spire.doc import TablePositioning
        ret = None if intPtr==None else TablePositioning(intPtr)
        return ret


    @property

    def LayoutType(self)->'LayoutType':
        """
    <summary>
        Gets or set the value of the layoutType.
            This element specifies the algorithm which shall be used  to layout the comtents of the table within the document.
    </summary>
<value>The type of the layout.</value>
        """
        GetDllLibDoc().RowFormat_get_LayoutType.argtypes=[c_void_p]
        GetDllLibDoc().RowFormat_get_LayoutType.restype=c_int
        ret = GetDllLibDoc().RowFormat_get_LayoutType(self.Ptr)
        objwraped = LayoutType(ret)
        return objwraped

    @LayoutType.setter
    def LayoutType(self, value:'LayoutType'):
        GetDllLibDoc().RowFormat_set_LayoutType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().RowFormat_set_LayoutType(self.Ptr, value.value)

