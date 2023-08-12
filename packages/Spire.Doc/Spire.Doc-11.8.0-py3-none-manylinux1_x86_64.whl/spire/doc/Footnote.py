from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Footnote (  ParagraphBase, ICompositeObject) :
    """

    """
    @property
    def UseAbsolutePos(self)->bool:
        """

        """
        GetDllLibDoc().Footnote_get_UseAbsolutePos.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_UseAbsolutePos.restype=c_bool
        ret = GetDllLibDoc().Footnote_get_UseAbsolutePos(self.Ptr)
        return ret

    @UseAbsolutePos.setter
    def UseAbsolutePos(self, value:bool):
        GetDllLibDoc().Footnote_set_UseAbsolutePos.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Footnote_set_UseAbsolutePos(self.Ptr, value)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().Footnote_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().Footnote_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def FootnoteType(self)->'FootnoteType':
        """
    <summary>
        Gets or sets footnote type: footnote or endnote
    </summary>
        """
        GetDllLibDoc().Footnote_get_FootnoteType.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_FootnoteType.restype=c_int
        ret = GetDllLibDoc().Footnote_get_FootnoteType(self.Ptr)
        objwraped = FootnoteType(ret)
        return objwraped

    @FootnoteType.setter
    def FootnoteType(self, value:'FootnoteType'):
        GetDllLibDoc().Footnote_set_FootnoteType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Footnote_set_FootnoteType(self.Ptr, value.value)

    @property
    def IsAutoNumbered(self)->bool:
        """
    <summary>
        Gets or sets the value indicating if the footnote is auto numbered
    </summary>
        """
        GetDllLibDoc().Footnote_get_IsAutoNumbered.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_IsAutoNumbered.restype=c_bool
        ret = GetDllLibDoc().Footnote_get_IsAutoNumbered(self.Ptr)
        return ret

    @IsAutoNumbered.setter
    def IsAutoNumbered(self, value:bool):
        GetDllLibDoc().Footnote_set_IsAutoNumbered.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Footnote_set_IsAutoNumbered(self.Ptr, value)

    @property

    def TextBody(self)->'Body':
        """
    <summary>
        Gets the text body of the footnote.
    </summary>
<value>The text body.</value>
        """
        GetDllLibDoc().Footnote_get_TextBody.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_TextBody.restype=c_void_p
        intPtr = GetDllLibDoc().Footnote_get_TextBody(self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @property

    def MarkerCharacterFormat(self)->'CharacterFormat':
        """
    <summary>
        Gets the marker character format
    </summary>
        """
        GetDllLibDoc().Footnote_get_MarkerCharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_MarkerCharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().Footnote_get_MarkerCharacterFormat(self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property
    def SymbolCode(self)->int:
        """
    <summary>
        Gets or sets the marker symbol code.
    </summary>
<value>The symbol code.</value>
        """
        GetDllLibDoc().Footnote_get_SymbolCode.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_SymbolCode.restype=c_int
        ret = GetDllLibDoc().Footnote_get_SymbolCode(self.Ptr)
        return ret

    @SymbolCode.setter
    def SymbolCode(self, value:int):
        GetDllLibDoc().Footnote_set_SymbolCode.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Footnote_set_SymbolCode(self.Ptr, value)

    @property

    def CustomMarker(self)->str:
        """
    <summary>
        Gets or sets the custom footnote marker.
    </summary>
<value>The custom marker.</value>
        """
        GetDllLibDoc().Footnote_get_CustomMarker.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_CustomMarker.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Footnote_get_CustomMarker(self.Ptr))
        return ret


    @CustomMarker.setter
    def CustomMarker(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Footnote_set_CustomMarker.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Footnote_set_CustomMarker(self.Ptr, valuePtr)

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """

        """
        GetDllLibDoc().Footnote_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().Footnote_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    def EnsureMinimum(self):
        """

        """
        GetDllLibDoc().Footnote_EnsureMinimum.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_EnsureMinimum(self.Ptr)

