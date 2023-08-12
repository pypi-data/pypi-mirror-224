from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Template (SpireObject) :
    """
    <summary>
        Class represents Attached tempalte of the document.
    </summary>
    """
    @property

    def Path(self)->str:
        """
    <summary>
        Gets or sets the path of the attached template.
     </summary>
<value>The path to attached template document</value>
        """
        GetDllLibDoc().Template_get_Path.argtypes=[c_void_p]
        GetDllLibDoc().Template_get_Path.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Template_get_Path(self.Ptr))
        return ret


    @Path.setter
    def Path(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Template_set_Path.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Template_set_Path(self.Ptr, valuePtr)

