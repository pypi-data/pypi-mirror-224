from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SequenceField (  Field, IDocumentObject) :
    """

    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().SequenceField_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().SequenceField_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().SequenceField_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def FormattingString(self)->str:
        """
    <summary>
        Gets the formatting string
    </summary>
        """
        GetDllLibDoc().SequenceField_get_FormattingString.argtypes=[c_void_p]
        GetDllLibDoc().SequenceField_get_FormattingString.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SequenceField_get_FormattingString(self.Ptr))
        return ret


    @property

    def NumberFormat(self)->'CaptionNumberingFormat':
        """
    <summary>
        Returns or setsthe type of caption numbering
    </summary>
        """
        GetDllLibDoc().SequenceField_get_NumberFormat.argtypes=[c_void_p]
        GetDllLibDoc().SequenceField_get_NumberFormat.restype=c_int
        ret = GetDllLibDoc().SequenceField_get_NumberFormat(self.Ptr)
        objwraped = CaptionNumberingFormat(ret)
        return objwraped

    @NumberFormat.setter
    def NumberFormat(self, value:'CaptionNumberingFormat'):
        GetDllLibDoc().SequenceField_set_NumberFormat.argtypes=[c_void_p, c_int]
        GetDllLibDoc().SequenceField_set_NumberFormat(self.Ptr, value.value)

    @property

    def CaptionName(self)->str:
        """
    <summary>
        Returns or sets caption name
    </summary>
        """
        GetDllLibDoc().SequenceField_get_CaptionName.argtypes=[c_void_p]
        GetDllLibDoc().SequenceField_get_CaptionName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SequenceField_get_CaptionName(self.Ptr))
        return ret


    @CaptionName.setter
    def CaptionName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SequenceField_set_CaptionName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SequenceField_set_CaptionName(self.Ptr, valuePtr)

