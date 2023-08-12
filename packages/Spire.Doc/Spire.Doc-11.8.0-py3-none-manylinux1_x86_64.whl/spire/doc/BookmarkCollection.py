from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BookmarkCollection (  CollectionEx) :
    """
    <summary>
        A collection of <see cref="T:Spire.Doc.Bookmark" /> objects that 
            represent the bookmarks in the document.
    </summary>
    """
    @dispatch

    def get_Item(self ,name:str)->Bookmark:
        """
    <summary>
        Gets the <see cref="T:Spire.Doc.Bookmark" /> with the specified name.
    </summary>
<value></value>
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().BookmarkCollection_get_Item.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().BookmarkCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().BookmarkCollection_get_Item(self.Ptr, namePtr)
        ret = None if intPtr==None else Bookmark(intPtr)
        return ret


    @dispatch

    def get_Item(self ,index:int)->Bookmark:
        """
    <summary>
        Gets the <see cref="T:Spire.Doc.Bookmark" /> at the specified index.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().BookmarkCollection_get_ItemI.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().BookmarkCollection_get_ItemI.restype=c_void_p
        intPtr = GetDllLibDoc().BookmarkCollection_get_ItemI(self.Ptr, index)
        ret = None if intPtr==None else Bookmark(intPtr)
        return ret



    def FindByName(self ,name:str)->'Bookmark':
        """
    <summary>
        Finds <see cref="T:Spire.Doc.Bookmark" /> object by specified name
    </summary>
    <param name="name">The bookmark name</param>
    <returns></returns>
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().BookmarkCollection_FindByName.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().BookmarkCollection_FindByName.restype=c_void_p
        intPtr = GetDllLibDoc().BookmarkCollection_FindByName(self.Ptr, namePtr)
        ret = None if intPtr==None else Bookmark(intPtr)
        return ret



    def RemoveAt(self ,index:int):
        """
    <summary>
        Removes a bookmark at the specified index.
    </summary>
    <param name="index">The index.</param>
        """
        
        GetDllLibDoc().BookmarkCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().BookmarkCollection_RemoveAt(self.Ptr, index)


    def Remove(self ,bookmark:'Bookmark'):
        """
    <summary>
        Removes the specified bookmark.
    </summary>
    <param name="bookmark">The bookmark.</param>
        """
        intPtrbookmark:c_void_p = bookmark.Ptr

        GetDllLibDoc().BookmarkCollection_Remove.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().BookmarkCollection_Remove(self.Ptr, intPtrbookmark)

    def Clear(self):
        """
    <summary>
        Removes all bookmarks from the document. 
    </summary>
        """
        GetDllLibDoc().BookmarkCollection_Clear.argtypes=[c_void_p]
        GetDllLibDoc().BookmarkCollection_Clear(self.Ptr)

