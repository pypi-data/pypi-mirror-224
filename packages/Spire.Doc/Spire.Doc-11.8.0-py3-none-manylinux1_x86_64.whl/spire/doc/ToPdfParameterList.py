from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ToPdfParameterList (SpireObject) :
    """

    """
    @dispatch
    def __init__(self):
        GetDllLibDoc().ToPdfParameterList_CreateToPdfParameterList.restype=c_void_p
        intPtr = GetDllLibDoc().ToPdfParameterList_CreateToPdfParameterList()
        super(ToPdfParameterList, self).__init__(intPtr)
    @property
    def MimicWPSLayout(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to mimic the layout of WPS Application.
            The default value is false.
    </summary>
        """
        GetDllLibDoc().ToPdfParameterList_get_MimicWPSLayout.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_MimicWPSLayout.restype=c_bool
        ret = GetDllLibDoc().ToPdfParameterList_get_MimicWPSLayout(self.Ptr)
        return ret

    @MimicWPSLayout.setter
    def MimicWPSLayout(self, value:bool):
        GetDllLibDoc().ToPdfParameterList_set_MimicWPSLayout.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ToPdfParameterList_set_MimicWPSLayout(self.Ptr, value)

    @property
    def UpdateFields(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to change the fields before 
            saving the document when using the new engine.
            The default value is true.
    </summary>
        """
        GetDllLibDoc().ToPdfParameterList_get_UpdateFields.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_UpdateFields.restype=c_bool
        ret = GetDllLibDoc().ToPdfParameterList_get_UpdateFields(self.Ptr)
        return ret

    @UpdateFields.setter
    def UpdateFields(self, value:bool):
        GetDllLibDoc().ToPdfParameterList_set_UpdateFields.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ToPdfParameterList_set_UpdateFields(self.Ptr, value)

    @property
    def UsePSCoversion(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether use the PS conversion.
    </summary>
<value>
  <c>true</c> if use the PS conversion;otherwise,<c>false</c>.</value>
        """
        GetDllLibDoc().ToPdfParameterList_get_UsePSCoversion.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_UsePSCoversion.restype=c_bool
        ret = GetDllLibDoc().ToPdfParameterList_get_UsePSCoversion(self.Ptr)
        return ret

    @UsePSCoversion.setter
    def UsePSCoversion(self, value:bool):
        GetDllLibDoc().ToPdfParameterList_set_UsePSCoversion.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ToPdfParameterList_set_UsePSCoversion(self.Ptr, value)

    @property
    def IsHidden(self)->bool:
        """
    <summary>
        Gets or sets hidden text is converted.
    </summary>
        """
        GetDllLibDoc().ToPdfParameterList_get_IsHidden.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_IsHidden.restype=c_bool
        ret = GetDllLibDoc().ToPdfParameterList_get_IsHidden(self.Ptr)
        return ret

    @IsHidden.setter
    def IsHidden(self, value:bool):
        GetDllLibDoc().ToPdfParameterList_set_IsHidden.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ToPdfParameterList_set_IsHidden(self.Ptr, value)

#    @property
#
#    def EmbeddedFontNameList(self)->'List1':
#        """
#    <summary>
#        Gets or sets Embedded into the PDF document font name.
#    </summary>
#        """
#        GetDllLibDoc().ToPdfParameterList_get_EmbeddedFontNameList.argtypes=[c_void_p]
#        GetDllLibDoc().ToPdfParameterList_get_EmbeddedFontNameList.restype=c_void_p
#        intPtr = GetDllLibDoc().ToPdfParameterList_get_EmbeddedFontNameList(self.Ptr)
#        ret = None if intPtr==None else List1(intPtr)
#        return ret
#


#    @EmbeddedFontNameList.setter
#    def EmbeddedFontNameList(self, value:'List1'):
#        GetDllLibDoc().ToPdfParameterList_set_EmbeddedFontNameList.argtypes=[c_void_p, c_void_p]
#        GetDllLibDoc().ToPdfParameterList_set_EmbeddedFontNameList(self.Ptr, value.Ptr)


    @property
    def IsEmbeddedAllFonts(self)->bool:
        """
    <summary>
        Gets or sets all fonts are embedded in the PDF document.
    </summary>
        """
        GetDllLibDoc().ToPdfParameterList_get_IsEmbeddedAllFonts.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_IsEmbeddedAllFonts.restype=c_bool
        ret = GetDllLibDoc().ToPdfParameterList_get_IsEmbeddedAllFonts(self.Ptr)
        return ret

    @IsEmbeddedAllFonts.setter
    def IsEmbeddedAllFonts(self, value:bool):
        GetDllLibDoc().ToPdfParameterList_set_IsEmbeddedAllFonts.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ToPdfParameterList_set_IsEmbeddedAllFonts(self.Ptr, value)

    @property
    def DisableLink(self)->bool:
        """
    <summary>
        gets or sets whether remove the link on the hyperlink and keep the character format
            during converting to pdf. 
    </summary>
        """
        GetDllLibDoc().ToPdfParameterList_get_DisableLink.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_DisableLink.restype=c_bool
        ret = GetDllLibDoc().ToPdfParameterList_get_DisableLink(self.Ptr)
        return ret

    @DisableLink.setter
    def DisableLink(self, value:bool):
        GetDllLibDoc().ToPdfParameterList_set_DisableLink.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ToPdfParameterList_set_DisableLink(self.Ptr, value)

    @property
    def IsAtLast(self)->bool:
        """
    <summary>
        Gets or sets To Pdf TextBox HeightType.The default is "Exactly".
    </summary>
        """
        GetDllLibDoc().ToPdfParameterList_get_IsAtLast.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_IsAtLast.restype=c_bool
        ret = GetDllLibDoc().ToPdfParameterList_get_IsAtLast(self.Ptr)
        return ret

    @IsAtLast.setter
    def IsAtLast(self, value:bool):
        GetDllLibDoc().ToPdfParameterList_set_IsAtLast.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ToPdfParameterList_set_IsAtLast(self.Ptr, value)

    @property

    def PdfConformanceLevel(self)->'PdfConformanceLevel':
        """
    <summary>
        Gets or sets the Pdf document's Conformance-level.
    </summary>
        """
        GetDllLibDoc().ToPdfParameterList_get_PdfConformanceLevel.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_PdfConformanceLevel.restype=c_int
        ret = GetDllLibDoc().ToPdfParameterList_get_PdfConformanceLevel(self.Ptr)
        objwraped = PdfConformanceLevel(ret)
        return objwraped


    @PdfConformanceLevel.setter
    def PdfConformanceLevel(self, value:'PdfConformanceLevel'):
        GetDllLibDoc().ToPdfParameterList_set_PdfConformanceLevel.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ToPdfParameterList_set_PdfConformanceLevel(self.Ptr, value.value)


    @property

    def PdfSecurity(self)->'PdfSecurity':
        """
    <summary>
        Represents the security settings of the PDF document.
    </summary>
        """
        GetDllLibDoc().ToPdfParameterList_get_PdfSecurity.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_PdfSecurity.restype=c_void_p
        intPtr = GetDllLibDoc().ToPdfParameterList_get_PdfSecurity(self.Ptr)
        ret = None if intPtr==None else PdfSecurity(intPtr)
        return ret



    @property

    def PrivateFontPaths(self)->List[PrivateFontPath]:
        """
    <summary>
        Gets or sets the private font paths.
    </summary>
        """
        GetDllLibDoc().ToPdfParameterList_get_PrivateFontPaths.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_PrivateFontPaths.restype=IntPtrArray
        intPtrArray = GetDllLibDoc().ToPdfParameterList_get_PrivateFontPaths(self.Ptr)
        ret = GetVectorFromArray(intPtrArray,c_void_p)
        return ret



    @PrivateFontPaths.setter
    def PrivateFontPaths(self, fontPathList:List[PrivateFontPath]):
        countFontPath = len(fontPathList)
        ArrayFontPaths = c_void_p * countFontPath
        arrayFontPaths = ArrayFontPaths()
        for i in range(0, countFontPath):
            arrayFontPaths[i] = fontPathList[i].Ptr
        GetDllLibDoc().ToPdfParameterList_set_PrivateFontPaths.argtypes=[c_void_p, ArrayFontPaths,c_int]
        GetDllLibDoc().ToPdfParameterList_set_PrivateFontPaths(self.Ptr, arrayFontPaths,countFontPath)


    @property
    def CreateWordBookmarksUsingHeadings(self)->bool:
        """
    <summary>
        Gets or set the a value that determines whether create the bookmarks using Headings.
    </summary>
        """
        GetDllLibDoc().ToPdfParameterList_get_CreateWordBookmarksUsingHeadings.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_CreateWordBookmarksUsingHeadings.restype=c_bool
        ret = GetDllLibDoc().ToPdfParameterList_get_CreateWordBookmarksUsingHeadings(self.Ptr)
        return ret

    @CreateWordBookmarksUsingHeadings.setter
    def CreateWordBookmarksUsingHeadings(self, value:bool):
        GetDllLibDoc().ToPdfParameterList_set_CreateWordBookmarksUsingHeadings.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ToPdfParameterList_set_CreateWordBookmarksUsingHeadings(self.Ptr, value)

    @property
    def CreateWordBookmarks(self)->bool:
        """
    <summary>
        Gets or set the a value, Whether to use word bookmars when create the bookmarks.
    </summary>
        """
        GetDllLibDoc().ToPdfParameterList_get_CreateWordBookmarks.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_CreateWordBookmarks.restype=c_bool
        ret = GetDllLibDoc().ToPdfParameterList_get_CreateWordBookmarks(self.Ptr)
        return ret

    @CreateWordBookmarks.setter
    def CreateWordBookmarks(self, value:bool):
        GetDllLibDoc().ToPdfParameterList_set_CreateWordBookmarks.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ToPdfParameterList_set_CreateWordBookmarks(self.Ptr, value)

    @property

    def WordBookmarksTitle(self)->str:
        """
    <summary>
        Gets or sets the word bookmarks title. The default value for this title is null.
    </summary>
<value>The word bookmarks title.</value>
        """
        GetDllLibDoc().ToPdfParameterList_get_WordBookmarksTitle.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_WordBookmarksTitle.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().ToPdfParameterList_get_WordBookmarksTitle(self.Ptr))
        return ret


    @WordBookmarksTitle.setter
    def WordBookmarksTitle(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().ToPdfParameterList_set_WordBookmarksTitle.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().ToPdfParameterList_set_WordBookmarksTitle(self.Ptr, valuePtr)

    @property

    def WordBookmarksColor(self)->'Color':
        """
    <summary>
        Gets or sets the text color of the word bookmarks.
            the default value is the "SaddleBrown" color(#FF8B4513).
    </summary>
<value>The text color of the word boomarks. </value>
        """
        GetDllLibDoc().ToPdfParameterList_get_WordBookmarksColor.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_WordBookmarksColor.restype=c_void_p
        intPtr = GetDllLibDoc().ToPdfParameterList_get_WordBookmarksColor(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @WordBookmarksColor.setter
    def WordBookmarksColor(self, value:'Color'):
        GetDllLibDoc().ToPdfParameterList_set_WordBookmarksColor.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().ToPdfParameterList_set_WordBookmarksColor(self.Ptr, value.Ptr)

    @property

    def WordBookmarksTextStyle(self)->'BookmarkTextStyle':
        """
    <summary>
        Gets or sets the text style of the word bookmarks.
            The default value is the Bold.
    </summary>
<value>The word bookmarks text style.</value>
        """
        GetDllLibDoc().ToPdfParameterList_get_WordBookmarksTextStyle.argtypes=[c_void_p]
        GetDllLibDoc().ToPdfParameterList_get_WordBookmarksTextStyle.restype=c_int
        ret = GetDllLibDoc().ToPdfParameterList_get_WordBookmarksTextStyle(self.Ptr)
        objwraped = BookmarkTextStyle(ret)
        return objwraped

    @WordBookmarksTextStyle.setter
    def WordBookmarksTextStyle(self, value:'BookmarkTextStyle'):
        GetDllLibDoc().ToPdfParameterList_set_WordBookmarksTextStyle.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ToPdfParameterList_set_WordBookmarksTextStyle(self.Ptr, value.value)

