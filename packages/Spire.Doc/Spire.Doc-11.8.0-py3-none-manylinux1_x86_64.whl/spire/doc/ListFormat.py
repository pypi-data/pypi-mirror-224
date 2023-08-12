from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListFormat (  WordAttrCollection) :
    """

    """
    @property
    def ListLevelNumber(self)->int:
        """
    <summary>
        Returns or sets list nesting level. 
    </summary>
        """
        GetDllLibDoc().ListFormat_get_ListLevelNumber.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_ListLevelNumber.restype=c_int
        ret = GetDllLibDoc().ListFormat_get_ListLevelNumber(self.Ptr)
        return ret

    @ListLevelNumber.setter
    def ListLevelNumber(self, value:int):
        GetDllLibDoc().ListFormat_set_ListLevelNumber.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ListFormat_set_ListLevelNumber(self.Ptr, value)

    @property

    def ListType(self)->'ListType':
        """
    <summary>
        Gets type of the list.
    </summary>
        """
        GetDllLibDoc().ListFormat_get_ListType.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_ListType.restype=c_int
        ret = GetDllLibDoc().ListFormat_get_ListType(self.Ptr)
        objwraped = ListType(ret)
        return objwraped

    @property
    def IsRestartNumbering(self)->bool:
        """
    <summary>
        Returns or sets whether numbering of the list must restart from previous list.
    </summary>
        """
        GetDllLibDoc().ListFormat_get_IsRestartNumbering.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_IsRestartNumbering.restype=c_bool
        ret = GetDllLibDoc().ListFormat_get_IsRestartNumbering(self.Ptr)
        return ret

    @IsRestartNumbering.setter
    def IsRestartNumbering(self, value:bool):
        GetDllLibDoc().ListFormat_set_IsRestartNumbering.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ListFormat_set_IsRestartNumbering(self.Ptr, value)

    @property

    def CustomStyleName(self)->str:
        """
    <summary>
        Gets the name of custom style.
    </summary>
        """
        GetDllLibDoc().ListFormat_get_CustomStyleName.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_CustomStyleName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().ListFormat_get_CustomStyleName(self.Ptr))
        return ret


    @property

    def CurrentListStyle(self)->'ListStyle':
        """
    <summary>
        Gets paragraph's list style.
    </summary>
        """
        GetDllLibDoc().ListFormat_get_CurrentListStyle.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_CurrentListStyle.restype=c_void_p
        intPtr = GetDllLibDoc().ListFormat_get_CurrentListStyle(self.Ptr)
        ret = None if intPtr==None else ListStyle(intPtr)
        return ret


    @property

    def CurrentListLevel(self)->'ListLevel':
        """
    <summary>
        Gets paragraph's ListLevel.
    </summary>
        """
        GetDllLibDoc().ListFormat_get_CurrentListLevel.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_CurrentListLevel.restype=c_void_p
        intPtr = GetDllLibDoc().ListFormat_get_CurrentListLevel(self.Ptr)
        ret = None if intPtr==None else ListLevel(intPtr)
        return ret


    def IncreaseIndentLevel(self):
        """
    <summary>
        Increase level indent.
    </summary>
        """
        GetDllLibDoc().ListFormat_IncreaseIndentLevel.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_IncreaseIndentLevel(self.Ptr)

    def DecreaseIndentLevel(self):
        """
    <summary>
        Decrease level indent.
    </summary>
        """
        GetDllLibDoc().ListFormat_DecreaseIndentLevel.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_DecreaseIndentLevel(self.Ptr)

    def ContinueListNumbering(self):
        """
    <summary>
        Continue last list.
    </summary>
        """
        GetDllLibDoc().ListFormat_ContinueListNumbering.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_ContinueListNumbering(self.Ptr)


    def ApplyStyle(self ,styleName:str):
        """
    <summary>
        Apply list style.
    </summary>
    <param name="styleName">The list style name.</param>
        """
        styleNamePtr = StrToPtr(styleName)
        GetDllLibDoc().ListFormat_ApplyStyle.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().ListFormat_ApplyStyle(self.Ptr, styleNamePtr)

    def ApplyBulletStyle(self):
        """
    <summary>
        Apply default bullet style for current paragraph.
    </summary>
        """
        GetDllLibDoc().ListFormat_ApplyBulletStyle.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_ApplyBulletStyle(self.Ptr)

    def ApplyNumberedStyle(self):
        """
    <summary>
        Apply default numbered style for current paragraph.
    </summary>
        """
        GetDllLibDoc().ListFormat_ApplyNumberedStyle.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_ApplyNumberedStyle(self.Ptr)

    def RemoveList(self):
        """
    <summary>
        Removes the list from current paragraph.
    </summary>
        """
        GetDllLibDoc().ListFormat_RemoveList.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_RemoveList(self.Ptr)

