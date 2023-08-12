from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Tab (  DocumentSerializable) :
    """

    """
    @property

    def Justification(self)->'TabJustification':
        """
    <summary>
        Gets or sets the justification.
    </summary>
<value>The justification.</value>
        """
        GetDllLibDoc().Tab_get_Justification.argtypes=[c_void_p]
        GetDllLibDoc().Tab_get_Justification.restype=c_int
        ret = GetDllLibDoc().Tab_get_Justification(self.Ptr)
        objwraped = TabJustification(ret)
        return objwraped

    @Justification.setter
    def Justification(self, value:'TabJustification'):
        GetDllLibDoc().Tab_set_Justification.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Tab_set_Justification(self.Ptr, value.value)

    @property

    def TabLeader(self)->'TabLeader':
        """
    <summary>
        Gets or sets the tab leader.
    </summary>
<value>The tab leader.</value>
        """
        GetDllLibDoc().Tab_get_TabLeader.argtypes=[c_void_p]
        GetDllLibDoc().Tab_get_TabLeader.restype=c_int
        ret = GetDllLibDoc().Tab_get_TabLeader(self.Ptr)
        objwraped = TabLeader(ret)
        return objwraped

    @TabLeader.setter
    def TabLeader(self, value:'TabLeader'):
        GetDllLibDoc().Tab_set_TabLeader.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Tab_set_TabLeader(self.Ptr, value.value)

    @property
    def Position(self)->float:
        """
    <summary>
        Gets or sets the position.
    </summary>
<value>The position.</value>
        """
        GetDllLibDoc().Tab_get_Position.argtypes=[c_void_p]
        GetDllLibDoc().Tab_get_Position.restype=c_float
        ret = GetDllLibDoc().Tab_get_Position(self.Ptr)
        return ret

    @Position.setter
    def Position(self, value:float):
        GetDllLibDoc().Tab_set_Position.argtypes=[c_void_p, c_float]
        GetDllLibDoc().Tab_set_Position(self.Ptr, value)


    def Equals(self ,tab:'Tab')->bool:
        """

        """
        intPtrtab:c_void_p = tab.Ptr

        GetDllLibDoc().Tab_Equals.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Tab_Equals.restype=c_bool
        ret = GetDllLibDoc().Tab_Equals(self.Ptr, intPtrtab)
        return ret

