from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CheckBoxFormField (  FormField, IDocumentObject) :
    """

    """
    @dispatch
    def __init__(self, doc:'IDocument'):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().CheckBoxFormField_CreateCheckBoxFormFieldD.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_CreateCheckBoxFormFieldD.restype=c_void_p
        intPtr = GetDllLibDoc().CheckBoxFormField_CreateCheckBoxFormFieldD(intPdoc)
        super(CheckBoxFormField, self).__init__(intPtr)
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().CheckBoxFormField_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().CheckBoxFormField_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def CheckBoxSize(self)->int:
        """
    <summary>
        Gets or sets size of checkbox.
    </summary>
        """
        GetDllLibDoc().CheckBoxFormField_get_CheckBoxSize.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_get_CheckBoxSize.restype=c_int
        ret = GetDllLibDoc().CheckBoxFormField_get_CheckBoxSize(self.Ptr)
        return ret

    @CheckBoxSize.setter
    def CheckBoxSize(self, value:int):
        GetDllLibDoc().CheckBoxFormField_set_CheckBoxSize.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CheckBoxFormField_set_CheckBoxSize(self.Ptr, value)

    @property
    def DefaultCheckBoxValue(self)->bool:
        """
    <summary>
        Gets or sets default checkbox value.
    </summary>
        """
        GetDllLibDoc().CheckBoxFormField_get_DefaultCheckBoxValue.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_get_DefaultCheckBoxValue.restype=c_bool
        ret = GetDllLibDoc().CheckBoxFormField_get_DefaultCheckBoxValue(self.Ptr)
        return ret

    @DefaultCheckBoxValue.setter
    def DefaultCheckBoxValue(self, value:bool):
        GetDllLibDoc().CheckBoxFormField_set_DefaultCheckBoxValue.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CheckBoxFormField_set_DefaultCheckBoxValue(self.Ptr, value)

    @property
    def Checked(self)->bool:
        """
    <summary>
        Gets or sets Checked property.
    </summary>
        """
        GetDllLibDoc().CheckBoxFormField_get_Checked.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_get_Checked.restype=c_bool
        ret = GetDllLibDoc().CheckBoxFormField_get_Checked(self.Ptr)
        return ret

    @Checked.setter
    def Checked(self, value:bool):
        GetDllLibDoc().CheckBoxFormField_set_Checked.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CheckBoxFormField_set_Checked(self.Ptr, value)

    @property

    def SizeType(self)->'CheckBoxSizeType':
        """
    <summary>
        Gets or sets check box size type.
    </summary>
        """
        GetDllLibDoc().CheckBoxFormField_get_SizeType.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_get_SizeType.restype=c_int
        ret = GetDllLibDoc().CheckBoxFormField_get_SizeType(self.Ptr)
        objwraped = CheckBoxSizeType(ret)
        return objwraped

    @SizeType.setter
    def SizeType(self, value:'CheckBoxSizeType'):
        GetDllLibDoc().CheckBoxFormField_set_SizeType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CheckBoxFormField_set_SizeType(self.Ptr, value.value)

