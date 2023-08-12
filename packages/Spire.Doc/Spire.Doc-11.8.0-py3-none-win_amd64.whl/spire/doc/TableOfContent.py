from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TableOfContent (  ParagraphBase, IDocumentObject) :
    """

    """
    @dispatch
    def __init__(self, doc:IDocument):
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().TableOfContent_CreateTableOfContentD.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_CreateTableOfContentD.restype=c_void_p
        intPtr = GetDllLibDoc().TableOfContent_CreateTableOfContentD(intPdoc)
        super(TableOfContent, self).__init__(intPtr)

    @dispatch
    def __init__(self, doc:IDocument,switches:str):
        switchesPtr = StrToPtr(switches)
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().TableOfContent_CreateTableOfContentDS.argtypes=[c_void_p,c_char_p]
        GetDllLibDoc().TableOfContent_CreateTableOfContentDS.restype=c_void_p
        intPtr = GetDllLibDoc().TableOfContent_CreateTableOfContentDS(intPdoc,switchesPtr)
        super(TableOfContent, self).__init__(intPtr)

    @property
    def UseAbsolutePos(self)->bool:
        """

        """
        GetDllLibDoc().TableOfContent_get_UseAbsolutePos.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UseAbsolutePos.restype=c_bool
        ret = GetDllLibDoc().TableOfContent_get_UseAbsolutePos(self.Ptr)
        return ret

    @UseAbsolutePos.setter
    def UseAbsolutePos(self, value:bool):
        GetDllLibDoc().TableOfContent_set_UseAbsolutePos.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().TableOfContent_set_UseAbsolutePos(self.Ptr, value)

    @property
    def UseHeadingStyles(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to use default heading styles.
    </summary>
<value>if it uses heading styles, set to <c>true</c>.</value>
        """
        GetDllLibDoc().TableOfContent_get_UseHeadingStyles.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UseHeadingStyles.restype=c_bool
        ret = GetDllLibDoc().TableOfContent_get_UseHeadingStyles(self.Ptr)
        return ret

    @UseHeadingStyles.setter
    def UseHeadingStyles(self, value:bool):
        GetDllLibDoc().TableOfContent_set_UseHeadingStyles.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().TableOfContent_set_UseHeadingStyles(self.Ptr, value)

    @property
    def UpperHeadingLevel(self)->int:
        """
    <summary>
        Gets or sets the ending heading level of the table of content. Default value is 3.
    </summary>
<value>The upper heading level.</value>
        """
        GetDllLibDoc().TableOfContent_get_UpperHeadingLevel.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UpperHeadingLevel.restype=c_int
        ret = GetDllLibDoc().TableOfContent_get_UpperHeadingLevel(self.Ptr)
        return ret

    @UpperHeadingLevel.setter
    def UpperHeadingLevel(self, value:int):
        GetDllLibDoc().TableOfContent_set_UpperHeadingLevel.argtypes=[c_void_p, c_int]
        GetDllLibDoc().TableOfContent_set_UpperHeadingLevel(self.Ptr, value)

    @property
    def LowerHeadingLevel(self)->int:
        """
    <summary>
        Gets or sets the starting heading level of the table of content. Default value is 1
    </summary>
<value>The starting heading level.</value>
        """
        GetDllLibDoc().TableOfContent_get_LowerHeadingLevel.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_LowerHeadingLevel.restype=c_int
        ret = GetDllLibDoc().TableOfContent_get_LowerHeadingLevel(self.Ptr)
        return ret

    @LowerHeadingLevel.setter
    def LowerHeadingLevel(self, value:int):
        GetDllLibDoc().TableOfContent_set_LowerHeadingLevel.argtypes=[c_void_p, c_int]
        GetDllLibDoc().TableOfContent_set_LowerHeadingLevel(self.Ptr, value)

    @property
    def UseTableEntryFields(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to use table entry fields.Default value is false.
    </summary>
<value>
            if it uses table entry fields, set to <c>true</c>.
            </value>
        """
        GetDllLibDoc().TableOfContent_get_UseTableEntryFields.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UseTableEntryFields.restype=c_bool
        ret = GetDllLibDoc().TableOfContent_get_UseTableEntryFields(self.Ptr)
        return ret

    @UseTableEntryFields.setter
    def UseTableEntryFields(self, value:bool):
        GetDllLibDoc().TableOfContent_set_UseTableEntryFields.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().TableOfContent_set_UseTableEntryFields(self.Ptr, value)

    @property

    def TableID(self)->str:
        """
    <summary>
        Gets or sets the table ID.
    </summary>
<value>The table ID.</value>
        """
        GetDllLibDoc().TableOfContent_get_TableID.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_TableID.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().TableOfContent_get_TableID(self.Ptr))
        return ret


    @TableID.setter
    def TableID(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TableOfContent_set_TableID.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().TableOfContent_set_TableID(self.Ptr, valuePtr)

    @property
    def RightAlignPageNumbers(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to show page numbers from right side. Default value is true.
    </summary>
<value>
            	if right align of page numbers, set to <c>true</c>.
            </value>
        """
        GetDllLibDoc().TableOfContent_get_RightAlignPageNumbers.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_RightAlignPageNumbers.restype=c_bool
        ret = GetDllLibDoc().TableOfContent_get_RightAlignPageNumbers(self.Ptr)
        return ret

    @RightAlignPageNumbers.setter
    def RightAlignPageNumbers(self, value:bool):
        GetDllLibDoc().TableOfContent_set_RightAlignPageNumbers.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().TableOfContent_set_RightAlignPageNumbers(self.Ptr, value)

    @property
    def IncludePageNumbers(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to show page numbers. Default value is true.
    </summary>
<value>if it includes page numbers, set to <c>true</c>.</value>
        """
        GetDllLibDoc().TableOfContent_get_IncludePageNumbers.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_IncludePageNumbers.restype=c_bool
        ret = GetDllLibDoc().TableOfContent_get_IncludePageNumbers(self.Ptr)
        return ret

    @IncludePageNumbers.setter
    def IncludePageNumbers(self, value:bool):
        GetDllLibDoc().TableOfContent_set_IncludePageNumbers.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().TableOfContent_set_IncludePageNumbers(self.Ptr, value)

    @property
    def UseHyperlinks(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to use hyperlinks.Default value is true.
    </summary>
<value>if it uses hyperlinks, set to <c>true</c>.</value>
        """
        GetDllLibDoc().TableOfContent_get_UseHyperlinks.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UseHyperlinks.restype=c_bool
        ret = GetDllLibDoc().TableOfContent_get_UseHyperlinks(self.Ptr)
        return ret

    @UseHyperlinks.setter
    def UseHyperlinks(self, value:bool):
        GetDllLibDoc().TableOfContent_set_UseHyperlinks.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().TableOfContent_set_UseHyperlinks(self.Ptr, value)

    @property
    def UseOutlineLevels(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether use outline levels.Default value is false.
    </summary>
<value>if it uses outline levels, set to <c>true</c>.</value>
        """
        GetDllLibDoc().TableOfContent_get_UseOutlineLevels.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UseOutlineLevels.restype=c_bool
        ret = GetDllLibDoc().TableOfContent_get_UseOutlineLevels(self.Ptr)
        return ret

    @UseOutlineLevels.setter
    def UseOutlineLevels(self, value:bool):
        GetDllLibDoc().TableOfContent_set_UseOutlineLevels.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().TableOfContent_set_UseOutlineLevels(self.Ptr, value)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().TableOfContent_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().TableOfContent_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped


    def SetTOCLevelStyle(self ,levelNumber:int,styleName:str):
        """
    <summary>
        Sets the style for TOC level.
    </summary>
    <param name="levelNumber">The level number.</param>
    <param name="styleName">Name of the style.</param>
        """
        styleNamePtr = StrToPtr(styleName)
        GetDllLibDoc().TableOfContent_SetTOCLevelStyle.argtypes=[c_void_p ,c_int,c_char_p]
        GetDllLibDoc().TableOfContent_SetTOCLevelStyle(self.Ptr, levelNumber,styleNamePtr)


    def GetTOCLevelStyle(self ,levelNumber:int)->str:
        """
    <summary>
        Gets the style name for TOC level.
    </summary>
    <param name="levelNumber">The level number.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().TableOfContent_GetTOCLevelStyle.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TableOfContent_GetTOCLevelStyle.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().TableOfContent_GetTOCLevelStyle(self.Ptr, levelNumber))
        return ret


