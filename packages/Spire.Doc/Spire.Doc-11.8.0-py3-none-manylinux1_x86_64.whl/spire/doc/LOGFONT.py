from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LOGFONT (SpireObject) :
    """

    """

    def ToString(self)->str:
        """

        """
        GetDllLibDoc().LOGFONT_ToString.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_ToString.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().LOGFONT_ToString(self.Ptr))
        return ret


    def lfHeight(self)->int:
        """

        """
        GetDllLibDoc().LOGFONT_lfHeight.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfHeight.restype=c_int
        ret = GetDllLibDoc().LOGFONT_lfHeight(self.Ptr)
        return ret

    def lfWidth(self)->int:
        """

        """
        GetDllLibDoc().LOGFONT_lfWidth.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfWidth.restype=c_int
        ret = GetDllLibDoc().LOGFONT_lfWidth(self.Ptr)
        return ret

    def lfEscapement(self)->int:
        """

        """
        GetDllLibDoc().LOGFONT_lfEscapement.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfEscapement.restype=c_int
        ret = GetDllLibDoc().LOGFONT_lfEscapement(self.Ptr)
        return ret

    def lfOrientation(self)->int:
        """

        """
        GetDllLibDoc().LOGFONT_lfOrientation.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfOrientation.restype=c_int
        ret = GetDllLibDoc().LOGFONT_lfOrientation(self.Ptr)
        return ret


    def lfWeight(self)->'FontWeight':
        """

        """
        GetDllLibDoc().LOGFONT_lfWeight.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfWeight.restype=c_int
        ret = GetDllLibDoc().LOGFONT_lfWeight(self.Ptr)
        objwraped = FontWeight(ret)
        return objwraped

    def lfItalic(self)->bool:
        """

        """
        GetDllLibDoc().LOGFONT_lfItalic.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfItalic.restype=c_bool
        ret = GetDllLibDoc().LOGFONT_lfItalic(self.Ptr)
        return ret

    def lfUnderline(self)->bool:
        """

        """
        GetDllLibDoc().LOGFONT_lfUnderline.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfUnderline.restype=c_bool
        ret = GetDllLibDoc().LOGFONT_lfUnderline(self.Ptr)
        return ret

    def lfStrikeOut(self)->bool:
        """

        """
        GetDllLibDoc().LOGFONT_lfStrikeOut.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfStrikeOut.restype=c_bool
        ret = GetDllLibDoc().LOGFONT_lfStrikeOut(self.Ptr)
        return ret


    def lfCharSet(self)->'FontCharSet':
        """

        """
        GetDllLibDoc().LOGFONT_lfCharSet.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfCharSet.restype=c_int
        ret = GetDllLibDoc().LOGFONT_lfCharSet(self.Ptr)
        objwraped = FontCharSet(ret)
        return objwraped


    def lfOutPrecision(self)->'FontPrecision':
        """

        """
        GetDllLibDoc().LOGFONT_lfOutPrecision.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfOutPrecision.restype=c_int
        ret = GetDllLibDoc().LOGFONT_lfOutPrecision(self.Ptr)
        objwraped = FontPrecision(ret)
        return objwraped


    def lfClipPrecision(self)->'FontClipPrecision':
        """

        """
        GetDllLibDoc().LOGFONT_lfClipPrecision.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfClipPrecision.restype=c_int
        ret = GetDllLibDoc().LOGFONT_lfClipPrecision(self.Ptr)
        objwraped = FontClipPrecision(ret)
        return objwraped


    def lfQuality(self)->'FontQuality':
        """

        """
        GetDllLibDoc().LOGFONT_lfQuality.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfQuality.restype=c_int
        ret = GetDllLibDoc().LOGFONT_lfQuality(self.Ptr)
        objwraped = FontQuality(ret)
        return objwraped


    def lfPitchAndFamily(self)->'FontPitchAndFamily':
        """

        """
        GetDllLibDoc().LOGFONT_lfPitchAndFamily.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfPitchAndFamily.restype=c_int
        ret = GetDllLibDoc().LOGFONT_lfPitchAndFamily(self.Ptr)
        objwraped = FontPitchAndFamily(ret)
        return objwraped


    def lfFaceName(self)->str:
        """

        """
        GetDllLibDoc().LOGFONT_lfFaceName.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfFaceName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().LOGFONT_lfFaceName(self.Ptr))
        return ret


