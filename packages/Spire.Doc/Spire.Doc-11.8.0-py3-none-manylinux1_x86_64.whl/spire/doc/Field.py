from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Field (  TextRange, IField) :
    """

    """
    @dispatch
    def __init__(self, doc:'IDocument'):
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().Field_CreateFieldD.argtypes=[c_void_p]
        GetDllLibDoc().Field_CreateFieldD.restype=c_void_p
        intPtr = GetDllLibDoc().Field_CreateFieldD(intPdoc)
        super(Field, self).__init__(intPtr)

    @property
    def IsLocked(self)->bool:
        """
    <summary>
        Gets or sets the lock property of the filed.if the field is locked,the field can't be updated.
    </summary>
        """
        GetDllLibDoc().Field_get_IsLocked.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_IsLocked.restype=c_bool
        ret = GetDllLibDoc().Field_get_IsLocked(self.Ptr)
        return ret

    @IsLocked.setter
    def IsLocked(self, value:bool):
        GetDllLibDoc().Field_set_IsLocked.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Field_set_IsLocked(self.Ptr, value)

    @property

    def TextFormat(self)->'TextFormat':
        """
    <summary>
        Gets or sets regular text format.
    </summary>
        """
        GetDllLibDoc().Field_get_TextFormat.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_TextFormat.restype=c_int
        ret = GetDllLibDoc().Field_get_TextFormat(self.Ptr)
        objwraped = TextFormat(ret)
        return objwraped

    @TextFormat.setter
    def TextFormat(self, value:'TextFormat'):
        GetDllLibDoc().Field_set_TextFormat.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Field_set_TextFormat(self.Ptr, value.value)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().Field_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().Field_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Pattern(self)->str:
        """
    <summary>
        Returns or sets field pattern.
    </summary>
        """
        GetDllLibDoc().Field_get_Pattern.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_Pattern.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Field_get_Pattern(self.Ptr))
        return ret


    @Pattern.setter
    def Pattern(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Field_set_Pattern.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Field_set_Pattern(self.Ptr, valuePtr)

    @property

    def Value(self)->str:
        """
    <summary>
        Gets the field value.
    </summary>
<value>The field value.</value>
        """
        GetDllLibDoc().Field_get_Value.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_Value.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Field_get_Value(self.Ptr))
        return ret


    @property

    def Type(self)->'FieldType':
        """
    <summary>
        Returns or sets field type
    </summary>
<value></value>
        """
        GetDllLibDoc().Field_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_Type.restype=c_int
        ret = GetDllLibDoc().Field_get_Type(self.Ptr)
        objwraped = FieldType(ret)
        return objwraped

    @Type.setter
    def Type(self, value:'FieldType'):
        GetDllLibDoc().Field_set_Type.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Field_set_Type(self.Ptr, value.value)

    @property

    def Code(self)->str:
        """
    <summary>
        Gets or sets the field code.
    </summary>
<value>The field code.</value>
        """
        GetDllLibDoc().Field_get_Code.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_Code.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Field_get_Code(self.Ptr))
        return ret


    @Code.setter
    def Code(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Field_set_Code.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Field_set_Code(self.Ptr, valuePtr)

    @property

    def Separator(self)->'FieldMark':
        """
    <summary>
        Gets or sets the field separator.
    </summary>
<value>The field separator.</value>
        """
        GetDllLibDoc().Field_get_Separator.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_Separator.restype=c_void_p
        intPtr = GetDllLibDoc().Field_get_Separator(self.Ptr)
        from spire.doc import FieldMark
        ret = None if intPtr==None else FieldMark(intPtr)
        return ret


    @property

    def End(self)->'FieldMark':
        """
    <summary>
        Gets or sets the field end.
    </summary>
<value>The field mark,Type of FieldEnd. </value>
        """
        GetDllLibDoc().Field_get_End.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_End.restype=c_void_p
        intPtr = GetDllLibDoc().Field_get_End(self.Ptr)
        from spire.doc import FieldMark
        ret = None if intPtr==None else FieldMark(intPtr)
        return ret


    @End.setter
    def End(self, value:'FieldMark'):
        GetDllLibDoc().Field_set_End.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().Field_set_End(self.Ptr, value.Ptr)

    @property

    def FieldText(self)->str:
        """
    <summary>
        Gets or Sets Filed Displays text information.
    </summary>
        """
        GetDllLibDoc().Field_get_FieldText.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_FieldText.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Field_get_FieldText(self.Ptr))
        return ret


    @FieldText.setter
    def FieldText(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Field_set_FieldText.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Field_set_FieldText(self.Ptr, valuePtr)

    def Update(self):
        """
    <summary>
        Update the result of the field.
            Can only be simpler field.
            Direct calls cannot update the NumPages field and Page field, ect.
    </summary>
        """
        GetDllLibDoc().Field_Update.argtypes=[c_void_p]
        GetDllLibDoc().Field_Update(self.Ptr)

