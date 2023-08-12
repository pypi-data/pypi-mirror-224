from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextWatermark (  WatermarkBase) :
    """

    """
    @dispatch
    def __init__(self):
        GetDllLibDoc().TextWatermark_CreateTextWatermark.restype=c_void_p
        intPtr = GetDllLibDoc().TextWatermark_CreateTextWatermark();
        super(TextWatermark, self).__init__(intPtr)

    @dispatch
    def __init__(self, text:str):
        textPtr = StrToPtr(text)
        GetDllLibDoc().TextWatermark_CreateTextWatermarkT.argtypes=[c_char_p]
        GetDllLibDoc().TextWatermark_CreateTextWatermarkT.restype=c_void_p
        intPtr = GetDllLibDoc().TextWatermark_CreateTextWatermarkT(textPtr)
        super(TextWatermark, self).__init__(intPtr)
    
    @dispatch
    def __init__(self, text:str, fontName:str, fontSize:int, layout:WatermarkLayout):
        textPtr = StrToPtr(text)
        fontNamePtr = StrToPtr(fontName)
        iTypelayout:c_int = layout.value

        GetDllLibDoc().TextWatermark_CreateTextWatermarkTFFL.argtypes=[c_char_p,c_char_p,c_int,c_int]
        GetDllLibDoc().TextWatermark_CreateTextWatermarkTFFL.restype=c_void_p
        intPtr = GetDllLibDoc().TextWatermark_CreateTextWatermarkTFFL(textPtr, fontNamePtr, fontSize, iTypelayout)
        super(TextWatermark, self).__init__(intPtr)

    @property

    def Text(self)->str:
        """
    <summary>
        Gets or sets watermark text
    </summary>
        """
        GetDllLibDoc().TextWatermark_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_Text.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().TextWatermark_get_Text(self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextWatermark_set_Text.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().TextWatermark_set_Text(self.Ptr, valuePtr)

    @property

    def FontName(self)->str:
        """
    <summary>
        Gets or sets watermark text's font name. 
    </summary>
        """
        GetDllLibDoc().TextWatermark_get_FontName.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_FontName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().TextWatermark_get_FontName(self.Ptr))
        return ret


    @FontName.setter
    def FontName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextWatermark_set_FontName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().TextWatermark_set_FontName(self.Ptr, valuePtr)

    @property
    def FontSize(self)->float:
        """
    <summary>
        Gets or sets text watermark size.
    </summary>
        """
        GetDllLibDoc().TextWatermark_get_FontSize.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_FontSize.restype=c_float
        ret = GetDllLibDoc().TextWatermark_get_FontSize(self.Ptr)
        return ret

    @FontSize.setter
    def FontSize(self, value:float):
        GetDllLibDoc().TextWatermark_set_FontSize.argtypes=[c_void_p, c_float]
        GetDllLibDoc().TextWatermark_set_FontSize(self.Ptr, value)

    @property

    def Color(self)->'Color':
        """
    <summary>
        Gets or sets text watermark color.
    </summary>
        """
        GetDllLibDoc().TextWatermark_get_Color.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_Color.restype=c_void_p
        intPtr = GetDllLibDoc().TextWatermark_get_Color(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @Color.setter
    def Color(self, value:'Color'):
        GetDllLibDoc().TextWatermark_set_Color.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().TextWatermark_set_Color(self.Ptr, value.Ptr)

    @property
    def Semitransparent(self)->bool:
        """
    <summary>
        Gets or sets semitransparent property for Text watermark.
    </summary>
        """
        GetDllLibDoc().TextWatermark_get_Semitransparent.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_Semitransparent.restype=c_bool
        ret = GetDllLibDoc().TextWatermark_get_Semitransparent(self.Ptr)
        return ret

    @Semitransparent.setter
    def Semitransparent(self, value:bool):
        GetDllLibDoc().TextWatermark_set_Semitransparent.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().TextWatermark_set_Semitransparent(self.Ptr, value)

    @property

    def Layout(self)->'WatermarkLayout':
        """
    <summary>
        Gets or sets layout for Text watermark.
    </summary>
        """
        GetDllLibDoc().TextWatermark_get_Layout.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_Layout.restype=c_int
        ret = GetDllLibDoc().TextWatermark_get_Layout(self.Ptr)
        objwraped = WatermarkLayout(ret)
        return objwraped

    @Layout.setter
    def Layout(self, value:'WatermarkLayout'):
        GetDllLibDoc().TextWatermark_set_Layout.argtypes=[c_void_p, c_int]
        GetDllLibDoc().TextWatermark_set_Layout(self.Ptr, value.value)

