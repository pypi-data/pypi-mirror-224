from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Background (  DocumentSerializable) :
    """

    """
    @property

    def Type(self)->'BackgroundType':
        """
    <summary>
        Gets or Sets the type of background for document.
    </summary>
        """
        GetDllLibDoc().Background_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().Background_get_Type.restype=c_int
        ret = GetDllLibDoc().Background_get_Type(self.Ptr)
        objwraped = BackgroundType(ret)
        return objwraped

    @Type.setter
    def Type(self, value:'BackgroundType'):
        GetDllLibDoc().Background_set_Type.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Background_set_Type(self.Ptr, value.value)

    @property

    def Color(self)->'Color':
        """
    <summary>
        Gets or sets background color.
    </summary>
        """
        GetDllLibDoc().Background_get_Color.argtypes=[c_void_p]
        GetDllLibDoc().Background_get_Color.restype=c_void_p
        intPtr = GetDllLibDoc().Background_get_Color(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @Color.setter
    def Color(self, value:'Color'):
        GetDllLibDoc().Background_set_Color.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().Background_set_Color(self.Ptr, value.Ptr)

    @property

    def Gradient(self)->'BackgroundGradient':
        """
    <summary>
        Gets or sets background gradient.
    </summary>
        """
        GetDllLibDoc().Background_get_Gradient.argtypes=[c_void_p]
        GetDllLibDoc().Background_get_Gradient.restype=c_void_p
        intPtr = GetDllLibDoc().Background_get_Gradient(self.Ptr)
        from spire.doc import BackgroundGradient
        ret = None if intPtr==None else BackgroundGradient(intPtr)
        return ret



    def GetDirectShapeAttribute(self ,key:int)->'SpireObject':
        """

        """
        
        GetDllLibDoc().Background_GetDirectShapeAttribute.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Background_GetDirectShapeAttribute.restype=c_void_p
        intPtr = GetDllLibDoc().Background_GetDirectShapeAttribute(self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret



    def GetInheritedShapeAttribute(self ,key:int)->'SpireObject':
        """

        """
        
        GetDllLibDoc().Background_GetInheritedShapeAttribute.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Background_GetInheritedShapeAttribute.restype=c_void_p
        intPtr = GetDllLibDoc().Background_GetInheritedShapeAttribute(self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret



    def GetShapeAttribute(self ,key:int)->'SpireObject':
        """

        """
        
        GetDllLibDoc().Background_GetShapeAttribute.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Background_GetShapeAttribute.restype=c_void_p
        intPtr = GetDllLibDoc().Background_GetShapeAttribute(self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret



    def SetShapeAttribute(self ,key:int,value:'SpireObject'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Background_SetShapeAttribute.argtypes=[c_void_p ,c_int,c_void_p]
        GetDllLibDoc().Background_SetShapeAttribute(self.Ptr, key,intPtrvalue)


    def SetShapeAttr(self ,key:int,value:'SpireObject'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Background_SetShapeAttr.argtypes=[c_void_p ,c_int,c_void_p]
        GetDllLibDoc().Background_SetShapeAttr(self.Ptr, key,intPtrvalue)


    def RemoveShapeAttribute(self ,key:int):
        """

        """
        
        GetDllLibDoc().Background_RemoveShapeAttribute.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Background_RemoveShapeAttribute(self.Ptr, key)


    def HasKey(self ,key:int)->bool:
        """

        """
        
        GetDllLibDoc().Background_HasKey.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Background_HasKey.restype=c_bool
        ret = GetDllLibDoc().Background_HasKey(self.Ptr, key)
        return ret

    @dispatch

    def SetPicture(self ,imgFile:str):
        """
    <summary>
        Sets the picture.
    </summary>
    <param name="imgFile">The image file.</param>
        """
        imgFilePtr = StrToPtr(imgFile)
        GetDllLibDoc().Background_SetPicture.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Background_SetPicture(self.Ptr, imgFilePtr)

    @dispatch

    def SetPicture(self ,imgStream:Stream):
        """
    <summary>
        Sets the picture.
    </summary>
    <param name="imgStream">The image stream.</param>
        """
        intPtrimgStream:c_void_p = imgStream.Ptr

        GetDllLibDoc().Background_SetPictureI.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Background_SetPictureI(self.Ptr, intPtrimgStream)

