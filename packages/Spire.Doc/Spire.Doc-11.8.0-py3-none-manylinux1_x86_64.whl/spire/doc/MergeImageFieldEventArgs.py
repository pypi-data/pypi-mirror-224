from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MergeImageFieldEventArgs (  MergeFieldEventArgs) :
    """
    <summary>
        Represents data during MergeImageField event.
    </summary>
    """
    @property
    def UseText(self)->bool:
        """

        """
        GetDllLibDoc().MergeImageFieldEventArgs_get_UseText.argtypes=[c_void_p]
        GetDllLibDoc().MergeImageFieldEventArgs_get_UseText.restype=c_bool
        ret = GetDllLibDoc().MergeImageFieldEventArgs_get_UseText(self.Ptr)
        return ret

    @property

    def ImageFileName(self)->str:
        """

        """
        GetDllLibDoc().MergeImageFieldEventArgs_get_ImageFileName.argtypes=[c_void_p]
        GetDllLibDoc().MergeImageFieldEventArgs_get_ImageFileName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().MergeImageFieldEventArgs_get_ImageFileName(self.Ptr))
        return ret


    @ImageFileName.setter
    def ImageFileName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().MergeImageFieldEventArgs_set_ImageFileName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().MergeImageFieldEventArgs_set_ImageFileName(self.Ptr, valuePtr)

    @property

    def ImageStream(self)->'Stream':
        """

        """
        GetDllLibDoc().MergeImageFieldEventArgs_get_ImageStream.argtypes=[c_void_p]
        GetDllLibDoc().MergeImageFieldEventArgs_get_ImageStream.restype=c_void_p
        intPtr = GetDllLibDoc().MergeImageFieldEventArgs_get_ImageStream(self.Ptr)
        ret = None if intPtr==None else Stream(intPtr)
        return ret


    @ImageStream.setter
    def ImageStream(self, value:'Stream'):
        GetDllLibDoc().MergeImageFieldEventArgs_set_ImageStream.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().MergeImageFieldEventArgs_set_ImageStream(self.Ptr, value.Ptr)

    @property

    def PictureSize(self)->'SizeF':
        """
    <summary>
        Gets or sets the size of the picture.
    </summary>
<value>The size of the picture.</value>
        """
        GetDllLibDoc().MergeImageFieldEventArgs_get_PictureSize.argtypes=[c_void_p]
        GetDllLibDoc().MergeImageFieldEventArgs_get_PictureSize.restype=c_void_p
        intPtr = GetDllLibDoc().MergeImageFieldEventArgs_get_PictureSize(self.Ptr)
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @PictureSize.setter
    def PictureSize(self, value:'SizeF'):
        GetDllLibDoc().MergeImageFieldEventArgs_set_PictureSize.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().MergeImageFieldEventArgs_set_PictureSize(self.Ptr, value.Ptr)

    @property
    def Skip(self)->bool:
        """

        """
        GetDllLibDoc().MergeImageFieldEventArgs_get_Skip.argtypes=[c_void_p]
        GetDllLibDoc().MergeImageFieldEventArgs_get_Skip.restype=c_bool
        ret = GetDllLibDoc().MergeImageFieldEventArgs_get_Skip(self.Ptr)
        return ret

    @Skip.setter
    def Skip(self, value:bool):
        GetDllLibDoc().MergeImageFieldEventArgs_set_Skip.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().MergeImageFieldEventArgs_set_Skip(self.Ptr, value)

    @dispatch

    def SetImage(self ,imgFile:str):
        """
    <summary>
        Sets the image.
    </summary>
    <param name="imgFile">The image file.</param>
        """
        imgFilePtr = StrToPtr(imgFile)
        GetDllLibDoc().MergeImageFieldEventArgs_SetImage.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().MergeImageFieldEventArgs_SetImage(self.Ptr, imgFilePtr)

    @dispatch

    def SetImage(self ,imgStream:Stream):
        """
    <summary>
        Sets the image.
    </summary>
    <param name="imgStream">The image stream.</param>
        """
        intPtrimgStream:c_void_p = imgStream.Ptr

        GetDllLibDoc().MergeImageFieldEventArgs_SetImageI.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().MergeImageFieldEventArgs_SetImageI(self.Ptr, intPtrimgStream)

