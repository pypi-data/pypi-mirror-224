from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FormatBase (  DocumentSerializable) :
    """

    """
    @property
    def IsDefault(self)->bool:
        """
    <summary>
        Gets a value indicating whether format is default.
    </summary>
<value>
  <c>true</c> if format is default; otherwise,<c>false</c>.</value>
        """
        GetDllLibDoc().FormatBase_get_IsDefault.argtypes=[c_void_p]
        GetDllLibDoc().FormatBase_get_IsDefault.restype=c_bool
        ret = GetDllLibDoc().FormatBase_get_IsDefault(self.Ptr)
        return ret


    def HasKey(self ,key:int)->bool:
        """
    <summary>
        Checks if Key exists.
    </summary>
    <param name="key">The key.</param>
    <returns>
            if the specified key has key, set to <c>true</c>.
            </returns>
        """
        
        GetDllLibDoc().FormatBase_HasKey.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().FormatBase_HasKey.restype=c_bool
        ret = GetDllLibDoc().FormatBase_HasKey(self.Ptr, key)
        return ret

    def ClearFormatting(self):
        """
    <summary>
        Clears the formatting.
    </summary>
        """
        GetDllLibDoc().FormatBase_ClearFormatting.argtypes=[c_void_p]
        GetDllLibDoc().FormatBase_ClearFormatting(self.Ptr)

    def ClearBackground(self):
        """

        """
        GetDllLibDoc().FormatBase_ClearBackground.argtypes=[c_void_p]
        GetDllLibDoc().FormatBase_ClearBackground(self.Ptr)

