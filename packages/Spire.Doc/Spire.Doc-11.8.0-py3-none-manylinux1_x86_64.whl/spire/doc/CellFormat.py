from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CellFormat (  WordAttrCollection) :
    """

    """
    @property

    def Borders(self)->'Borders':
        """
    <summary>
        Gets borders.
    </summary>
        """
        GetDllLibDoc().CellFormat_get_Borders.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_Borders.restype=c_void_p
        intPtr = GetDllLibDoc().CellFormat_get_Borders(self.Ptr)
        ret = None if intPtr==None else Borders(intPtr)
        return ret


    @property

    def Paddings(self)->'Paddings':
        """
    <summary>
        Gets paddings.
    </summary>
        """
        GetDllLibDoc().CellFormat_get_Paddings.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_Paddings.restype=c_void_p
        intPtr = GetDllLibDoc().CellFormat_get_Paddings(self.Ptr)
        ret = None if intPtr==None else Paddings(intPtr)
        return ret


    @property

    def VerticalAlignment(self)->'VerticalAlignment':
        """
    <summary>
        Gets or sets vertical alignment.
    </summary>
        """
        GetDllLibDoc().CellFormat_get_VerticalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_VerticalAlignment.restype=c_int
        ret = GetDllLibDoc().CellFormat_get_VerticalAlignment(self.Ptr)
        objwraped = VerticalAlignment(ret)
        return objwraped

    @VerticalAlignment.setter
    def VerticalAlignment(self, value:'VerticalAlignment'):
        GetDllLibDoc().CellFormat_set_VerticalAlignment.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CellFormat_set_VerticalAlignment(self.Ptr, value.value)

    @property

    def BackColor(self)->'Color':
        """
    <summary>
        Gets or sets background color.
    </summary>
        """
        GetDllLibDoc().CellFormat_get_BackColor.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_BackColor.restype=c_void_p
        intPtr = GetDllLibDoc().CellFormat_get_BackColor(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @BackColor.setter
    def BackColor(self, value:'Color'):
        GetDllLibDoc().CellFormat_set_BackColor.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().CellFormat_set_BackColor(self.Ptr, value.Ptr)

    @property

    def VerticalMerge(self)->'CellMerge':
        """
    <summary>
        Returns or setsthe way of vertical merging of the cell.
    </summary>
        """
        GetDllLibDoc().CellFormat_get_VerticalMerge.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_VerticalMerge.restype=c_int
        ret = GetDllLibDoc().CellFormat_get_VerticalMerge(self.Ptr)
        objwraped = CellMerge(ret)
        return objwraped

    @VerticalMerge.setter
    def VerticalMerge(self, value:'CellMerge'):
        GetDllLibDoc().CellFormat_set_VerticalMerge.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CellFormat_set_VerticalMerge(self.Ptr, value.value)

    @property

    def HorizontalMerge(self)->'CellMerge':
        """
    <summary>
        Returns or setsthe way of horizontal merging of the cell.
    </summary>
        """
        GetDllLibDoc().CellFormat_get_HorizontalMerge.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_HorizontalMerge.restype=c_int
        ret = GetDllLibDoc().CellFormat_get_HorizontalMerge(self.Ptr)
        objwraped = CellMerge(ret)
        return objwraped

    @HorizontalMerge.setter
    def HorizontalMerge(self, value:'CellMerge'):
        GetDllLibDoc().CellFormat_set_HorizontalMerge.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CellFormat_set_HorizontalMerge(self.Ptr, value.value)

    @property
    def TextWrap(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether [text wrap].
    </summary>
<value>
  <c>true</c> if it specifies text wrap, set to <c>true</c>.</value>
        """
        GetDllLibDoc().CellFormat_get_TextWrap.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_TextWrap.restype=c_bool
        ret = GetDllLibDoc().CellFormat_get_TextWrap(self.Ptr)
        return ret

    @TextWrap.setter
    def TextWrap(self, value:bool):
        GetDllLibDoc().CellFormat_set_TextWrap.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CellFormat_set_TextWrap(self.Ptr, value)

    @property
    def FitText(self)->bool:
        """
    <summary>
        Gets or sets fit text option.
    </summary>
        """
        GetDllLibDoc().CellFormat_get_FitText.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_FitText.restype=c_bool
        ret = GetDllLibDoc().CellFormat_get_FitText(self.Ptr)
        return ret

    @FitText.setter
    def FitText(self, value:bool):
        GetDllLibDoc().CellFormat_set_FitText.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CellFormat_set_FitText(self.Ptr, value)

    @property

    def TextDirection(self)->'TextDirection':
        """
    <summary>
        Gets or sets cell text direction.
    </summary>
        """
        GetDllLibDoc().CellFormat_get_TextDirection.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_TextDirection.restype=c_int
        ret = GetDllLibDoc().CellFormat_get_TextDirection(self.Ptr)
        objwraped = TextDirection(ret)
        return objwraped

    @TextDirection.setter
    def TextDirection(self, value:'TextDirection'):
        GetDllLibDoc().CellFormat_set_TextDirection.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CellFormat_set_TextDirection(self.Ptr, value.value)

    @property
    def SamePaddingsAsTable(self)->bool:
        """
    <summary>
        Defines whether to use same paddings as table has. 
    </summary>
        """
        GetDllLibDoc().CellFormat_get_SamePaddingsAsTable.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_SamePaddingsAsTable.restype=c_bool
        ret = GetDllLibDoc().CellFormat_get_SamePaddingsAsTable(self.Ptr)
        return ret

    @SamePaddingsAsTable.setter
    def SamePaddingsAsTable(self, value:bool):
        GetDllLibDoc().CellFormat_set_SamePaddingsAsTable.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CellFormat_set_SamePaddingsAsTable(self.Ptr, value)

    def ClearBackground(self):
        """
    <summary>
        Clears cell background.
    </summary>
        """
        GetDllLibDoc().CellFormat_ClearBackground.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_ClearBackground(self.Ptr)

