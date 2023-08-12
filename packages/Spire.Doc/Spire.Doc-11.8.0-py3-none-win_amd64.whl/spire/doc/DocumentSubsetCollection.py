from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentSubsetCollection (  OwnerHolder, IDocumentObjectCollection, ICollectionBase, IEnumerable) :
    """
    <summary>
        Represents a subset from collection of specified type entities.
    </summary>
    """
    @property

    def Document(self)->'Document':
        """
    <summary>
        Gets the document.
    </summary>
<value>The document.</value>
        """
        GetDllLibDoc().DocumentSubsetCollection_get_Document.argtypes=[c_void_p]
        GetDllLibDoc().DocumentSubsetCollection_get_Document.restype=c_void_p
        intPtr = GetDllLibDoc().DocumentSubsetCollection_get_Document(self.Ptr)
        ret = None if intPtr==None else Document(intPtr)
        return ret


    @property

    def Owner(self)->'DocumentObject':
        """
    <summary>
        Gets the owner.
    </summary>
<value>The owner.</value>
        """
        GetDllLibDoc().DocumentSubsetCollection_get_Owner.argtypes=[c_void_p]
        GetDllLibDoc().DocumentSubsetCollection_get_Owner.restype=c_void_p
        intPtr = GetDllLibDoc().DocumentSubsetCollection_get_Owner(self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


    @property
    def Count(self)->int:
        """
    <summary>
        Gets the count.
    </summary>
<value>The count.</value>
        """
        GetDllLibDoc().DocumentSubsetCollection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().DocumentSubsetCollection_get_Count.restype=c_int
        ret = GetDllLibDoc().DocumentSubsetCollection_get_Count(self.Ptr)
        return ret


    def get_Item(self ,index:int)->'DocumentObject':
        """
    <summary>
        Gets the <see cref="T:Spire.Doc.DocumentObject" /> at the specified index.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().DocumentSubsetCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().DocumentSubsetCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().DocumentSubsetCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


    def Clear(self):
        """
    <summary>
        Removes all entities 
    </summary>
        """
        GetDllLibDoc().DocumentSubsetCollection_Clear.argtypes=[c_void_p]
        GetDllLibDoc().DocumentSubsetCollection_Clear(self.Ptr)


    def GetEnumerator(self)->'IEnumerator':
        """
    <summary>
        Returns an enumerator that iterates through a collection.
    </summary>
    <returns>
            An <see cref="T:System.Collections.IEnumerator"></see> object that can be used to iterate through the collection.
            </returns>
        """
        GetDllLibDoc().DocumentSubsetCollection_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().DocumentSubsetCollection_GetEnumerator.restype=c_void_p
        intPtr = GetDllLibDoc().DocumentSubsetCollection_GetEnumerator(self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret


