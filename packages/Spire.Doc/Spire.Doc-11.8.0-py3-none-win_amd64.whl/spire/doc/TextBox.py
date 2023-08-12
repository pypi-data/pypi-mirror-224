from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBox (  ShapeObject, ITextBox, ICompositeObject) :
    """

    """
    @dispatch
    def __init__(self, doc:IDocument):
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().TextBox_CreateTextBoxD.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_CreateTextBoxD.restype=c_void_p
        intPtr = GetDllLibDoc().TextBox_CreateTextBoxD(intPdoc)
        super(TextBox, self).__init__(intPtr)

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
    <summary>
        Gets the child entities.
    </summary>
<value>The child entities.</value>
        """
        GetDllLibDoc().TextBox_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().TextBox_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().TextBox_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().TextBox_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Format(self)->'TextBoxFormat':
        """
    <summary>
        Gets the format value.
    </summary>
        """
        GetDllLibDoc().TextBox_get_Format.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_get_Format.restype=c_void_p
        intPtr = GetDllLibDoc().TextBox_get_Format(self.Ptr)
        from spire.doc import TextBoxFormat
        ret = None if intPtr==None else TextBoxFormat(intPtr)
        return ret


    @property

    def Body(self)->'Body':
        """
    <summary>
        Get/set TextBody value
    </summary>
        """
        GetDllLibDoc().TextBox_get_Body.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_get_Body.restype=c_void_p
        intPtr = GetDllLibDoc().TextBox_get_Body(self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
    <summary>
        Gets the character format.
    </summary>
<value>The character format.</value>
        """
        GetDllLibDoc().TextBox_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_get_CharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().TextBox_get_CharacterFormat(self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


