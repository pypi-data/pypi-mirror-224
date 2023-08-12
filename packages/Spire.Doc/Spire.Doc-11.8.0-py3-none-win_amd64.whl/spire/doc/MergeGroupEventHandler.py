from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MergeGroupEventHandler (SpireObject) :
    """
    <summary>
        Represents the Method that handles Merage group event.
    </summary>
    <param name="doc">Document object</param>
    <param name="Name">Group or table name</param>
    <param name="rowIndex">Represents the Row Index.</param>
    <param name="IsTable">Indicates is table, otherwise is group</param>
    """

    def Invoke(self ,sender:'SpireObject',args:'MergeGroupEventArgs'):
        """

        """
        intPtrsender:c_void_p = sender.Ptr
        intPtrargs:c_void_p = args.Ptr

        GetDllLibDoc().MergeGroupEventHandler_Invoke.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().MergeGroupEventHandler_Invoke(self.Ptr, intPtrsender,intPtrargs)

#
#    def BeginInvoke(self ,sender:'SpireObject',args:'MergeGroupEventArgs',callback:'AsyncCallback',object:'SpireObject')->'IAsyncResult':
#        """
#
#        """
#        intPtrsender:c_void_p = sender.Ptr
#        intPtrargs:c_void_p = args.Ptr
#        intPtrcallback:c_void_p = callback.Ptr
#        intPtrobject:c_void_p = object.Ptr
#
#        GetDllLibDoc().MergeGroupEventHandler_BeginInvoke.argtypes=[c_void_p ,c_void_p,c_void_p,c_void_p,c_void_p]
#        GetDllLibDoc().MergeGroupEventHandler_BeginInvoke.restype=c_void_p
#        intPtr = GetDllLibDoc().MergeGroupEventHandler_BeginInvoke(self.Ptr, intPtrsender,intPtrargs,intPtrcallback,intPtrobject)
#        ret = None if intPtr==None else IAsyncResult(intPtr)
#        return ret
#


#
#    def EndInvoke(self ,result:'IAsyncResult'):
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        GetDllLibDoc().MergeGroupEventHandler_EndInvoke.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().MergeGroupEventHandler_EndInvoke(self.Ptr, intPtrresult)


