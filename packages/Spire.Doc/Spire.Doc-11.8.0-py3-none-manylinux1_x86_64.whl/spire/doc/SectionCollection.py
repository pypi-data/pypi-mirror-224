from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SectionCollection (  DocumentObjectCollection, IWSectionCollection) :
    """

    """

    def get_Item(self ,index:int)->'Section':
        """

        """
        
        GetDllLibDoc().SectionCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().SectionCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().SectionCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else Section(intPtr)
        return ret



    def Add(self ,section:'ISection')->int:
        """
    <summary>
        Adds a section to end of document.
    </summary>
    <param name="section">The section.</param>
    <returns></returns>
        """
        intPtrsection:c_void_p = section.Ptr

        GetDllLibDoc().SectionCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().SectionCollection_Add.restype=c_int
        ret = GetDllLibDoc().SectionCollection_Add(self.Ptr, intPtrsection)
        return ret


    def IndexOf(self ,section:'ISection')->int:
        """
    <summary>
        Returns the zero-based index of the specified section.
    </summary>
    <param name="section">The section.</param>
    <returns></returns>
        """
        intPtrsection:c_void_p = section.Ptr

        GetDllLibDoc().SectionCollection_IndexOf.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().SectionCollection_IndexOf.restype=c_int
        ret = GetDllLibDoc().SectionCollection_IndexOf(self.Ptr, intPtrsection)
        return ret

