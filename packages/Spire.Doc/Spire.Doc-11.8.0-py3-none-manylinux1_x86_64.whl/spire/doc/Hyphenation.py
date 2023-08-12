from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Hyphenation (SpireObject) :
    """
    <summary>
        Class represents Hyphenation settings of the document.
    </summary>
    """
    @property
    def AutoHyphenation(self)->bool:
        """

        """
        GetDllLibDoc().Hyphenation_get_AutoHyphenation.argtypes=[c_void_p]
        GetDllLibDoc().Hyphenation_get_AutoHyphenation.restype=c_bool
        ret = GetDllLibDoc().Hyphenation_get_AutoHyphenation(self.Ptr)
        return ret

    @AutoHyphenation.setter
    def AutoHyphenation(self, value:bool):
        GetDllLibDoc().Hyphenation_set_AutoHyphenation.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Hyphenation_set_AutoHyphenation(self.Ptr, value)

    @property
    def HyphenateCaps(self)->bool:
        """

        """
        GetDllLibDoc().Hyphenation_get_HyphenateCaps.argtypes=[c_void_p]
        GetDllLibDoc().Hyphenation_get_HyphenateCaps.restype=c_bool
        ret = GetDllLibDoc().Hyphenation_get_HyphenateCaps(self.Ptr)
        return ret

    @HyphenateCaps.setter
    def HyphenateCaps(self, value:bool):
        GetDllLibDoc().Hyphenation_set_HyphenateCaps.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Hyphenation_set_HyphenateCaps(self.Ptr, value)

    @property
    def HyphenationZone(self)->float:
        """

        """
        GetDllLibDoc().Hyphenation_get_HyphenationZone.argtypes=[c_void_p]
        GetDllLibDoc().Hyphenation_get_HyphenationZone.restype=c_float
        ret = GetDllLibDoc().Hyphenation_get_HyphenationZone(self.Ptr)
        return ret

    @HyphenationZone.setter
    def HyphenationZone(self, value:float):
        GetDllLibDoc().Hyphenation_set_HyphenationZone.argtypes=[c_void_p, c_float]
        GetDllLibDoc().Hyphenation_set_HyphenationZone(self.Ptr, value)

    @property
    def ConsecutiveHyphensLimit(self)->int:
        """

        """
        GetDllLibDoc().Hyphenation_get_ConsecutiveHyphensLimit.argtypes=[c_void_p]
        GetDllLibDoc().Hyphenation_get_ConsecutiveHyphensLimit.restype=c_int
        ret = GetDllLibDoc().Hyphenation_get_ConsecutiveHyphensLimit(self.Ptr)
        return ret

    @ConsecutiveHyphensLimit.setter
    def ConsecutiveHyphensLimit(self, value:int):
        GetDllLibDoc().Hyphenation_set_ConsecutiveHyphensLimit.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Hyphenation_set_ConsecutiveHyphensLimit(self.Ptr, value)

