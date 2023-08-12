from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MergeGroupEventArgs (SpireObject) :
    """

    """
    @property

    def Document(self)->'IDocument':
        """
    <summary>
        Gets the document.
    </summary>
        """
        GetDllLibDoc().MergeGroupEventArgs_get_Document.argtypes=[c_void_p]
        GetDllLibDoc().MergeGroupEventArgs_get_Document.restype=c_void_p
        intPtr = GetDllLibDoc().MergeGroupEventArgs_get_Document(self.Ptr)
        ret = None if intPtr==None else IDocument(intPtr)
        return ret


    @property

    def TableName(self)->str:
        """
    <summary>
        Gets the Table Name
    </summary>
        """
        GetDllLibDoc().MergeGroupEventArgs_get_TableName.argtypes=[c_void_p]
        GetDllLibDoc().MergeGroupEventArgs_get_TableName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeGroupEventArgs_get_TableName(self.Ptr))
        return ret


    @property

    def GroupName(self)->str:
        """
    <summary>
        Gets the group name.
    </summary>
        """
        GetDllLibDoc().MergeGroupEventArgs_get_GroupName.argtypes=[c_void_p]
        GetDllLibDoc().MergeGroupEventArgs_get_GroupName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeGroupEventArgs_get_GroupName(self.Ptr))
        return ret


    @property

    def MergeField(self)->'IMergeField':
        """
    <summary>
        Gets the merge field.
    </summary>
        """
        GetDllLibDoc().MergeGroupEventArgs_get_MergeField.argtypes=[c_void_p]
        GetDllLibDoc().MergeGroupEventArgs_get_MergeField.restype=c_void_p
        intPtr = GetDllLibDoc().MergeGroupEventArgs_get_MergeField(self.Ptr)
        ret = None if intPtr==None else IMergeField(intPtr)
        return ret


    @property
    def RowIndex(self)->int:
        """
    <summary>
        Gets the index of the row.
    </summary>
        """
        GetDllLibDoc().MergeGroupEventArgs_get_RowIndex.argtypes=[c_void_p]
        GetDllLibDoc().MergeGroupEventArgs_get_RowIndex.restype=c_int
        ret = GetDllLibDoc().MergeGroupEventArgs_get_RowIndex(self.Ptr)
        return ret

    @property
    def RowCount(self)->int:
        """
    <summary>
        Gets the count of the row.
    </summary>
        """
        GetDllLibDoc().MergeGroupEventArgs_get_RowCount.argtypes=[c_void_p]
        GetDllLibDoc().MergeGroupEventArgs_get_RowCount.restype=c_int
        ret = GetDllLibDoc().MergeGroupEventArgs_get_RowCount(self.Ptr)
        return ret

    @property

    def EventType(self)->'GroupEventType':
        """

        """
        GetDllLibDoc().MergeGroupEventArgs_get_EventType.argtypes=[c_void_p]
        GetDllLibDoc().MergeGroupEventArgs_get_EventType.restype=c_int
        ret = GetDllLibDoc().MergeGroupEventArgs_get_EventType(self.Ptr)
        objwraped = GroupEventType(ret)
        return objwraped

