from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DropDownItem (  DocumentSerializable) :
    """

    """
    @property

    def Text(self)->str:
        """
    <summary>
        Gets or sets  text
    </summary>
        """
        GetDllLibDoc().DropDownItem_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().DropDownItem_get_Text.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().DropDownItem_get_Text(self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().DropDownItem_set_Text.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().DropDownItem_set_Text(self.Ptr, valuePtr)

