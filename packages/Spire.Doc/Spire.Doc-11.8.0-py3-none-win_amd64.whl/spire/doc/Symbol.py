from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Symbol (  ParagraphBase, IDocumentObject) :
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
        GetDllLibDoc().Symbol_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Symbol_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().Symbol_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
    <summary>
        Gets character format for the symbol.
    </summary>
        """
        GetDllLibDoc().Symbol_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().Symbol_get_CharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().Symbol_get_CharacterFormat(self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def FontName(self)->str:
        """
    <summary>
        Returns or setssymbol font name.
    </summary>
        """
        GetDllLibDoc().Symbol_get_FontName.argtypes=[c_void_p]
        GetDllLibDoc().Symbol_get_FontName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Symbol_get_FontName(self.Ptr))
        return ret


    @FontName.setter
    def FontName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Symbol_set_FontName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Symbol_set_FontName(self.Ptr, valuePtr)

    @property
    def CharacterCode(self)->int:
        """
    <summary>
        Returns or sets symbol's character code.
    </summary>
        """
        GetDllLibDoc().Symbol_get_CharacterCode.argtypes=[c_void_p]
        GetDllLibDoc().Symbol_get_CharacterCode.restype=c_int
        ret = GetDllLibDoc().Symbol_get_CharacterCode(self.Ptr)
        return ret

    @CharacterCode.setter
    def CharacterCode(self, value:int):
        GetDllLibDoc().Symbol_set_CharacterCode.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Symbol_set_CharacterCode(self.Ptr, value)

