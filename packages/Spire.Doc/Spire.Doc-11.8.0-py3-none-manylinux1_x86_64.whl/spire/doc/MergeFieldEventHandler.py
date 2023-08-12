from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MergeFieldEventHandler (SpireObject) :
    """
    <summary>
        Represents the mail merge functionality. 
    </summary>
    <summary>
        Represents the MergeField event
    </summary>
    """

    def Invoke(self ,sender:'SpireObject',args:'MergeFieldEventArgs'):
        """

        """
        intPtrsender:c_void_p = sender.Ptr
        intPtrargs:c_void_p = args.Ptr

        GetDllLibDoc().MergeFieldEventHandler_Invoke.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().MergeFieldEventHandler_Invoke(self.Ptr, intPtrsender,intPtrargs)

#
#    def BeginInvoke(self ,sender:'SpireObject',args:'MergeFieldEventArgs',callback:'AsyncCallback',object:'SpireObject')->'IAsyncResult':
#        """
#
#        """
#        intPtrsender:c_void_p = sender.Ptr
#        intPtrargs:c_void_p = args.Ptr
#        intPtrcallback:c_void_p = callback.Ptr
#        intPtrobject:c_void_p = object.Ptr
#
#        GetDllLibDoc().MergeFieldEventHandler_BeginInvoke.argtypes=[c_void_p ,c_void_p,c_void_p,c_void_p,c_void_p]
#        GetDllLibDoc().MergeFieldEventHandler_BeginInvoke.restype=c_void_p
#        intPtr = GetDllLibDoc().MergeFieldEventHandler_BeginInvoke(self.Ptr, intPtrsender,intPtrargs,intPtrcallback,intPtrobject)
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
#        GetDllLibDoc().MergeFieldEventHandler_EndInvoke.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().MergeFieldEventHandler_EndInvoke(self.Ptr, intPtrresult)


