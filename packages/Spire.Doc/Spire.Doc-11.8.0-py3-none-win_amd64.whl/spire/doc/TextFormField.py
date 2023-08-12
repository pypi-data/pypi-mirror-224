from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextFormField (  FormField, ITextRange) :
    """

    """
    @dispatch
    def __init__(self, doc:IDocument):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().TextFormField_CreateTextFormFieldD.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_CreateTextFormFieldD.restype=c_void_p
        intPtr = GetDllLibDoc().TextFormField_CreateTextFormFieldD(intPdoc)
        super(TextFormField, self).__init__(intPtr)
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().TextFormField_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().TextFormField_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def TextFieldType(self)->'TextFormFieldType':
        """
    <summary>
        Get/sets text form field type.
    </summary>
        """
        GetDllLibDoc().TextFormField_get_TextFieldType.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_TextFieldType.restype=c_int
        ret = GetDllLibDoc().TextFormField_get_TextFieldType(self.Ptr)
        objwraped = TextFormFieldType(ret)
        return objwraped

    @TextFieldType.setter
    def TextFieldType(self, value:'TextFormFieldType'):
        GetDllLibDoc().TextFormField_set_TextFieldType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().TextFormField_set_TextFieldType(self.Ptr, value.value)

    @property

    def StringFormat(self)->str:
        """
    <summary>
        Gets or sets string text format (text, date/time, number) directly.
    </summary>
        """
        GetDllLibDoc().TextFormField_get_StringFormat.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_StringFormat.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().TextFormField_get_StringFormat(self.Ptr))
        return ret


    @StringFormat.setter
    def StringFormat(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextFormField_set_StringFormat.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().TextFormField_set_StringFormat(self.Ptr, valuePtr)

    @property

    def DefaultText(self)->str:
        """
    <summary>
        Gets or sets default text for text form field.
    </summary>
        """
        GetDllLibDoc().TextFormField_get_DefaultText.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_DefaultText.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().TextFormField_get_DefaultText(self.Ptr))
        return ret


    @DefaultText.setter
    def DefaultText(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextFormField_set_DefaultText.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().TextFormField_set_DefaultText(self.Ptr, valuePtr)

    @property
    def MaximumLength(self)->int:
        """
    <summary>
        Gets or sets maximum text length.
    </summary>
        """
        GetDllLibDoc().TextFormField_get_MaximumLength.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_MaximumLength.restype=c_int
        ret = GetDllLibDoc().TextFormField_get_MaximumLength(self.Ptr)
        return ret

    @MaximumLength.setter
    def MaximumLength(self, value:int):
        GetDllLibDoc().TextFormField_set_MaximumLength.argtypes=[c_void_p, c_int]
        GetDllLibDoc().TextFormField_set_MaximumLength(self.Ptr, value)

    @property

    def TextRange(self)->'TextRange':
        """
    <summary>
        Gets or sets form field text range;
    </summary>
        """
        GetDllLibDoc().TextFormField_get_TextRange.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_TextRange.restype=c_void_p
        intPtr = GetDllLibDoc().TextFormField_get_TextRange(self.Ptr)
        ret = None if intPtr==None else TextRange(intPtr)
        return ret


    @TextRange.setter
    def TextRange(self, value:'TextRange'):
        GetDllLibDoc().TextFormField_set_TextRange.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().TextFormField_set_TextRange(self.Ptr, value.Ptr)

    @property

    def Text(self)->str:
        """
    <summary>
        Returns or setsthe text of text form field.
    </summary>
<value></value>
        """
        GetDllLibDoc().TextFormField_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_Text.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().TextFormField_get_Text(self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextFormField_set_Text.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().TextFormField_set_Text(self.Ptr, valuePtr)

