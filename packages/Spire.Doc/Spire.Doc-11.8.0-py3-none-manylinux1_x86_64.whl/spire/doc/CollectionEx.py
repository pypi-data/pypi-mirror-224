from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CollectionEx (  OwnerHolder, IEnumerable) :
    """

    """
    @property
    def Count(self)->int:
        """
    <summary>
        Gets the number of items in the collection.
    </summary>
<value>The count.</value>
        """
        GetDllLibDoc().CollectionEx_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().CollectionEx_get_Count.restype=c_int
        ret = GetDllLibDoc().CollectionEx_get_Count(self.Ptr)
        return ret


    def GetEnumerator(self)->'IEnumerator':
        """
    <summary>
        Returns an enumerator that iterates through a collection.
    </summary>
    <returns>
            An <see cref="T:System.Collections.IEnumerator"></see> object that can be used to iterate through the collection.
            </returns>
        """
        GetDllLibDoc().CollectionEx_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().CollectionEx_GetEnumerator.restype=c_void_p
        intPtr = GetDllLibDoc().CollectionEx_GetEnumerator(self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret


