from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PageLayoutHandler (SpireObject) :
    """
    <summary>
        Represents the method that will handle an event that with event data.
    </summary>
    <param name="sender">The source of the event</param>
    <param name="args">args that contains event data</param>
    """

    def Invoke(self ,sender:'SpireObject',args:'PageLayoutEventArgs'):
        """

        """
        intPtrsender:c_void_p = sender.Ptr
        intPtrargs:c_void_p = args.Ptr

        GetDllLibDoc().PageLayoutHandler_Invoke.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().PageLayoutHandler_Invoke(self.Ptr, intPtrsender,intPtrargs)

#
#    def BeginInvoke(self ,sender:'SpireObject',args:'PageLayoutEventArgs',callback:'AsyncCallback',object:'SpireObject')->'IAsyncResult':
#        """
#
#        """
#        intPtrsender:c_void_p = sender.Ptr
#        intPtrargs:c_void_p = args.Ptr
#        intPtrcallback:c_void_p = callback.Ptr
#        intPtrobject:c_void_p = object.Ptr
#
#        GetDllLibDoc().PageLayoutHandler_BeginInvoke.argtypes=[c_void_p ,c_void_p,c_void_p,c_void_p,c_void_p]
#        GetDllLibDoc().PageLayoutHandler_BeginInvoke.restype=c_void_p
#        intPtr = GetDllLibDoc().PageLayoutHandler_BeginInvoke(self.Ptr, intPtrsender,intPtrargs,intPtrcallback,intPtrobject)
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
#        GetDllLibDoc().PageLayoutHandler_EndInvoke.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().PageLayoutHandler_EndInvoke(self.Ptr, intPtrresult)


