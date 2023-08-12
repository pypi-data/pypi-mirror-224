from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ViewSetup (  DocumentSerializable) :
    """

    """
    @property
    def ZoomPercent(self)->int:
        """
    <summary>
        Returns or sets zooming value in percents
    </summary>
<value>The zoom percent.</value>
        """
        GetDllLibDoc().ViewSetup_get_ZoomPercent.argtypes=[c_void_p]
        GetDllLibDoc().ViewSetup_get_ZoomPercent.restype=c_int
        ret = GetDllLibDoc().ViewSetup_get_ZoomPercent(self.Ptr)
        return ret

    @ZoomPercent.setter
    def ZoomPercent(self, value:int):
        GetDllLibDoc().ViewSetup_set_ZoomPercent.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ViewSetup_set_ZoomPercent(self.Ptr, value)

    @property

    def ZoomType(self)->'ZoomType':
        """
    <summary>
        Returns or sets zooming type
    </summary>
<value>The type of the zoom.</value>
        """
        GetDllLibDoc().ViewSetup_get_ZoomType.argtypes=[c_void_p]
        GetDllLibDoc().ViewSetup_get_ZoomType.restype=c_int
        ret = GetDllLibDoc().ViewSetup_get_ZoomType(self.Ptr)
        objwraped = ZoomType(ret)
        return objwraped

    @ZoomType.setter
    def ZoomType(self, value:'ZoomType'):
        GetDllLibDoc().ViewSetup_set_ZoomType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ViewSetup_set_ZoomType(self.Ptr, value.value)

    @property

    def DocumentViewType(self)->'DocumentViewType':
        """
    <summary>
        Returns or sets document view mode
    </summary>
<value>The type of the document view.</value>
        """
        GetDllLibDoc().ViewSetup_get_DocumentViewType.argtypes=[c_void_p]
        GetDllLibDoc().ViewSetup_get_DocumentViewType.restype=c_int
        ret = GetDllLibDoc().ViewSetup_get_DocumentViewType(self.Ptr)
        objwraped = DocumentViewType(ret)
        return objwraped

    @DocumentViewType.setter
    def DocumentViewType(self, value:'DocumentViewType'):
        GetDllLibDoc().ViewSetup_set_DocumentViewType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ViewSetup_set_DocumentViewType(self.Ptr, value.value)

    @staticmethod
    def DEF_ZOOMING()->int:
        """
    <summary>
        Constant value for Zoom.
    </summary>
        """
        #GetDllLibDoc().ViewSetup_DEF_ZOOMING.argtypes=[]
        GetDllLibDoc().ViewSetup_DEF_ZOOMING.restype=c_int
        ret = GetDllLibDoc().ViewSetup_DEF_ZOOMING()
        return ret

