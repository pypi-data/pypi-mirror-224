from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FootnoteBody (SpireObject) :
    """

    """
    @property

    def Separator(self)->'Body':
        """

        """
        GetDllLibDoc().FootnoteBody_get_Separator.argtypes=[c_void_p]
        GetDllLibDoc().FootnoteBody_get_Separator.restype=c_void_p
        intPtr = GetDllLibDoc().FootnoteBody_get_Separator(self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @Separator.setter
    def Separator(self, value:'Body'):
        GetDllLibDoc().FootnoteBody_set_Separator.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().FootnoteBody_set_Separator(self.Ptr, value.Ptr)

    @property

    def ContinuationSeparator(self)->'Body':
        """

        """
        GetDllLibDoc().FootnoteBody_get_ContinuationSeparator.argtypes=[c_void_p]
        GetDllLibDoc().FootnoteBody_get_ContinuationSeparator.restype=c_void_p
        intPtr = GetDllLibDoc().FootnoteBody_get_ContinuationSeparator(self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @ContinuationSeparator.setter
    def ContinuationSeparator(self, value:'Body'):
        GetDllLibDoc().FootnoteBody_set_ContinuationSeparator.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().FootnoteBody_set_ContinuationSeparator(self.Ptr, value.Ptr)

    @property

    def ContinuationNotice(self)->'Body':
        """

        """
        GetDllLibDoc().FootnoteBody_get_ContinuationNotice.argtypes=[c_void_p]
        GetDllLibDoc().FootnoteBody_get_ContinuationNotice.restype=c_void_p
        intPtr = GetDllLibDoc().FootnoteBody_get_ContinuationNotice(self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @ContinuationNotice.setter
    def ContinuationNotice(self, value:'Body'):
        GetDllLibDoc().FootnoteBody_set_ContinuationNotice.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().FootnoteBody_set_ContinuationNotice(self.Ptr, value.Ptr)


    def Clone(self)->'FootnoteBody':
        """

        """
        GetDllLibDoc().FootnoteBody_Clone.argtypes=[c_void_p]
        GetDllLibDoc().FootnoteBody_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().FootnoteBody_Clone(self.Ptr)
        ret = None if intPtr==None else FootnoteBody(intPtr)
        return ret


