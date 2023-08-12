from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextRange (  ParagraphBase, ITextRange) :
    """

    """
    @dispatch
    def __init__(self, doc:'IDocument'):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().TextRange_CreateTextRangeD.argtypes=[c_void_p]
        GetDllLibDoc().TextRange_CreateTextRangeD.restype=c_void_p
        intPtr = GetDllLibDoc().TextRange_CreateTextRangeD(intPdoc)
        super(TextRange, self).__init__(intPtr)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().TextRange_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TextRange_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().TextRange_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Text(self)->str:
        """
    <summary>
        Returns or sets text.
    </summary>
        """
        GetDllLibDoc().TextRange_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().TextRange_get_Text.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().TextRange_get_Text(self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextRange_set_Text.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().TextRange_set_Text(self.Ptr, valuePtr)

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
    <summary>
        Gets the character format.
    </summary>
        """
        GetDllLibDoc().TextRange_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().TextRange_get_CharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().TextRange_get_CharacterFormat(self.Ptr)
        from spire.doc import CharacterFormat
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


