from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Frame (  WordAttrCollection) :
    """
    <summary>
        Represents Frame object used in framed document.
    </summary>
    """
    @property
    def FrameAnchorLock(self)->bool:
        """
    <summary>
        Gets or Sets whether lock the anchor of Frame or not.
    </summary>
        """
        GetDllLibDoc().Frame_get_FrameAnchorLock.argtypes=[c_void_p]
        GetDllLibDoc().Frame_get_FrameAnchorLock.restype=c_bool
        ret = GetDllLibDoc().Frame_get_FrameAnchorLock(self.Ptr)
        return ret

    @FrameAnchorLock.setter
    def FrameAnchorLock(self, value:bool):
        GetDllLibDoc().Frame_set_FrameAnchorLock.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Frame_set_FrameAnchorLock(self.Ptr, value)

    @property

    def FrameHorizontalPosition(self)->'HorizontalPosition':
        """
    <summary>
        Gets or Sets Horizontal Position of Frame.
    </summary>
        """
        GetDllLibDoc().Frame_get_FrameHorizontalPosition.argtypes=[c_void_p]
        GetDllLibDoc().Frame_get_FrameHorizontalPosition.restype=c_int
        ret = GetDllLibDoc().Frame_get_FrameHorizontalPosition(self.Ptr)
        objwraped = HorizontalPosition(ret)
        return objwraped

    @FrameHorizontalPosition.setter
    def FrameHorizontalPosition(self, value:'HorizontalPosition'):
        GetDllLibDoc().Frame_set_FrameHorizontalPosition.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Frame_set_FrameHorizontalPosition(self.Ptr, value.value)

    @property

    def FrameVerticalPosition(self)->'VerticalPosition':
        """
    <summary>
        Gets or Sets Vertical Position of Frame.
    </summary>
        """
        GetDllLibDoc().Frame_get_FrameVerticalPosition.argtypes=[c_void_p]
        GetDllLibDoc().Frame_get_FrameVerticalPosition.restype=c_int
        ret = GetDllLibDoc().Frame_get_FrameVerticalPosition(self.Ptr)
        objwraped = VerticalPosition(ret)
        return objwraped

    @FrameVerticalPosition.setter
    def FrameVerticalPosition(self, value:'VerticalPosition'):
        GetDllLibDoc().Frame_set_FrameVerticalPosition.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Frame_set_FrameVerticalPosition(self.Ptr, value.value)

    @property

    def FrameWidthRule(self)->'FrameSizeRule':
        """
    <summary>
        Gets or Sets Width Rule of Frame.
    </summary>
        """
        GetDllLibDoc().Frame_get_FrameWidthRule.argtypes=[c_void_p]
        GetDllLibDoc().Frame_get_FrameWidthRule.restype=c_int
        ret = GetDllLibDoc().Frame_get_FrameWidthRule(self.Ptr)
        objwraped = FrameSizeRule(ret)
        return objwraped

    @FrameWidthRule.setter
    def FrameWidthRule(self, value:'FrameSizeRule'):
        GetDllLibDoc().Frame_set_FrameWidthRule.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Frame_set_FrameWidthRule(self.Ptr, value.value)

    @property

    def FrameHeightRule(self)->'FrameSizeRule':
        """
    <summary>
        Gets or Sets Height Rule of Frame.
    </summary>
        """
        GetDllLibDoc().Frame_get_FrameHeightRule.argtypes=[c_void_p]
        GetDllLibDoc().Frame_get_FrameHeightRule.restype=c_int
        ret = GetDllLibDoc().Frame_get_FrameHeightRule(self.Ptr)
        objwraped = FrameSizeRule(ret)
        return objwraped

    @FrameHeightRule.setter
    def FrameHeightRule(self, value:'FrameSizeRule'):
        GetDllLibDoc().Frame_set_FrameHeightRule.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Frame_set_FrameHeightRule(self.Ptr, value.value)

    @property
    def WrapFrameAround(self)->bool:
        """
    <summary>
        Gets or Sets wrap type of Frame.
    </summary>
        """
        GetDllLibDoc().Frame_get_WrapFrameAround.argtypes=[c_void_p]
        GetDllLibDoc().Frame_get_WrapFrameAround.restype=c_bool
        ret = GetDllLibDoc().Frame_get_WrapFrameAround(self.Ptr)
        return ret

    @WrapFrameAround.setter
    def WrapFrameAround(self, value:bool):
        GetDllLibDoc().Frame_set_WrapFrameAround.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Frame_set_WrapFrameAround(self.Ptr, value)

    @property

    def FrameHorizontalOrigin(self)->'FrameHorzAnchor':
        """
    <summary>
        Gets or sets relative to what the frame is positioned horizontally. 
    </summary>
        """
        GetDllLibDoc().Frame_get_FrameHorizontalOrigin.argtypes=[c_void_p]
        GetDllLibDoc().Frame_get_FrameHorizontalOrigin.restype=c_int
        ret = GetDllLibDoc().Frame_get_FrameHorizontalOrigin(self.Ptr)
        objwraped = FrameHorzAnchor(ret)
        return objwraped

    @FrameHorizontalOrigin.setter
    def FrameHorizontalOrigin(self, value:'FrameHorzAnchor'):
        GetDllLibDoc().Frame_set_FrameHorizontalOrigin.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Frame_set_FrameHorizontalOrigin(self.Ptr, value.value)

    @property

    def FrameVerticalOrigin(self)->'FrameVertAnchor':
        """
    <summary>
        gets or sets relative to what the frame is positioned vertically. 
    </summary>
        """
        GetDllLibDoc().Frame_get_FrameVerticalOrigin.argtypes=[c_void_p]
        GetDllLibDoc().Frame_get_FrameVerticalOrigin.restype=c_int
        ret = GetDllLibDoc().Frame_get_FrameVerticalOrigin(self.Ptr)
        objwraped = FrameVertAnchor(ret)
        return objwraped

    @FrameVerticalOrigin.setter
    def FrameVerticalOrigin(self, value:'FrameVertAnchor'):
        GetDllLibDoc().Frame_set_FrameVerticalOrigin.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Frame_set_FrameVerticalOrigin(self.Ptr, value.value)

    def GetWidth(self)->float:
        """
    <summary>
        Gets width of this frame
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Frame_GetWidth.argtypes=[c_void_p]
        GetDllLibDoc().Frame_GetWidth.restype=c_float
        ret = GetDllLibDoc().Frame_GetWidth(self.Ptr)
        return ret


    def SetWidth(self ,value:float):
        """
    <summary>
        Sets width of this frame
    </summary>
    <param name="value"></param>
        """
        
        GetDllLibDoc().Frame_SetWidth.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().Frame_SetWidth(self.Ptr, value)

    def GetHeight(self)->float:
        """
    <summary>
        Gets height of this frame
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Frame_GetHeight.argtypes=[c_void_p]
        GetDllLibDoc().Frame_GetHeight.restype=c_float
        ret = GetDllLibDoc().Frame_GetHeight(self.Ptr)
        return ret


    def SetHeight(self ,value:float):
        """
    <summary>
        Sets height of this frame
    </summary>
    <param name="value"></param>
        """
        
        GetDllLibDoc().Frame_SetHeight.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().Frame_SetHeight(self.Ptr, value)

    def GetHorizontalPosition(self)->float:
        """
    <summary>
        Gets the position of the left edge of the frame
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Frame_GetHorizontalPosition.argtypes=[c_void_p]
        GetDllLibDoc().Frame_GetHorizontalPosition.restype=c_float
        ret = GetDllLibDoc().Frame_GetHorizontalPosition(self.Ptr)
        return ret


    def SetHorizontalPosition(self ,value:float):
        """
    <summary>
        Sets the position of the left edge of the frame
    </summary>
    <param name="value"></param>
        """
        
        GetDllLibDoc().Frame_SetHorizontalPosition.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().Frame_SetHorizontalPosition(self.Ptr, value)

    def GetHorizontalDistanceFromText(self)->float:
        """
    <summary>
        Gets the distance between the document text and left or right edge of the frame.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Frame_GetHorizontalDistanceFromText.argtypes=[c_void_p]
        GetDllLibDoc().Frame_GetHorizontalDistanceFromText.restype=c_float
        ret = GetDllLibDoc().Frame_GetHorizontalDistanceFromText(self.Ptr)
        return ret


    def SetHorizontalDistanceFromText(self ,value:float):
        """
    <summary>
        Sets the distance between the document text and left or right edge of the frame.
    </summary>
    <param name="value"></param>
        """
        
        GetDllLibDoc().Frame_SetHorizontalDistanceFromText.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().Frame_SetHorizontalDistanceFromText(self.Ptr, value)

    def GetVerticalPosition(self)->float:
        """
    <summary>
        Gets the position of the top edge of the frame
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Frame_GetVerticalPosition.argtypes=[c_void_p]
        GetDllLibDoc().Frame_GetVerticalPosition.restype=c_float
        ret = GetDllLibDoc().Frame_GetVerticalPosition(self.Ptr)
        return ret


    def SetVerticalPosition(self ,value:float):
        """
    <summary>
        Sets the position of the top edge of the frame
    </summary>
    <param name="value"></param>
        """
        
        GetDllLibDoc().Frame_SetVerticalPosition.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().Frame_SetVerticalPosition(self.Ptr, value)

    def GetVerticalDistanceFromText(self)->float:
        """
    <summary>
        Gets the distance between the document text and top or bottom edge of the frame.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Frame_GetVerticalDistanceFromText.argtypes=[c_void_p]
        GetDllLibDoc().Frame_GetVerticalDistanceFromText.restype=c_float
        ret = GetDllLibDoc().Frame_GetVerticalDistanceFromText(self.Ptr)
        return ret


    def SetVerticalDistanceFromText(self ,value:float):
        """
    <summary>
        Sets the distance between the document text and top or bottom edge of the frame.
    </summary>
    <param name="value"></param>
        """
        
        GetDllLibDoc().Frame_SetVerticalDistanceFromText.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().Frame_SetVerticalDistanceFromText(self.Ptr, value)

