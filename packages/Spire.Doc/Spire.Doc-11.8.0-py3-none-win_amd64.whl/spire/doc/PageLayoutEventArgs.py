from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PageLayoutEventArgs (SpireObject) :
    """
    <summary>
        Spire.Doc.Documents.Rendering.DocumentLayouter.PageLayoutEventArgs is the class containg event data
     </summary>
    """
    @property
    def PageIndex(self)->int:
        """
    <summary>
        Represents the page number of documents.
    </summary>
        """
        GetDllLibDoc().PageLayoutEventArgs_get_PageIndex.argtypes=[c_void_p]
        GetDllLibDoc().PageLayoutEventArgs_get_PageIndex.restype=c_int
        ret = GetDllLibDoc().PageLayoutEventArgs_get_PageIndex(self.Ptr)
        return ret

    @PageIndex.setter
    def PageIndex(self, value:int):
        GetDllLibDoc().PageLayoutEventArgs_set_PageIndex.argtypes=[c_void_p, c_int]
        GetDllLibDoc().PageLayoutEventArgs_set_PageIndex(self.Ptr, value)

    @property

    def PageSetup(self)->'PageSetup':
        """
    <summary>
        Represents the document page informations.
    </summary>
        """
        GetDllLibDoc().PageLayoutEventArgs_get_PageSetup.argtypes=[c_void_p]
        GetDllLibDoc().PageLayoutEventArgs_get_PageSetup.restype=c_void_p
        intPtr = GetDllLibDoc().PageLayoutEventArgs_get_PageSetup(self.Ptr)
        ret = None if intPtr==None else PageSetup(intPtr)
        return ret


    @PageSetup.setter
    def PageSetup(self, value:'PageSetup'):
        GetDllLibDoc().PageLayoutEventArgs_set_PageSetup.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().PageLayoutEventArgs_set_PageSetup(self.Ptr, value.Ptr)

