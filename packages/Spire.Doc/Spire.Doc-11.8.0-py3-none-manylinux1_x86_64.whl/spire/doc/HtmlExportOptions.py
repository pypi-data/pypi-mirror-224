from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HtmlExportOptions (SpireObject) :
    """

    """
    @property
    def EPubExportFont(self)->bool:
        """

        """
        GetDllLibDoc().HtmlExportOptions_get_EPubExportFont.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_EPubExportFont.restype=c_bool
        ret = GetDllLibDoc().HtmlExportOptions_get_EPubExportFont(self.Ptr)
        return ret

    @EPubExportFont.setter
    def EPubExportFont(self, value:bool):
        GetDllLibDoc().HtmlExportOptions_set_EPubExportFont.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().HtmlExportOptions_set_EPubExportFont(self.Ptr, value)

    @property

    def CssStyleSheetType(self)->'CssStyleSheetType':
        """
    <summary>
        Gets or sets the type of the HTML export CSS style sheet.
    </summary>
<value>The type of the HTML export CSS style sheet.</value>
        """
        GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetType.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetType.restype=c_int
        ret = GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetType(self.Ptr)
        objwraped = CssStyleSheetType(ret)
        return objwraped

    @CssStyleSheetType.setter
    def CssStyleSheetType(self, value:'CssStyleSheetType'):
        GetDllLibDoc().HtmlExportOptions_set_CssStyleSheetType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().HtmlExportOptions_set_CssStyleSheetType(self.Ptr, value.value)

    @property
    def ImageEmbedded(self)->bool:
        """
    <summary>
        If false,indicates exporting the image as a single file; 
            If true, embedding the image into the html code using Data URI scheme.
            The default value is false.
            Note: Internet Explorer 8 limits data URIs to a maximum length of 32KB.
    </summary>
<value>The value of the HTML export image style sheet.</value>
        """
        GetDllLibDoc().HtmlExportOptions_get_ImageEmbedded.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_ImageEmbedded.restype=c_bool
        ret = GetDllLibDoc().HtmlExportOptions_get_ImageEmbedded(self.Ptr)
        return ret

    @ImageEmbedded.setter
    def ImageEmbedded(self, value:bool):
        GetDllLibDoc().HtmlExportOptions_set_ImageEmbedded.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().HtmlExportOptions_set_ImageEmbedded(self.Ptr, value)

    @property
    def IsExportDocumentStyles(self)->bool:
        """
    <summary>
        Gets or Sets a switch that determines whether to export the document styles to head.
    </summary>
        """
        GetDllLibDoc().HtmlExportOptions_get_IsExportDocumentStyles.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_IsExportDocumentStyles.restype=c_bool
        ret = GetDllLibDoc().HtmlExportOptions_get_IsExportDocumentStyles(self.Ptr)
        return ret

    @IsExportDocumentStyles.setter
    def IsExportDocumentStyles(self, value:bool):
        GetDllLibDoc().HtmlExportOptions_set_IsExportDocumentStyles.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().HtmlExportOptions_set_IsExportDocumentStyles(self.Ptr, value)

    @property

    def CssStyleSheetFileName(self)->str:
        """
    <summary>
        Gets or sets the name of the HTML export CSS style sheet file.
    </summary>
<value>The name of the HTML export CSS style sheet file.</value>
        """
        GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetFileName.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetFileName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetFileName(self.Ptr))
        return ret


    @CssStyleSheetFileName.setter
    def CssStyleSheetFileName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().HtmlExportOptions_set_CssStyleSheetFileName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().HtmlExportOptions_set_CssStyleSheetFileName(self.Ptr, valuePtr)

    @property
    def HasHeadersFooters(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether HTML export headers footers.
    </summary>
        """
        GetDllLibDoc().HtmlExportOptions_get_HasHeadersFooters.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_HasHeadersFooters.restype=c_bool
        ret = GetDllLibDoc().HtmlExportOptions_get_HasHeadersFooters(self.Ptr)
        return ret

    @HasHeadersFooters.setter
    def HasHeadersFooters(self, value:bool):
        GetDllLibDoc().HtmlExportOptions_set_HasHeadersFooters.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().HtmlExportOptions_set_HasHeadersFooters(self.Ptr, value)

    @property
    def IsTextInputFormFieldAsText(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether HTML export text input form field as text.
    </summary>
<value>
            	If HTML export text input form field as text, set to <c>true</c>.
            </value>
        """
        GetDllLibDoc().HtmlExportOptions_get_IsTextInputFormFieldAsText.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_IsTextInputFormFieldAsText.restype=c_bool
        ret = GetDllLibDoc().HtmlExportOptions_get_IsTextInputFormFieldAsText(self.Ptr)
        return ret

    @IsTextInputFormFieldAsText.setter
    def IsTextInputFormFieldAsText(self, value:bool):
        GetDllLibDoc().HtmlExportOptions_set_IsTextInputFormFieldAsText.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().HtmlExportOptions_set_IsTextInputFormFieldAsText(self.Ptr, value)

    @property

    def ImagesPath(self)->str:
        """
    <summary>
        Gets or sets the HTML export images folder.
    </summary>
<value>The HTML export images folder.</value>
        """
        GetDllLibDoc().HtmlExportOptions_get_ImagesPath.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_ImagesPath.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().HtmlExportOptions_get_ImagesPath(self.Ptr))
        return ret


    @ImagesPath.setter
    def ImagesPath(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().HtmlExportOptions_set_ImagesPath.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().HtmlExportOptions_set_ImagesPath(self.Ptr, valuePtr)

    @property
    def UseSaveFileRelativePath(self)->bool:
        """
    <summary>
         Gets or sets a value whether Image Path is relative to the file save path. 
    </summary>
<value>
            	If Image Path wants to be relative to the file save path, set to <c>true</c>.
            </value>
        """
        GetDllLibDoc().HtmlExportOptions_get_UseSaveFileRelativePath.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_UseSaveFileRelativePath.restype=c_bool
        ret = GetDllLibDoc().HtmlExportOptions_get_UseSaveFileRelativePath(self.Ptr)
        return ret

    @UseSaveFileRelativePath.setter
    def UseSaveFileRelativePath(self, value:bool):
        GetDllLibDoc().HtmlExportOptions_set_UseSaveFileRelativePath.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().HtmlExportOptions_set_UseSaveFileRelativePath(self.Ptr, value)

    @property
    def UseMsoSpace(self)->bool:
        """
    <summary>
         Gets or sets a switch that determines whether to use mso rules' space.. 
    </summary>
        """
        GetDllLibDoc().HtmlExportOptions_get_UseMsoSpace.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_UseMsoSpace.restype=c_bool
        ret = GetDllLibDoc().HtmlExportOptions_get_UseMsoSpace(self.Ptr)
        return ret

    @UseMsoSpace.setter
    def UseMsoSpace(self, value:bool):
        GetDllLibDoc().HtmlExportOptions_set_UseMsoSpace.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().HtmlExportOptions_set_UseMsoSpace(self.Ptr, value)

