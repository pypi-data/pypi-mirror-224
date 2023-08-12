from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MergeImageFieldEventHandler (SpireObject) :
    """
    <summary>
        Represents the Method that handles MergeImageField event
    </summary>
    """

    def Invoke(self ,sender:'SpireObject',args:'MergeImageFieldEventArgs'):
        """

        """
        intPtrsender:c_void_p = sender.Ptr
        intPtrargs:c_void_p = args.Ptr

        GetDllLibDoc().MergeImageFieldEventHandler_Invoke.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().MergeImageFieldEventHandler_Invoke(self.Ptr, intPtrsender,intPtrargs)

#
#    def BeginInvoke(self ,sender:'SpireObject',args:'MergeImageFieldEventArgs',callback:'AsyncCallback',object:'SpireObject')->'IAsyncResult':
#        """
#
#        """
#        intPtrsender:c_void_p = sender.Ptr
#        intPtrargs:c_void_p = args.Ptr
#        intPtrcallback:c_void_p = callback.Ptr
#        intPtrobject:c_void_p = object.Ptr
#
#        GetDllLibDoc().MergeImageFieldEventHandler_BeginInvoke.argtypes=[c_void_p ,c_void_p,c_void_p,c_void_p,c_void_p]
#        GetDllLibDoc().MergeImageFieldEventHandler_BeginInvoke.restype=c_void_p
#        intPtr = GetDllLibDoc().MergeImageFieldEventHandler_BeginInvoke(self.Ptr, intPtrsender,intPtrargs,intPtrcallback,intPtrobject)
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
#        GetDllLibDoc().MergeImageFieldEventHandler_EndInvoke.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().MergeImageFieldEventHandler_EndInvoke(self.Ptr, intPtrresult)


