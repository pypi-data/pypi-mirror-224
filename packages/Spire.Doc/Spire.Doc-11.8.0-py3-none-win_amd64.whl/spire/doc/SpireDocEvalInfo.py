from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SpireDocEvalInfo (SpireObject) :
    """
    <summary>
        Represents the method that will handle an event that with event data.
    </summary>
    <param name="sender">The source of the event.</param>
    <param name="args">The args that contains event data.</param>
    """

    def Invoke(self ,sender:'SpireObject',args:str):
        """

        """
        argsPtr = StrToPtr(args)
        intPtrsender:c_void_p = sender.Ptr

        GetDllLibDoc().SpireDocEvalInfo_Invoke.argtypes=[c_void_p ,c_void_p,c_char_p]
        GetDllLibDoc().SpireDocEvalInfo_Invoke(self.Ptr, intPtrsender,argsPtr)

#
#    def BeginInvoke(self ,sender:'SpireObject',args:str,callback:'AsyncCallback',object:'SpireObject')->'IAsyncResult':
#        """
#
#        """
#        intPtrsender:c_void_p = sender.Ptr
#        intPtrcallback:c_void_p = callback.Ptr
#        intPtrobject:c_void_p = object.Ptr
#
#        GetDllLibDoc().SpireDocEvalInfo_BeginInvoke.argtypes=[c_void_p ,c_void_p,c_wchar_p,c_void_p,c_void_p]
#        GetDllLibDoc().SpireDocEvalInfo_BeginInvoke.restype=c_void_p
#        intPtr = GetDllLibDoc().SpireDocEvalInfo_BeginInvoke(self.Ptr, intPtrsender,args,intPtrcallback,intPtrobject)
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
#        GetDllLibDoc().SpireDocEvalInfo_EndInvoke.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().SpireDocEvalInfo_EndInvoke(self.Ptr, intPtrresult)


