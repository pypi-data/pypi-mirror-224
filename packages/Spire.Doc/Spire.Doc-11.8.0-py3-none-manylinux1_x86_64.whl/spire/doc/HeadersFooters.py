from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HeadersFooters (  DocumentSerializable, IEnumerable) :
    """

    """
    @property

    def Header(self)->'HeaderFooter':
        """
    <summary>
        Gets default header.
    </summary>
        """
        GetDllLibDoc().HeadersFooters_get_Header.argtypes=[c_void_p]
        GetDllLibDoc().HeadersFooters_get_Header.restype=c_void_p
        intPtr = GetDllLibDoc().HeadersFooters_get_Header(self.Ptr)
        ret = None if intPtr==None else HeaderFooter(intPtr)
        return ret


    @property

    def Footer(self)->'HeaderFooter':
        """
    <summary>
        Gets default footer.
    </summary>
        """
        GetDllLibDoc().HeadersFooters_get_Footer.argtypes=[c_void_p]
        GetDllLibDoc().HeadersFooters_get_Footer.restype=c_void_p
        intPtr = GetDllLibDoc().HeadersFooters_get_Footer(self.Ptr)
        ret = None if intPtr==None else HeaderFooter(intPtr)
        return ret


    @property

    def EvenHeader(self)->'HeaderFooter':
        """
    <summary>
        Gets even header.
    </summary>
        """
        GetDllLibDoc().HeadersFooters_get_EvenHeader.argtypes=[c_void_p]
        GetDllLibDoc().HeadersFooters_get_EvenHeader.restype=c_void_p
        intPtr = GetDllLibDoc().HeadersFooters_get_EvenHeader(self.Ptr)
        ret = None if intPtr==None else HeaderFooter(intPtr)
        return ret


    @property

    def OddHeader(self)->'HeaderFooter':
        """
    <summary>
        Gets odd header ( This is also the default header ).
    </summary>
        """
        GetDllLibDoc().HeadersFooters_get_OddHeader.argtypes=[c_void_p]
        GetDllLibDoc().HeadersFooters_get_OddHeader.restype=c_void_p
        intPtr = GetDllLibDoc().HeadersFooters_get_OddHeader(self.Ptr)
        ret = None if intPtr==None else HeaderFooter(intPtr)
        return ret


    @property

    def EvenFooter(self)->'HeaderFooter':
        """
    <summary>
        Gets even footer
    </summary>
        """
        GetDllLibDoc().HeadersFooters_get_EvenFooter.argtypes=[c_void_p]
        GetDllLibDoc().HeadersFooters_get_EvenFooter.restype=c_void_p
        intPtr = GetDllLibDoc().HeadersFooters_get_EvenFooter(self.Ptr)
        ret = None if intPtr==None else HeaderFooter(intPtr)
        return ret


    @property

    def OddFooter(self)->'HeaderFooter':
        """
    <summary>
        Gets odd footer ( This is also the default footer ).
    </summary>
        """
        GetDllLibDoc().HeadersFooters_get_OddFooter.argtypes=[c_void_p]
        GetDllLibDoc().HeadersFooters_get_OddFooter.restype=c_void_p
        intPtr = GetDllLibDoc().HeadersFooters_get_OddFooter(self.Ptr)
        ret = None if intPtr==None else HeaderFooter(intPtr)
        return ret


    @property

    def FirstPageHeader(self)->'HeaderFooter':
        """
    <summary>
        Gets first page header.
    </summary>
        """
        GetDllLibDoc().HeadersFooters_get_FirstPageHeader.argtypes=[c_void_p]
        GetDllLibDoc().HeadersFooters_get_FirstPageHeader.restype=c_void_p
        intPtr = GetDllLibDoc().HeadersFooters_get_FirstPageHeader(self.Ptr)
        ret = None if intPtr==None else HeaderFooter(intPtr)
        return ret


    @property

    def FirstPageFooter(self)->'HeaderFooter':
        """
    <summary>
        Gets first page footer.
    </summary>
        """
        GetDllLibDoc().HeadersFooters_get_FirstPageFooter.argtypes=[c_void_p]
        GetDllLibDoc().HeadersFooters_get_FirstPageFooter.restype=c_void_p
        intPtr = GetDllLibDoc().HeadersFooters_get_FirstPageFooter(self.Ptr)
        ret = None if intPtr==None else HeaderFooter(intPtr)
        return ret


    @property
    def IsEmpty(self)->bool:
        """
    <summary>
        Detects whether all headers/footers are empty.
    </summary>
        """
        GetDllLibDoc().HeadersFooters_get_IsEmpty.argtypes=[c_void_p]
        GetDllLibDoc().HeadersFooters_get_IsEmpty.restype=c_bool
        ret = GetDllLibDoc().HeadersFooters_get_IsEmpty(self.Ptr)
        return ret

    @dispatch

    def get_Item(self ,index:int)->HeaderFooter:
        """
    <summary>
        Gets TextBody at specified index.
    </summary>
        """
        
        GetDllLibDoc().HeadersFooters_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().HeadersFooters_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().HeadersFooters_get_Item(self.Ptr, index)
        ret = None if intPtr==None else HeaderFooter(intPtr)
        return ret


    @dispatch

    def get_Item(self ,hfType:HeaderFooterType)->HeaderFooter:
        """
    <summary>
        Gets TextBody by specified HeaderFooter type.
    </summary>
        """
        enumhfType:c_int = hfType.value

        GetDllLibDoc().HeadersFooters_get_ItemH.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().HeadersFooters_get_ItemH.restype=c_void_p
        intPtr = GetDllLibDoc().HeadersFooters_get_ItemH(self.Ptr, enumhfType)
        ret = None if intPtr==None else HeaderFooter(intPtr)
        return ret


    @property
    def LinkToPrevious(self)->bool:
        """
    <summary>
        If set to True if this header or footer is linked in the previous section.
    </summary>
        """
        GetDllLibDoc().HeadersFooters_get_LinkToPrevious.argtypes=[c_void_p]
        GetDllLibDoc().HeadersFooters_get_LinkToPrevious.restype=c_bool
        ret = GetDllLibDoc().HeadersFooters_get_LinkToPrevious(self.Ptr)
        return ret

    @LinkToPrevious.setter
    def LinkToPrevious(self, value:bool):
        GetDllLibDoc().HeadersFooters_set_LinkToPrevious.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().HeadersFooters_set_LinkToPrevious(self.Ptr, value)


    def GetEnumerator(self)->'IEnumerator':
        """

        """
        GetDllLibDoc().HeadersFooters_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().HeadersFooters_GetEnumerator.restype=c_void_p
        intPtr = GetDllLibDoc().HeadersFooters_GetEnumerator(self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret


