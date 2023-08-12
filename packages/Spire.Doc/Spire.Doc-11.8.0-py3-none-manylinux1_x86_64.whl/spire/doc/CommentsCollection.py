from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CommentsCollection (  CollectionEx) :
    """
    <summary>
        A collection of <see cref="!:Spire.Doc.CommentsCollection" /> objects that 
            represent the comments in the document.
    </summary>
    """

    def get_Item(self ,index:int)->'Comment':
        """
    <summary>
        Gets the comment at specified index.
    </summary>
<value></value>
    <returns></returns>
        """
        
        GetDllLibDoc().CommentsCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().CommentsCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().CommentsCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else Comment(intPtr)
        return ret


    def Counts(self)->int:
        """
    <summary>
        Counts this instance.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().CommentsCollection_Counts.argtypes=[c_void_p]
        GetDllLibDoc().CommentsCollection_Counts.restype=c_int
        ret = GetDllLibDoc().CommentsCollection_Counts(self.Ptr)
        return ret


    def RemoveAt(self ,index:int):
        """
    <summary>
        Remove a Comment at specified index.
    </summary>
    <param name="index"></param>
        """
        
        GetDllLibDoc().CommentsCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().CommentsCollection_RemoveAt(self.Ptr, index)

    def Clear(self):
        """
    <summary>
        Remove all the Comment from the document.
    </summary>
        """
        GetDllLibDoc().CommentsCollection_Clear.argtypes=[c_void_p]
        GetDllLibDoc().CommentsCollection_Clear(self.Ptr)


    def Remove(self ,comment:'Comment'):
        """
    <summary>
        Removes the specified Comment.
    </summary>
    <param name="comment"></param>
        """
        intPtrcomment:c_void_p = comment.Ptr

        GetDllLibDoc().CommentsCollection_Remove.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().CommentsCollection_Remove(self.Ptr, intPtrcomment)

