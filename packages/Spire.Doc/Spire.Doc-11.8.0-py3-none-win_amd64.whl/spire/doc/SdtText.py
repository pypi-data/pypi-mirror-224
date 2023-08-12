from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtText (  SdtControlProperties) :
    """

    """
    @dispatch
    def __init__(self, isRichText:bool):
        GetDllLibDoc().SdtText_CreateSdtTextI.argtypes=[c_bool]
        GetDllLibDoc().SdtText_CreateSdtTextI.restype = c_void_p
        intPtr = GetDllLibDoc().SdtText_CreateSdtTextI(isRichText)
        super(SdtText, self).__init__(intPtr)

    @property
    def IsMultiline(self)->bool:
        """
    <summary>
        Allow Soft Line Breaks. Specifies whether soft line breaks can be added to 
            the contents of this structured document tag when this document is modified. 
    </summary>
        """
        GetDllLibDoc().SdtText_get_IsMultiline.argtypes=[c_void_p]
        GetDllLibDoc().SdtText_get_IsMultiline.restype=c_bool
        ret = GetDllLibDoc().SdtText_get_IsMultiline(self.Ptr)
        return ret

    @IsMultiline.setter
    def IsMultiline(self, value:bool):
        GetDllLibDoc().SdtText_set_IsMultiline.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().SdtText_set_IsMultiline(self.Ptr, value)

