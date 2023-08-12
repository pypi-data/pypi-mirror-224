from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PasswordErrorException (SpireObject) :
    """
    <summary>
        Class password error exception.
    </summary>
    """
    @property

    def Message(self)->str:
        """
    <summary>
        Gets the message that describes the current exception.
    </summary>
        """
        GetDllLibDoc().PasswordErrorException_get_Message.argtypes=[c_void_p]
        GetDllLibDoc().PasswordErrorException_get_Message.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().PasswordErrorException_get_Message(self.Ptr))
        return ret


