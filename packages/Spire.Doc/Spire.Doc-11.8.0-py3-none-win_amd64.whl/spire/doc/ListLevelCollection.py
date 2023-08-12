from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListLevelCollection (  DocumentSerializableCollection) :
    """
    <summary>
        Represents a collections of list formatting for each level in a list.
    </summary>
    """

    def get_Item(self ,index:int)->'ListLevel':
        """
    <summary>
        Gets the <see cref="!:Spire.Doc.WListLevel" /> at the specified index.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().ListLevelCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ListLevelCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().ListLevelCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else ListLevel(intPtr)
        return ret


