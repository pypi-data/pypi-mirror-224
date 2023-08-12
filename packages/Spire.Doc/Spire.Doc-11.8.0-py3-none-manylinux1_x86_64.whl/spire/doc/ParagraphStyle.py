from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ParagraphStyle (  Style, IParagraphStyle) :
    """

    """
    @dispatch
    def __init__(self, doc:IDocument):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().ParagraphStyle_CreateParagraphStyleD.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphStyle_CreateParagraphStyleD.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphStyle_CreateParagraphStyleD(intPdoc)
        super(ParagraphStyle, self).__init__(intPtr)

    @property

    def ParagraphFormat(self)->'ParagraphFormat':
        """

        """
        GetDllLibDoc().ParagraphStyle_get_ParagraphFormat.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphStyle_get_ParagraphFormat.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphStyle_get_ParagraphFormat(self.Ptr)
        ret = None if intPtr==None else ParagraphFormat(intPtr)
        return ret


    @property

    def BaseStyle(self)->'ParagraphStyle':
        """

        """
        GetDllLibDoc().ParagraphStyle_get_BaseStyle.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphStyle_get_BaseStyle.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphStyle_get_BaseStyle(self.Ptr)
        ret = None if intPtr==None else ParagraphStyle(intPtr)
        return ret


    @property

    def StyleType(self)->'StyleType':
        """

        """
        GetDllLibDoc().ParagraphStyle_get_StyleType.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphStyle_get_StyleType.restype=c_int
        ret = GetDllLibDoc().ParagraphStyle_get_StyleType(self.Ptr)
        objwraped = StyleType(ret)
        return objwraped

    @property

    def ListFormat(self)->'ListFormat':
        """

        """
        GetDllLibDoc().ParagraphStyle_get_ListFormat.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphStyle_get_ListFormat.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphStyle_get_ListFormat(self.Ptr)
        ret = None if intPtr==None else ListFormat(intPtr)
        return ret



    def ApplyBaseStyle(self ,styleName:str):
        """

        """
        styleNamePtr = StrToPtr(styleName)
        GetDllLibDoc().ParagraphStyle_ApplyBaseStyle.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().ParagraphStyle_ApplyBaseStyle(self.Ptr, styleNamePtr)


    def Clone(self)->'IStyle':
        """

        """
        GetDllLibDoc().ParagraphStyle_Clone.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphStyle_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphStyle_Clone(self.Ptr)
        ret = None if intPtr==None else IStyle(intPtr)
        return ret


