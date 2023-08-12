from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MailMergeDataTable (SpireObject) :
    """

    """
    @property

    def GroupName(self)->str:
        """

        """
        GetDllLibDoc().MailMergeDataTable_get_GroupName.argtypes=[c_void_p]
        GetDllLibDoc().MailMergeDataTable_get_GroupName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MailMergeDataTable_get_GroupName(self.Ptr))
        return ret


    @property

    def SourceData(self)->'IEnumerator':
        """

        """
        GetDllLibDoc().MailMergeDataTable_get_SourceData.argtypes=[c_void_p]
        GetDllLibDoc().MailMergeDataTable_get_SourceData.restype=c_void_p
        intPtr = GetDllLibDoc().MailMergeDataTable_get_SourceData(self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret


