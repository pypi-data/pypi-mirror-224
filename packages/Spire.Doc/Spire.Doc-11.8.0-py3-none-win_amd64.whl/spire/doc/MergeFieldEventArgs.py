from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MergeFieldEventArgs (SpireObject) :
    """
    <summary>
        Represents data during MergeField event.
    </summary>
    """
    @property

    def Document(self)->'IDocument':
        """

        """
        GetDllLibDoc().MergeFieldEventArgs_get_Document.argtypes=[c_void_p]
        GetDllLibDoc().MergeFieldEventArgs_get_Document.restype=c_void_p
        intPtr = GetDllLibDoc().MergeFieldEventArgs_get_Document(self.Ptr)
        ret = None if intPtr==None else IDocument(intPtr)
        return ret


    @property

    def FieldName(self)->str:
        """

        """
        GetDllLibDoc().MergeFieldEventArgs_get_FieldName.argtypes=[c_void_p]
        GetDllLibDoc().MergeFieldEventArgs_get_FieldName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeFieldEventArgs_get_FieldName(self.Ptr))
        return ret


    @property

    def FieldValue(self)->'SpireObject':
        """

        """
        GetDllLibDoc().MergeFieldEventArgs_get_FieldValue.argtypes=[c_void_p]
        GetDllLibDoc().MergeFieldEventArgs_get_FieldValue.restype=c_void_p
        intPtr = GetDllLibDoc().MergeFieldEventArgs_get_FieldValue(self.Ptr)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret


    @property

    def TableName(self)->str:
        """

        """
        GetDllLibDoc().MergeFieldEventArgs_get_TableName.argtypes=[c_void_p]
        GetDllLibDoc().MergeFieldEventArgs_get_TableName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeFieldEventArgs_get_TableName(self.Ptr))
        return ret


    @property
    def RowIndex(self)->int:
        """

        """
        GetDllLibDoc().MergeFieldEventArgs_get_RowIndex.argtypes=[c_void_p]
        GetDllLibDoc().MergeFieldEventArgs_get_RowIndex.restype=c_int
        ret = GetDllLibDoc().MergeFieldEventArgs_get_RowIndex(self.Ptr)
        return ret

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """

        """
        GetDllLibDoc().MergeFieldEventArgs_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().MergeFieldEventArgs_get_CharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().MergeFieldEventArgs_get_CharacterFormat(self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def Text(self)->str:
        """

        """
        GetDllLibDoc().MergeFieldEventArgs_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().MergeFieldEventArgs_get_Text.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeFieldEventArgs_get_Text(self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().MergeFieldEventArgs_set_Text.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().MergeFieldEventArgs_set_Text(self.Ptr, valuePtr)

    @property

    def CurrentMergeField(self)->'IMergeField':
        """

        """
        GetDllLibDoc().MergeFieldEventArgs_get_CurrentMergeField.argtypes=[c_void_p]
        GetDllLibDoc().MergeFieldEventArgs_get_CurrentMergeField.restype=c_void_p
        intPtr = GetDllLibDoc().MergeFieldEventArgs_get_CurrentMergeField(self.Ptr)
        ret = None if intPtr==None else IMergeField(intPtr)
        return ret


    @property
    def IsKeepTextFormat(self)->bool:
        """

        """
        GetDllLibDoc().MergeFieldEventArgs_get_IsKeepTextFormat.argtypes=[c_void_p]
        GetDllLibDoc().MergeFieldEventArgs_get_IsKeepTextFormat.restype=c_bool
        ret = GetDllLibDoc().MergeFieldEventArgs_get_IsKeepTextFormat(self.Ptr)
        return ret

    @IsKeepTextFormat.setter
    def IsKeepTextFormat(self, value:bool):
        GetDllLibDoc().MergeFieldEventArgs_set_IsKeepTextFormat.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().MergeFieldEventArgs_set_IsKeepTextFormat(self.Ptr, value)

    @property
    def IsKeepHtmlTextFormat(self)->bool:
        """
    <summary>
        Gets or sets if keep html text formatting.
    </summary>
        """
        GetDllLibDoc().MergeFieldEventArgs_get_IsKeepHtmlTextFormat.argtypes=[c_void_p]
        GetDllLibDoc().MergeFieldEventArgs_get_IsKeepHtmlTextFormat.restype=c_bool
        ret = GetDllLibDoc().MergeFieldEventArgs_get_IsKeepHtmlTextFormat(self.Ptr)
        return ret

    @IsKeepHtmlTextFormat.setter
    def IsKeepHtmlTextFormat(self, value:bool):
        GetDllLibDoc().MergeFieldEventArgs_set_IsKeepHtmlTextFormat.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().MergeFieldEventArgs_set_IsKeepHtmlTextFormat(self.Ptr, value)

