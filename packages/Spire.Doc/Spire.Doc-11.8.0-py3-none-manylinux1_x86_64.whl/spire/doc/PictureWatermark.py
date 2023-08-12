from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PictureWatermark (  WatermarkBase) :
    """

    """
    def __init__(self):
        GetDllLibDoc().PictureWatermark_CreatePictureWatermark.restype = c_void_p
        intPtr = GetDllLibDoc().PictureWatermark_CreatePictureWatermark()
        super(PictureWatermark, self).__init__(intPtr)


    @property
    def Scaling(self)->float:
        """
    <summary>
        Gets or sets picture scaling in percents.
    </summary>
        """
        GetDllLibDoc().PictureWatermark_get_Scaling.argtypes=[c_void_p]
        GetDllLibDoc().PictureWatermark_get_Scaling.restype=c_float
        ret = GetDllLibDoc().PictureWatermark_get_Scaling(self.Ptr)
        return ret

    @Scaling.setter
    def Scaling(self, value:float):
        GetDllLibDoc().PictureWatermark_set_Scaling.argtypes=[c_void_p, c_float]
        GetDllLibDoc().PictureWatermark_set_Scaling(self.Ptr, value)

    @property
    def IsWashout(self)->bool:
        """
    <summary>
        Gets or sets washout property for Picture watermark.
    </summary>
        """
        GetDllLibDoc().PictureWatermark_get_IsWashout.argtypes=[c_void_p]
        GetDllLibDoc().PictureWatermark_get_IsWashout.restype=c_bool
        ret = GetDllLibDoc().PictureWatermark_get_IsWashout(self.Ptr)
        return ret

    @IsWashout.setter
    def IsWashout(self, value:bool):
        GetDllLibDoc().PictureWatermark_set_IsWashout.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().PictureWatermark_set_IsWashout(self.Ptr, value)

    @dispatch

    def SetPicture(self ,ImgFile:str):
        """
    <summary>
        Sets the picture.
    </summary>
    <param name="ImgFile">The image file.</param>
        """
        ImgFilePtr = StrToPtr(ImgFile)
        GetDllLibDoc().PictureWatermark_SetPicture.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().PictureWatermark_SetPicture(self.Ptr, ImgFilePtr)

    @dispatch

    def SetPicture(self ,imgStream:Stream):
        """
    <summary>
        Sets the picture.
    </summary>
    <param name="imgStream">The img stream.</param>
        """
        intPtrimgStream:c_void_p = imgStream.Ptr

        GetDllLibDoc().PictureWatermark_SetPictureI.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().PictureWatermark_SetPictureI(self.Ptr, intPtrimgStream)

