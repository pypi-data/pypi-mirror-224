from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LicenseProvider (SpireObject) :
    """

    """
    @staticmethod

    def Register(userName:str,code:str):
        """

        """
        userNamePtr = StrToPtr(userName)
        codePtr = StrToPtr(code)
        GetDllLibDoc().LicenseProvider_Register.argtypes=[c_char_p,c_char_p]
        GetDllLibDoc().LicenseProvider_Register(userNamePtr,codePtr)

