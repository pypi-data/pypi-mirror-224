from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtCheckBox (  SdtControlProperties) :
    """

    """
    @dispatch
    def __init__(self):
        GetDllLibDoc().SdtCheckBox_CreateSdtCheckBox.restype=c_void_p
        intPtr = GetDllLibDoc().SdtCheckBox_CreateSdtCheckBox()
        super(SdtCheckBox, self).__init__(intPtr)

    @property
    def Checked(self)->bool:
        """
    <summary>
        Indicates if checkbox is in checked state.
    </summary>
        """
        GetDllLibDoc().SdtCheckBox_get_Checked.argtypes=[c_void_p]
        GetDllLibDoc().SdtCheckBox_get_Checked.restype=c_bool
        ret = GetDllLibDoc().SdtCheckBox_get_Checked(self.Ptr)
        return ret

    @Checked.setter
    def Checked(self, value:bool):
        GetDllLibDoc().SdtCheckBox_set_Checked.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().SdtCheckBox_set_Checked(self.Ptr, value)

    @property

    def CheckedStateFontName(self)->str:
        """
    <summary>
        Font name used for checked state.
    </summary>
        """
        GetDllLibDoc().SdtCheckBox_get_CheckedStateFontName.argtypes=[c_void_p]
        GetDllLibDoc().SdtCheckBox_get_CheckedStateFontName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SdtCheckBox_get_CheckedStateFontName(self.Ptr))
        return ret


    @CheckedStateFontName.setter
    def CheckedStateFontName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtCheckBox_set_CheckedStateFontName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SdtCheckBox_set_CheckedStateFontName(self.Ptr, valuePtr)

    @property
    def CheckedStateCharacterCode(self)->int:
        """
    <summary>
        Character code used for checked state.
    </summary>
        """
        GetDllLibDoc().SdtCheckBox_get_CheckedStateCharacterCode.argtypes=[c_void_p]
        GetDllLibDoc().SdtCheckBox_get_CheckedStateCharacterCode.restype=c_int
        ret = GetDllLibDoc().SdtCheckBox_get_CheckedStateCharacterCode(self.Ptr)
        return ret

    @CheckedStateCharacterCode.setter
    def CheckedStateCharacterCode(self, value:int):
        GetDllLibDoc().SdtCheckBox_set_CheckedStateCharacterCode.argtypes=[c_void_p, c_int]
        GetDllLibDoc().SdtCheckBox_set_CheckedStateCharacterCode(self.Ptr, value)

    @property

    def UnCheckedStateFontName(self)->str:
        """
    <summary>
        Font name used for unchecked state.
    </summary>
        """
        GetDllLibDoc().SdtCheckBox_get_UnCheckedStateFontName.argtypes=[c_void_p]
        GetDllLibDoc().SdtCheckBox_get_UnCheckedStateFontName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SdtCheckBox_get_UnCheckedStateFontName(self.Ptr))
        return ret


    @UnCheckedStateFontName.setter
    def UnCheckedStateFontName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtCheckBox_set_UnCheckedStateFontName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SdtCheckBox_set_UnCheckedStateFontName(self.Ptr, valuePtr)

    @property
    def UnCheckedStateCharacterCode(self)->int:
        """
    <summary>
        Character code used for unchecked state.
    </summary>
        """
        GetDllLibDoc().SdtCheckBox_get_UnCheckedStateCharacterCode.argtypes=[c_void_p]
        GetDllLibDoc().SdtCheckBox_get_UnCheckedStateCharacterCode.restype=c_int
        ret = GetDllLibDoc().SdtCheckBox_get_UnCheckedStateCharacterCode(self.Ptr)
        return ret

    @UnCheckedStateCharacterCode.setter
    def UnCheckedStateCharacterCode(self, value:int):
        GetDllLibDoc().SdtCheckBox_set_UnCheckedStateCharacterCode.argtypes=[c_void_p, c_int]
        GetDllLibDoc().SdtCheckBox_set_UnCheckedStateCharacterCode(self.Ptr, value)

    @staticmethod
    def DefaultCheckedState()->int:
        """

        """
        #GetDllLibDoc().SdtCheckBox_DefaultCheckedState.argtypes=[]
        GetDllLibDoc().SdtCheckBox_DefaultCheckedState.restype=c_int
        ret = GetDllLibDoc().SdtCheckBox_DefaultCheckedState()
        return ret

    @staticmethod
    def DefaultUncheckedState()->int:
        """

        """
        #GetDllLibDoc().SdtCheckBox_DefaultUncheckedState.argtypes=[]
        GetDllLibDoc().SdtCheckBox_DefaultUncheckedState.restype=c_int
        ret = GetDllLibDoc().SdtCheckBox_DefaultUncheckedState()
        return ret

    @staticmethod

    def DefaultFontName()->str:
        """

        """
        #GetDllLibDoc().SdtCheckBox_DefaultFontName.argtypes=[]
        GetDllLibDoc().SdtCheckBox_DefaultFontName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SdtCheckBox_DefaultFontName())
        return ret


