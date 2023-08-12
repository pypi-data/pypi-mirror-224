from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FormField (  Field) :
    """

    """
    @property

    def FormFieldType(self)->'FormFieldType':
        """
    <summary>
        Gets type of this form field.
    </summary>
        """
        GetDllLibDoc().FormField_get_FormFieldType.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_FormFieldType.restype=c_int
        ret = GetDllLibDoc().FormField_get_FormFieldType(self.Ptr)
        objwraped = FormFieldType(ret)
        return objwraped

    @property

    def Name(self)->str:
        """
    <summary>
        Gets or sets form field title name (bookmark name).
            The name is unique in the document.
    </summary>
        """
        GetDllLibDoc().FormField_get_Name.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_Name.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().FormField_get_Name(self.Ptr))
        return ret


    @Name.setter
    def Name(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().FormField_set_Name.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().FormField_set_Name(self.Ptr, valuePtr)

    @property

    def Help(self)->str:
        """
    <summary>
        Gets or sets form field help.
    </summary>
        """
        GetDllLibDoc().FormField_get_Help.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_Help.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().FormField_get_Help(self.Ptr))
        return ret


    @Help.setter
    def Help(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().FormField_set_Help.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().FormField_set_Help(self.Ptr, valuePtr)

    @property

    def StatusBarHelp(self)->str:
        """
    <summary>
        Gets or sets the status bar help.
    </summary>
<value>The status bar help.</value>
        """
        GetDllLibDoc().FormField_get_StatusBarHelp.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_StatusBarHelp.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().FormField_get_StatusBarHelp(self.Ptr))
        return ret


    @StatusBarHelp.setter
    def StatusBarHelp(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().FormField_set_StatusBarHelp.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().FormField_set_StatusBarHelp(self.Ptr, valuePtr)

    @property

    def MacroOnStart(self)->str:
        """
    <summary>
        Returns or setsthe name of macros on start
    </summary>
        """
        GetDllLibDoc().FormField_get_MacroOnStart.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_MacroOnStart.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().FormField_get_MacroOnStart(self.Ptr))
        return ret


    @MacroOnStart.setter
    def MacroOnStart(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().FormField_set_MacroOnStart.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().FormField_set_MacroOnStart(self.Ptr, valuePtr)

    @property

    def MacroOnEnd(self)->str:
        """
    <summary>
        Returns or setsthe name of macros on end
    </summary>
        """
        GetDllLibDoc().FormField_get_MacroOnEnd.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_MacroOnEnd.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().FormField_get_MacroOnEnd(self.Ptr))
        return ret


    @MacroOnEnd.setter
    def MacroOnEnd(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().FormField_set_MacroOnEnd.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().FormField_set_MacroOnEnd(self.Ptr, valuePtr)

    @property
    def Enabled(self)->bool:
        """
    <summary>
        Get/sets Enabled property (true if form field enabled).
    </summary>
        """
        GetDllLibDoc().FormField_get_Enabled.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_Enabled.restype=c_bool
        ret = GetDllLibDoc().FormField_get_Enabled(self.Ptr)
        return ret

    @Enabled.setter
    def Enabled(self, value:bool):
        GetDllLibDoc().FormField_set_Enabled.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().FormField_set_Enabled(self.Ptr, value)

    @property
    def CalculateOnExit(self)->bool:
        """
    <summary>
        Gets or sets calculate on exit property.
    </summary>
        """
        GetDllLibDoc().FormField_get_CalculateOnExit.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_CalculateOnExit.restype=c_bool
        ret = GetDllLibDoc().FormField_get_CalculateOnExit(self.Ptr)
        return ret

    @CalculateOnExit.setter
    def CalculateOnExit(self, value:bool):
        GetDllLibDoc().FormField_set_CalculateOnExit.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().FormField_set_CalculateOnExit(self.Ptr, value)

