from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SubSetEnumerator (  IEnumerator) :
    """
    <summary>
        Represents a internal enumerator for EntitySubSetCollection. 
    </summary>
    """
    @property

    def Current(self)->'SpireObject':
        """
    <summary>
        Gets the current element in the collection.
    </summary>
<value></value>
    <returns>The current element in the collection.</returns>
<exception cref="T:System.InvalidOperationException">The enumerator is positioned before the first element of the collection or after the last element. </exception>
        """
        GetDllLibDoc().SubSetEnumerator_get_Current.argtypes=[c_void_p]
        GetDllLibDoc().SubSetEnumerator_get_Current.restype=c_void_p
        intPtr = GetDllLibDoc().SubSetEnumerator_get_Current(self.Ptr)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret


    def MoveNext(self)->bool:
        """
    <summary>
        Advances the enumerator to the next element of the collection.
    </summary>
    <returns>
            true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
            </returns>
<exception cref="T:System.InvalidOperationException">The collection was modified after the enumerator was created. </exception>
        """
        GetDllLibDoc().SubSetEnumerator_MoveNext.argtypes=[c_void_p]
        GetDllLibDoc().SubSetEnumerator_MoveNext.restype=c_bool
        ret = GetDllLibDoc().SubSetEnumerator_MoveNext(self.Ptr)
        return ret

    def Reset(self):
        """
    <summary>
        Sets the enumerator to its initial position, which is before the first element in the collection.
    </summary>
<exception cref="T:System.InvalidOperationException">The collection was modified after the enumerator was created. </exception>
        """
        GetDllLibDoc().SubSetEnumerator_Reset.argtypes=[c_void_p]
        GetDllLibDoc().SubSetEnumerator_Reset(self.Ptr)

