from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BuiltinDocumentProperties (  SummaryDocumentProperties) :
    """

    """
    @property

    def Category(self)->str:
        """
    <summary>
        Gets or sets the category of the document.
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_Category.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_Category.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().BuiltinDocumentProperties_get_Category(self.Ptr))
        return ret


    @Category.setter
    def Category(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().BuiltinDocumentProperties_set_Category.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().BuiltinDocumentProperties_set_Category(self.Ptr, valuePtr)

    @property
    def BytesCount(self)->int:
        """
    <summary>
        Gets the number of bytes in the document.
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_BytesCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_BytesCount.restype=c_int
        ret = GetDllLibDoc().BuiltinDocumentProperties_get_BytesCount(self.Ptr)
        return ret

    @property
    def LinesCount(self)->int:
        """
    <summary>
        Gets the number of lines in the document.
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_LinesCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_LinesCount.restype=c_int
        ret = GetDllLibDoc().BuiltinDocumentProperties_get_LinesCount(self.Ptr)
        return ret

    @property
    def ParagraphCount(self)->int:
        """
    <summary>
        Gets the number of paragraphs in the document.
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_ParagraphCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_ParagraphCount.restype=c_int
        ret = GetDllLibDoc().BuiltinDocumentProperties_get_ParagraphCount(self.Ptr)
        return ret

    @property
    def CharCountWithSpace(self)->int:
        """
    <summary>
        Gets document characters count(including spaces)
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_CharCountWithSpace.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_CharCountWithSpace.restype=c_int
        ret = GetDllLibDoc().BuiltinDocumentProperties_get_CharCountWithSpace(self.Ptr)
        return ret

    @property
    def SlideCount(self)->int:
        """
    <summary>
        Gets slide count.
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_SlideCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_SlideCount.restype=c_int
        ret = GetDllLibDoc().BuiltinDocumentProperties_get_SlideCount(self.Ptr)
        return ret

    @property
    def NoteCount(self)->int:
        """
    <summary>
        Gets Note count.
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_NoteCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_NoteCount.restype=c_int
        ret = GetDllLibDoc().BuiltinDocumentProperties_get_NoteCount(self.Ptr)
        return ret

    @property
    def HiddenCount(self)->int:
        """
    <summary>
        Gets hidden count
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_HiddenCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_HiddenCount.restype=c_int
        ret = GetDllLibDoc().BuiltinDocumentProperties_get_HiddenCount(self.Ptr)
        return ret

    @property

    def Company(self)->str:
        """
    <summary>
        Returns or setsCompany property.
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_Company.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_Company.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().BuiltinDocumentProperties_get_Company(self.Ptr))
        return ret


    @Company.setter
    def Company(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().BuiltinDocumentProperties_set_Company.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().BuiltinDocumentProperties_set_Company(self.Ptr, valuePtr)

    @property

    def HyperLinkBase(self)->str:
        """
    <summary>
        Returns or sets HyperLinkBase property.
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_HyperLinkBase.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_HyperLinkBase.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().BuiltinDocumentProperties_get_HyperLinkBase(self.Ptr))
        return ret


    @HyperLinkBase.setter
    def HyperLinkBase(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().BuiltinDocumentProperties_set_HyperLinkBase.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().BuiltinDocumentProperties_set_HyperLinkBase(self.Ptr, valuePtr)

    @property

    def Manager(self)->str:
        """
    <summary>
        Gets or sets Manager property.
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_Manager.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_Manager.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().BuiltinDocumentProperties_get_Manager(self.Ptr))
        return ret


    @Manager.setter
    def Manager(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().BuiltinDocumentProperties_set_Manager.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().BuiltinDocumentProperties_set_Manager(self.Ptr, valuePtr)

    @property

    def ContentStatus(self)->str:
        """
    <summary>
        Gets or sets the document status.
    </summary>
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_ContentStatus.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_ContentStatus.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().BuiltinDocumentProperties_get_ContentStatus(self.Ptr))
        return ret


    @ContentStatus.setter
    def ContentStatus(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().BuiltinDocumentProperties_set_ContentStatus.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().BuiltinDocumentProperties_set_ContentStatus(self.Ptr, valuePtr)


    def Clone(self)->'BuiltinDocumentProperties':
        """

        """
        GetDllLibDoc().BuiltinDocumentProperties_Clone.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().BuiltinDocumentProperties_Clone(self.Ptr)
        ret = None if intPtr==None else BuiltinDocumentProperties(intPtr)
        return ret


