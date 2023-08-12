from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BookmarkLevelHandler (SpireObject) :
    """
    <summary>
        Represents the method that will handle an event that with event data.
    </summary>
    <param name="sender">The source of the event</param>
    <param name="args">args that contains event data</param>
    """

    def Invoke(self ,sender:'SpireObject',args:'BookmarkLevelEventArgs'):
        """

        """
        intPtrsender:c_void_p = sender.Ptr
        intPtrargs:c_void_p = args.Ptr

        GetDllLibDoc().BookmarkLevelHandler_Invoke.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().BookmarkLevelHandler_Invoke(self.Ptr, intPtrsender,intPtrargs)

#
#    def BeginInvoke(self ,sender:'SpireObject',args:'BookmarkLevelEventArgs',callback:'AsyncCallback',object:'SpireObject')->'IAsyncResult':
#        """
#
#        """
#        intPtrsender:c_void_p = sender.Ptr
#        intPtrargs:c_void_p = args.Ptr
#        intPtrcallback:c_void_p = callback.Ptr
#        intPtrobject:c_void_p = object.Ptr
#
#        GetDllLibDoc().BookmarkLevelHandler_BeginInvoke.argtypes=[c_void_p ,c_void_p,c_void_p,c_void_p,c_void_p]
#        GetDllLibDoc().BookmarkLevelHandler_BeginInvoke.restype=c_void_p
#        intPtr = GetDllLibDoc().BookmarkLevelHandler_BeginInvoke(self.Ptr, intPtrsender,intPtrargs,intPtrcallback,intPtrobject)
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
#        GetDllLibDoc().BookmarkLevelHandler_EndInvoke.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().BookmarkLevelHandler_EndInvoke(self.Ptr, intPtrresult)


