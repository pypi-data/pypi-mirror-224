from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MergeField (  Field, IMergeField) :
    """

    """
    @dispatch
    def __init__(self, doc:IDocument):
       intPdoc:c_void_p =  doc.Ptr

       GetDllLibDoc().MergeField_CreateMergeFieldD.argtypes=[c_void_p]
       GetDllLibDoc().MergeField_CreateMergeFieldD.restype=c_void_p
       intPtr = GetDllLibDoc().MergeField_CreateMergeFieldD(intPdoc)
       super(MergeField, self).__init__(intPtr)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
    <value>The type of the document object.</value>
        """
        GetDllLibDoc().MergeField_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().MergeField_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def FieldName(self)->str:
        """
    <summary>
        Returns or sets field name
    </summary>
        """
        GetDllLibDoc().MergeField_get_FieldName.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_FieldName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeField_get_FieldName(self.Ptr))
        return ret


    @FieldName.setter
    def FieldName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().MergeField_set_FieldName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().MergeField_set_FieldName(self.Ptr, valuePtr)

    @property

    def Text(self)->str:
        """

        """
        GetDllLibDoc().MergeField_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_Text.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeField_get_Text(self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().MergeField_set_Text.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().MergeField_set_Text(self.Ptr, valuePtr)

    @property

    def TextBefore(self)->str:
        """
    <summary>
        Returns or sets the text before merge field
    </summary>
        """
        GetDllLibDoc().MergeField_get_TextBefore.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_TextBefore.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeField_get_TextBefore(self.Ptr))
        return ret


    @TextBefore.setter
    def TextBefore(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().MergeField_set_TextBefore.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().MergeField_set_TextBefore(self.Ptr, valuePtr)

    @property

    def TextAfter(self)->str:
        """
    <summary>
        Returns or sets the text after merge field
    </summary>
        """
        GetDllLibDoc().MergeField_get_TextAfter.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_TextAfter.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeField_get_TextAfter(self.Ptr))
        return ret


    @TextAfter.setter
    def TextAfter(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().MergeField_set_TextAfter.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().MergeField_set_TextAfter(self.Ptr, valuePtr)

    @property

    def Prefix(self)->str:
        """
    <summary>
        Gets the prefix of merge field.
    </summary>
        """
        GetDllLibDoc().MergeField_get_Prefix.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_Prefix.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeField_get_Prefix(self.Ptr))
        return ret


    @property

    def NumberFormat(self)->str:
        """
    <summary>
        Gets the number format.
    </summary>
        """
        GetDllLibDoc().MergeField_get_NumberFormat.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_NumberFormat.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeField_get_NumberFormat(self.Ptr))
        return ret


    @property

    def DateFormat(self)->str:
        """
    <summary>
        Gets the date format.
    </summary>
        """
        GetDllLibDoc().MergeField_get_DateFormat.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_DateFormat.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeField_get_DateFormat(self.Ptr))
        return ret


    @property

    def TextItems(self)->'ParagraphItemCollection':
        """
    <summary>
        Gets the text items.
    </summary>
<value>The text items.</value>
        """
        GetDllLibDoc().MergeField_get_TextItems.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_TextItems.restype=c_void_p
        intPtr = GetDllLibDoc().MergeField_get_TextItems(self.Ptr)
        ret = None if intPtr==None else ParagraphItemCollection(intPtr)
        return ret


