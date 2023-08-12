from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ParagraphFormat (  WordAttrCollection) :
    """

    """
    @property
    def WordWrap(self)->bool:
        """
<summary>        
             Gets or sets a value that determines whether allow Latin text to wrap in the middle of a word.   
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_WordWrap.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_WordWrap.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_WordWrap(self.Ptr)
        return ret

    @WordWrap.setter
    def WordWrap(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_WordWrap.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_WordWrap(self.Ptr, value)

    @property

    def TextAlignment(self)->'TextAlignment':
        """
    <summary>
        Gets or sets the style of textalignment 
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_TextAlignment.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_TextAlignment.restype=c_int
        ret = GetDllLibDoc().ParagraphFormat_get_TextAlignment(self.Ptr)
        objwraped = TextAlignment(ret)
        return objwraped

    @TextAlignment.setter
    def TextAlignment(self, value:'TextAlignment'):
        GetDllLibDoc().ParagraphFormat_set_TextAlignment.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ParagraphFormat_set_TextAlignment(self.Ptr, value.value)

    @property
    def MirrorIndents(self)->bool:
        """
    <summary>
        Gets a value indicating whether indentation type is mirror indents.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_MirrorIndents.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_MirrorIndents.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_MirrorIndents(self.Ptr)
        return ret

    @MirrorIndents.setter
    def MirrorIndents(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_MirrorIndents.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_MirrorIndents(self.Ptr, value)

    @property
    def SuppressAutoHyphens(self)->bool:
        """
    <summary>
        Indicates whether to suppress automatic hyphenation for the paragraph.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_SuppressAutoHyphens.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_SuppressAutoHyphens.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_SuppressAutoHyphens(self.Ptr)
        return ret

    @SuppressAutoHyphens.setter
    def SuppressAutoHyphens(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_SuppressAutoHyphens.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_SuppressAutoHyphens(self.Ptr, value)


    def SetLeftIndent(self ,leftIndent:float):
        """
    <summary>
        Sets the value that represents the left indent for paragraph.
    </summary>
    <param name="leftIndent">The left indent.</param>
        """
        
        GetDllLibDoc().ParagraphFormat_SetLeftIndent.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().ParagraphFormat_SetLeftIndent(self.Ptr, leftIndent)


    def SetRightIndent(self ,rightIndent:float):
        """
    <summary>
        Sets the value that represents the right indent for paragraph.
    </summary>
    <param name="rightIndent">The right indent.</param>
        """
        
        GetDllLibDoc().ParagraphFormat_SetRightIndent.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().ParagraphFormat_SetRightIndent(self.Ptr, rightIndent)


    def SetFirstLineIndent(self ,firstLineIndent:float):
        """
    <summary>
        Sets the value that represents the first line indent for paragraph.
    </summary>
    <param name="firstLineIndent">The first line indent.</param>
        """
        
        GetDllLibDoc().ParagraphFormat_SetFirstLineIndent.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().ParagraphFormat_SetFirstLineIndent(self.Ptr, firstLineIndent)

    def ClearBackground(self):
        """
    <summary>
        Clears paragraph background.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_ClearBackground.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_ClearBackground(self.Ptr)

    @property
    def IsKinSoku(self)->bool:
        """
    <summary>
        Get or Set a value that determines whether use Asian rules for controlling first and last characters.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_IsKinSoku.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_IsKinSoku.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_IsKinSoku(self.Ptr)
        return ret

    @IsKinSoku.setter
    def IsKinSoku(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_IsKinSoku.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_IsKinSoku(self.Ptr, value)

    @property
    def IsBidi(self)->bool:
        """
    <summary>
        Returns or sets right-to-left property of the paragraph.
    </summary>
<value>if bidi, set to <c>true</c>.</value>
        """
        GetDllLibDoc().ParagraphFormat_get_IsBidi.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_IsBidi.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_IsBidi(self.Ptr)
        return ret

    @IsBidi.setter
    def IsBidi(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_IsBidi.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_IsBidi(self.Ptr, value)

    @property

    def Tabs(self)->'TabCollection':
        """
    <summary>
        Gets the tabs info.
    </summary>
<value>The tabs info.</value>
        """
        GetDllLibDoc().ParagraphFormat_get_Tabs.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_Tabs.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphFormat_get_Tabs(self.Ptr)
        from spire.doc import TabCollection
        ret = None if intPtr==None else TabCollection(intPtr)
        return ret


    @property
    def KeepLines(self)->bool:
        """
    <summary>
        True if all lines in the paragraph are to remain on the same page. 
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_KeepLines.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_KeepLines.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_KeepLines(self.Ptr)
        return ret

    @KeepLines.setter
    def KeepLines(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_KeepLines.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_KeepLines(self.Ptr, value)

    @property
    def KeepFollow(self)->bool:
        """
    <summary>
        True if the paragraph is to remains on the same page as the 
            paragraph that follows it. 
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_KeepFollow.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_KeepFollow.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_KeepFollow(self.Ptr)
        return ret

    @KeepFollow.setter
    def KeepFollow(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_KeepFollow.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_KeepFollow(self.Ptr, value)

    @property
    def PageBreakBefore(self)->bool:
        """
    <summary>
        True if a page break is forced before the paragraph
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_PageBreakBefore.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_PageBreakBefore.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_PageBreakBefore(self.Ptr)
        return ret

    @PageBreakBefore.setter
    def PageBreakBefore(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_PageBreakBefore.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_PageBreakBefore(self.Ptr, value)

    @property
    def PageBreakAfter(self)->bool:
        """
    <summary>
        True if a page break is forced after the paragraph
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_PageBreakAfter.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_PageBreakAfter.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_PageBreakAfter(self.Ptr)
        return ret

    @PageBreakAfter.setter
    def PageBreakAfter(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_PageBreakAfter.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_PageBreakAfter(self.Ptr, value)

    @property
    def IsWidowControl(self)->bool:
        """
    <summary>
        True if the first and last lines in the paragraph 
            are to remain on the same page as the rest of the paragraph. 
    </summary>
<remarks></remarks>
        """
        GetDllLibDoc().ParagraphFormat_get_IsWidowControl.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_IsWidowControl.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_IsWidowControl(self.Ptr)
        return ret

    @IsWidowControl.setter
    def IsWidowControl(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_IsWidowControl.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_IsWidowControl(self.Ptr, value)

    @property
    def AutoSpaceDN(self)->bool:
        """
    <summary>
        Gets or sets the value that determines whether the space is automatically adjusted between Asian text and numbers. 
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_AutoSpaceDN.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_AutoSpaceDN.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_AutoSpaceDN(self.Ptr)
        return ret

    @AutoSpaceDN.setter
    def AutoSpaceDN(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_AutoSpaceDN.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_AutoSpaceDN(self.Ptr, value)

    @property
    def AutoSpaceDE(self)->bool:
        """
    <summary>
         Gets or sets the value that determines whether the space is automatically adjusted between Asian and Latin text.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_AutoSpaceDE.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_AutoSpaceDE.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_AutoSpaceDE(self.Ptr)
        return ret

    @AutoSpaceDE.setter
    def AutoSpaceDE(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_AutoSpaceDE.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_AutoSpaceDE(self.Ptr, value)

    @property

    def HorizontalAlignment(self)->'HorizontalAlignment':
        """
    <summary>
        Returns or sets horizontal alignment for the paragraph. 
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_HorizontalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_HorizontalAlignment.restype=c_int
        ret = GetDllLibDoc().ParagraphFormat_get_HorizontalAlignment(self.Ptr)
        objwraped = HorizontalAlignment(ret)
        return objwraped

    @HorizontalAlignment.setter
    def HorizontalAlignment(self, value:'HorizontalAlignment'):
        GetDllLibDoc().ParagraphFormat_set_HorizontalAlignment.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ParagraphFormat_set_HorizontalAlignment(self.Ptr, value.value)

    @property
    def LeftIndent(self)->float:
        """
    <summary>
        Returns or set sthe value that represents the left indent for paragraph. 
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_LeftIndent.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_LeftIndent.restype=c_float
        ret = GetDllLibDoc().ParagraphFormat_get_LeftIndent(self.Ptr)
        return ret

    @LeftIndent.setter
    def LeftIndent(self, value:float):
        GetDllLibDoc().ParagraphFormat_set_LeftIndent.argtypes=[c_void_p, c_float]
        GetDllLibDoc().ParagraphFormat_set_LeftIndent(self.Ptr, value)

    @property
    def RightIndent(self)->float:
        """
    <summary>
        Returns or sets the value that represents the right indent for paragraph.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_RightIndent.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_RightIndent.restype=c_float
        ret = GetDllLibDoc().ParagraphFormat_get_RightIndent(self.Ptr)
        return ret

    @RightIndent.setter
    def RightIndent(self, value:float):
        GetDllLibDoc().ParagraphFormat_set_RightIndent.argtypes=[c_void_p, c_float]
        GetDllLibDoc().ParagraphFormat_set_RightIndent(self.Ptr, value)

    @property
    def FirstLineIndent(self)->float:
        """
    <summary>
        Gets or sets the value(in points) for first line or hanging indent.Positive
            value represents first-line indent, and Negative value
            represents hanging indent.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_FirstLineIndent.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_FirstLineIndent.restype=c_float
        ret = GetDllLibDoc().ParagraphFormat_get_FirstLineIndent(self.Ptr)
        return ret

    @FirstLineIndent.setter
    def FirstLineIndent(self, value:float):
        GetDllLibDoc().ParagraphFormat_set_FirstLineIndent.argtypes=[c_void_p, c_float]
        GetDllLibDoc().ParagraphFormat_set_FirstLineIndent(self.Ptr, value)

    @property
    def BeforeSpacing(self)->float:
        """
    <summary>
        Returns or sets the spacing (in points) before the paragraph. 
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_BeforeSpacing.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_BeforeSpacing.restype=c_float
        ret = GetDllLibDoc().ParagraphFormat_get_BeforeSpacing(self.Ptr)
        return ret

    @BeforeSpacing.setter
    def BeforeSpacing(self, value:float):
        GetDllLibDoc().ParagraphFormat_set_BeforeSpacing.argtypes=[c_void_p, c_float]
        GetDllLibDoc().ParagraphFormat_set_BeforeSpacing(self.Ptr, value)

    @property
    def AfterSpacing(self)->float:
        """
    <summary>
        Returns or sets the spacing (in points) after the paragraph.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_AfterSpacing.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_AfterSpacing.restype=c_float
        ret = GetDllLibDoc().ParagraphFormat_get_AfterSpacing(self.Ptr)
        return ret

    @AfterSpacing.setter
    def AfterSpacing(self, value:float):
        GetDllLibDoc().ParagraphFormat_set_AfterSpacing.argtypes=[c_void_p, c_float]
        GetDllLibDoc().ParagraphFormat_set_AfterSpacing(self.Ptr, value)

    @property

    def Borders(self)->'Borders':
        """
    <summary>
        Gets collection of borders in the paragraph
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_Borders.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_Borders.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphFormat_get_Borders(self.Ptr)
        ret = None if intPtr==None else Borders(intPtr)
        return ret


    @property

    def BackColor(self)->'Color':
        """
    <summary>
        Gets or sets background color of the paragraph 
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_BackColor.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_BackColor.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphFormat_get_BackColor(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @BackColor.setter
    def BackColor(self, value:'Color'):
        GetDllLibDoc().ParagraphFormat_set_BackColor.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().ParagraphFormat_set_BackColor(self.Ptr, value.Ptr)

    @property
    def IsColumnBreakAfter(self)->bool:
        """

        """
        GetDllLibDoc().ParagraphFormat_get_IsColumnBreakAfter.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_IsColumnBreakAfter.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_IsColumnBreakAfter(self.Ptr)
        return ret

    @IsColumnBreakAfter.setter
    def IsColumnBreakAfter(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_IsColumnBreakAfter.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_IsColumnBreakAfter(self.Ptr, value)

    @property
    def LineSpacing(self)->float:
        """
    <summary>
        Returns or sets line spacing property of the paragraph.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_LineSpacing.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_LineSpacing.restype=c_float
        ret = GetDllLibDoc().ParagraphFormat_get_LineSpacing(self.Ptr)
        return ret

    @LineSpacing.setter
    def LineSpacing(self, value:float):
        GetDllLibDoc().ParagraphFormat_set_LineSpacing.argtypes=[c_void_p, c_float]
        GetDllLibDoc().ParagraphFormat_set_LineSpacing(self.Ptr, value)

    @property

    def LineSpacingRule(self)->'LineSpacingRule':
        """
    <summary>
        Returns or sets line spacing rule property of the paragraph.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_LineSpacingRule.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_LineSpacingRule.restype=c_int
        ret = GetDllLibDoc().ParagraphFormat_get_LineSpacingRule(self.Ptr)
        objwraped = LineSpacingRule(ret)
        return objwraped

    @LineSpacingRule.setter
    def LineSpacingRule(self, value:'LineSpacingRule'):
        GetDllLibDoc().ParagraphFormat_set_LineSpacingRule.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ParagraphFormat_set_LineSpacingRule(self.Ptr, value.value)

    @property
    def BeforeAutoSpacing(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether spacing before is automatic.
    </summary>
<value>if spacing before is automatic, set to <c>true</c>.</value>
        """
        GetDllLibDoc().ParagraphFormat_get_BeforeAutoSpacing.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_BeforeAutoSpacing.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_BeforeAutoSpacing(self.Ptr)
        return ret

    @BeforeAutoSpacing.setter
    def BeforeAutoSpacing(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_BeforeAutoSpacing.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_BeforeAutoSpacing(self.Ptr, value)

    @property
    def AfterAutoSpacing(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether spacing after is automatic.
    </summary>
<value>if spacing after is automatic, set to <c>true</c>.</value>
        """
        GetDllLibDoc().ParagraphFormat_get_AfterAutoSpacing.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_AfterAutoSpacing.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_AfterAutoSpacing(self.Ptr)
        return ret

    @AfterAutoSpacing.setter
    def AfterAutoSpacing(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_AfterAutoSpacing.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_AfterAutoSpacing(self.Ptr, value)

    @property
    def SnapToGrid(self)->bool:
        """
    <summary>
        Gets or sets a value specifies whether the current paragraph snaps to grid when document grid is defined.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_SnapToGrid.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_SnapToGrid.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_SnapToGrid(self.Ptr)
        return ret

    @SnapToGrid.setter
    def SnapToGrid(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_SnapToGrid.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_SnapToGrid(self.Ptr, value)

    @property

    def OutlineLevel(self)->'OutlineLevel':
        """
    <summary>
        Gets or sets the outline level.
    </summary>
<value>The outline level.</value>
        """
        GetDllLibDoc().ParagraphFormat_get_OutlineLevel.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_OutlineLevel.restype=c_int
        ret = GetDllLibDoc().ParagraphFormat_get_OutlineLevel(self.Ptr)
        objwraped = OutlineLevel(ret)
        return objwraped

    @OutlineLevel.setter
    def OutlineLevel(self, value:'OutlineLevel'):
        GetDllLibDoc().ParagraphFormat_set_OutlineLevel.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ParagraphFormat_set_OutlineLevel(self.Ptr, value.value)

    @property
    def OverflowPunc(self)->bool:
        """
    <summary>
        Gets or set allow punctuation to extend past text extents.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_OverflowPunc.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_OverflowPunc.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_OverflowPunc(self.Ptr)
        return ret

    @OverflowPunc.setter
    def OverflowPunc(self, value:bool):
        GetDllLibDoc().ParagraphFormat_set_OverflowPunc.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ParagraphFormat_set_OverflowPunc(self.Ptr, value)

    @property
    def IsFrame(self)->bool:
        """
    <summary>
        Gets a value indicating whether this instance is frame.
    </summary>
        """
        GetDllLibDoc().ParagraphFormat_get_IsFrame.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_IsFrame.restype=c_bool
        ret = GetDllLibDoc().ParagraphFormat_get_IsFrame(self.Ptr)
        return ret

    @property

    def Frame(self)->'Frame':
        """

        """
        GetDllLibDoc().ParagraphFormat_get_Frame.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphFormat_get_Frame.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphFormat_get_Frame(self.Ptr)
        ret = None if intPtr==None else Frame(intPtr)
        return ret


