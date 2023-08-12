from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IfField (  Field) :
    """

    """
    @dispatch
    def __init__(self, doc:IDocument):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().IfField_CreateIfFieldD.argtypes=[c_void_p]
        GetDllLibDoc().IfField_CreateIfFieldD.restype=c_void_p
        intPtr = GetDllLibDoc().IfField_CreateIfFieldD(intPdoc)
        super(IfField, self).__init__(intPtr)
