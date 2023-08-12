from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Border (  AttrCollection) :
    """

    """
    @property

    def Color(self)->'Color':
        """
    <summary>
        Gets or sets color of the border.
    </summary>
        """
        GetDllLibDoc().Border_get_Color.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_Color.restype=c_void_p
        intPtr = GetDllLibDoc().Border_get_Color(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @Color.setter
    def Color(self, value:'Color'):
        GetDllLibDoc().Border_set_Color.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().Border_set_Color(self.Ptr, value.Ptr)

    @property
    def LineWidth(self)->float:
        """
    <summary>
        Gets or sets width of the border.
    </summary>
        """
        GetDllLibDoc().Border_get_LineWidth.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_LineWidth.restype=c_float
        ret = GetDllLibDoc().Border_get_LineWidth(self.Ptr)
        return ret

    @LineWidth.setter
    def LineWidth(self, value:float):
        GetDllLibDoc().Border_set_LineWidth.argtypes=[c_void_p, c_float]
        GetDllLibDoc().Border_set_LineWidth(self.Ptr, value)

    @property

    def BorderType(self)->'BorderStyle':
        """
    <summary>
        Gets or sets  style of the border.
    </summary>
        """
        GetDllLibDoc().Border_get_BorderType.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_BorderType.restype=c_int
        ret = GetDllLibDoc().Border_get_BorderType(self.Ptr)
        objwraped = BorderStyle(ret)
        return objwraped

    @BorderType.setter
    def BorderType(self, value:'BorderStyle'):
        GetDllLibDoc().Border_set_BorderType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Border_set_BorderType(self.Ptr, value.value)

    @property
    def Space(self)->float:
        """
    <summary>
        Returns or setswidth of space to maintain between border and text within border.
    </summary>
        """
        GetDllLibDoc().Border_get_Space.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_Space.restype=c_float
        ret = GetDllLibDoc().Border_get_Space(self.Ptr)
        return ret

    @Space.setter
    def Space(self, value:float):
        GetDllLibDoc().Border_set_Space.argtypes=[c_void_p, c_float]
        GetDllLibDoc().Border_set_Space(self.Ptr, value)

    @property
    def Shadow(self)->bool:
        """
    <summary>
        Setting to define if border should be drawn with shadow.
    </summary>
        """
        GetDllLibDoc().Border_get_Shadow.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_Shadow.restype=c_bool
        ret = GetDllLibDoc().Border_get_Shadow(self.Ptr)
        return ret

    @Shadow.setter
    def Shadow(self, value:bool):
        GetDllLibDoc().Border_set_Shadow.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Border_set_Shadow(self.Ptr, value)

    @property
    def IsDefault(self)->bool:
        """
    <summary>
        Gets a value indicating whether format is default.
    </summary>
<value>
  <c>true</c> if format is default; otherwise,<c>false</c>.</value>
        """
        GetDllLibDoc().Border_get_IsDefault.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_IsDefault.restype=c_bool
        ret = GetDllLibDoc().Border_get_IsDefault(self.Ptr)
        return ret


    def InitFormatting(self ,color:'Color',lineWidth:float,borderType:'BorderStyle',shadow:bool):
        """
    <summary>
        Initialize Border style.
    </summary>
    <param name="color">The color.</param>
    <param name="lineWidth">Width of the line.</param>
    <param name="borderType">Type of the border.</param>
    <param name="shadow">if it specifies shadow, set to <c>true</c>.</param>
        """
        intPtrcolor:c_void_p = color.Ptr
        enumborderType:c_int = borderType.value

        GetDllLibDoc().Border_InitFormatting.argtypes=[c_void_p ,c_void_p,c_float,c_int,c_bool]
        GetDllLibDoc().Border_InitFormatting(self.Ptr, intPtrcolor,lineWidth,enumborderType,shadow)

