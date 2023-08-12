from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class WordArt (SpireObject) :
    """

    """
    @property

    def FontFamily(self)->str:
        """

        """
        GetDllLibDoc().WordArt_get_FontFamily.argtypes=[c_void_p]
        GetDllLibDoc().WordArt_get_FontFamily.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().WordArt_get_FontFamily(self.Ptr))
        return ret


    @FontFamily.setter
    def FontFamily(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().WordArt_set_FontFamily.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().WordArt_set_FontFamily(self.Ptr, valuePtr)

    @property
    def Size(self)->float:
        """

        """
        GetDllLibDoc().WordArt_get_Size.argtypes=[c_void_p]
        GetDllLibDoc().WordArt_get_Size.restype=c_double
        ret = GetDllLibDoc().WordArt_get_Size(self.Ptr)
        return ret

    @Size.setter
    def Size(self, value:float):
        GetDllLibDoc().WordArt_set_Size.argtypes=[c_void_p, c_double]
        GetDllLibDoc().WordArt_set_Size(self.Ptr, value)

    @property
    def Bold(self)->bool:
        """

        """
        GetDllLibDoc().WordArt_get_Bold.argtypes=[c_void_p]
        GetDllLibDoc().WordArt_get_Bold.restype=c_bool
        ret = GetDllLibDoc().WordArt_get_Bold(self.Ptr)
        return ret

    @Bold.setter
    def Bold(self, value:bool):
        GetDllLibDoc().WordArt_set_Bold.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().WordArt_set_Bold(self.Ptr, value)

    @property
    def Italic(self)->bool:
        """

        """
        GetDllLibDoc().WordArt_get_Italic.argtypes=[c_void_p]
        GetDllLibDoc().WordArt_get_Italic.restype=c_bool
        ret = GetDllLibDoc().WordArt_get_Italic(self.Ptr)
        return ret

    @Italic.setter
    def Italic(self, value:bool):
        GetDllLibDoc().WordArt_set_Italic.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().WordArt_set_Italic(self.Ptr, value)

    @property
    def SmallCaps(self)->bool:
        """

        """
        GetDllLibDoc().WordArt_get_SmallCaps.argtypes=[c_void_p]
        GetDllLibDoc().WordArt_get_SmallCaps.restype=c_bool
        ret = GetDllLibDoc().WordArt_get_SmallCaps(self.Ptr)
        return ret

    @SmallCaps.setter
    def SmallCaps(self, value:bool):
        GetDllLibDoc().WordArt_set_SmallCaps.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().WordArt_set_SmallCaps(self.Ptr, value)

    @property

    def Text(self)->str:
        """

        """
        GetDllLibDoc().WordArt_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().WordArt_get_Text.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().WordArt_get_Text(self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().WordArt_set_Text.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().WordArt_set_Text(self.Ptr, valuePtr)

