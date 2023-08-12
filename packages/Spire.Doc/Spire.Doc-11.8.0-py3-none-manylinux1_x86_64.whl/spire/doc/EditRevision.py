from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class EditRevision (  RevisionBase) :
    """

    """
    @property

    def Type(self)->'EditRevisionType':
        """

        """
        GetDllLibDoc().EditRevision_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().EditRevision_get_Type.restype=c_int
        ret = GetDllLibDoc().EditRevision_get_Type(self.Ptr)
        objwraped = EditRevisionType(ret)
        return objwraped

