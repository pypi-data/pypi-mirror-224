from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocPicture (  ShapeObject, IPicture) :
#class DocPicture (  ShapeObject, IDocumentObject,IPicture) :
    """

    """
    @dispatch
    def __init__(self, doc:IDocument):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().DocPicture_CreateDocPictureD.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_CreateDocPictureD.restype = c_void_p
        intPtr = GetDllLibDoc().DocPicture_CreateDocPictureD(intPdoc)
        super(DocPicture, self).__init__(intPtr)
    @property
    def Rotation(self)->float:
        """
    <summary>
        Gets/Sets the rotation of DocPicture.Specifies the rotation of the graphic frame.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_Rotation.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Rotation.restype=c_float
        ret = GetDllLibDoc().DocPicture_get_Rotation(self.Ptr)
        return ret

    @Rotation.setter
    def Rotation(self, value:float):
        GetDllLibDoc().DocPicture_set_Rotation.argtypes=[c_void_p, c_float]
        GetDllLibDoc().DocPicture_set_Rotation(self.Ptr, value)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
    <value>The type of the document object.</value>
        """
        GetDllLibDoc().DocPicture_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().DocPicture_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def Height(self)->float:
        """
    <summary>
        Returns or sets picture height.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_Height.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Height.restype=c_float
        ret = GetDllLibDoc().DocPicture_get_Height(self.Ptr)
        return ret

    @Height.setter
    def Height(self, value:float):
        GetDllLibDoc().DocPicture_set_Height.argtypes=[c_void_p, c_float]
        GetDllLibDoc().DocPicture_set_Height(self.Ptr, value)

    @property
    def Width(self)->float:
        """
    <summary>
        Returns or sets picture width.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_Width.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Width.restype=c_float
        ret = GetDllLibDoc().DocPicture_get_Width(self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:float):
        GetDllLibDoc().DocPicture_set_Width.argtypes=[c_void_p, c_float]
        GetDllLibDoc().DocPicture_set_Width(self.Ptr, value)

    @property
    def HeightScale(self)->float:
        """

        """
        GetDllLibDoc().DocPicture_get_HeightScale.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_HeightScale.restype=c_float
        ret = GetDllLibDoc().DocPicture_get_HeightScale(self.Ptr)
        return ret

    @HeightScale.setter
    def HeightScale(self, value:float):
        GetDllLibDoc().DocPicture_set_HeightScale.argtypes=[c_void_p, c_float]
        GetDllLibDoc().DocPicture_set_HeightScale(self.Ptr, value)

    @property
    def WidthScale(self)->float:
        """

        """
        GetDllLibDoc().DocPicture_get_WidthScale.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_WidthScale.restype=c_float
        ret = GetDllLibDoc().DocPicture_get_WidthScale(self.Ptr)
        return ret

    @WidthScale.setter
    def WidthScale(self, value:float):
        GetDllLibDoc().DocPicture_set_WidthScale.argtypes=[c_void_p, c_float]
        GetDllLibDoc().DocPicture_set_WidthScale(self.Ptr, value)

    @dispatch

    def SetScale(self ,scaleFactor:float):
        """
    <summary>
        Scale the image by scale factor.
    </summary>
        """
        
        GetDllLibDoc().DocPicture_SetScale.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().DocPicture_SetScale(self.Ptr, scaleFactor)

    @dispatch

    def SetScale(self ,heightFactor:float,widthFactor:float):
        """
    <summary>
        Scale the image by scale factor.
    </summary>
        """
        
        GetDllLibDoc().DocPicture_SetScaleHW.argtypes=[c_void_p ,c_float,c_float]
        GetDllLibDoc().DocPicture_SetScaleHW(self.Ptr, heightFactor,widthFactor)

    @property

    def ImageBytes(self):
        """
    <summary>
        Gets image byte array.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_ImageBytes.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_ImageBytes.restype=IntPtrArray
        intPtrArray = GetDllLibDoc().DocPicture_get_ImageBytes(self.Ptr)
        ret = GetBytesFromArray(intPtrArray)
        return ret


    @property
    def GrayScale(self)->bool:
        """

        """
        GetDllLibDoc().DocPicture_get_GrayScale.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_GrayScale.restype=c_bool
        ret = GetDllLibDoc().DocPicture_get_GrayScale(self.Ptr)
        return ret

    @GrayScale.setter
    def GrayScale(self, value:bool):
        GetDllLibDoc().DocPicture_set_GrayScale.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().DocPicture_set_GrayScale(self.Ptr, value)

    @property
    def BiLevel(self)->bool:
        """

        """
        GetDllLibDoc().DocPicture_get_BiLevel.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_BiLevel.restype=c_bool
        ret = GetDllLibDoc().DocPicture_get_BiLevel(self.Ptr)
        return ret

    @BiLevel.setter
    def BiLevel(self, value:bool):
        GetDllLibDoc().DocPicture_set_BiLevel.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().DocPicture_set_BiLevel(self.Ptr, value)

    @property
    def Brightness(self)->float:
        """

        """
        GetDllLibDoc().DocPicture_get_Brightness.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Brightness.restype=c_float
        ret = GetDllLibDoc().DocPicture_get_Brightness(self.Ptr)
        return ret

    @Brightness.setter
    def Brightness(self, value:float):
        GetDllLibDoc().DocPicture_set_Brightness.argtypes=[c_void_p, c_float]
        GetDllLibDoc().DocPicture_set_Brightness(self.Ptr, value)

    @property
    def Contrast(self)->float:
        """

        """
        GetDllLibDoc().DocPicture_get_Contrast.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Contrast.restype=c_float
        ret = GetDllLibDoc().DocPicture_get_Contrast(self.Ptr)
        return ret

    @Contrast.setter
    def Contrast(self, value:float):
        GetDllLibDoc().DocPicture_set_Contrast.argtypes=[c_void_p, c_float]
        GetDllLibDoc().DocPicture_set_Contrast(self.Ptr, value)

    @property

    def Color(self)->'PictureColor':
        """
    <summary>
        Gets or sets picture color.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_Color.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Color.restype=c_int
        ret = GetDllLibDoc().DocPicture_get_Color(self.Ptr)
        objwraped = PictureColor(ret)
        return objwraped

    @Color.setter
    def Color(self, value:'PictureColor'):
        GetDllLibDoc().DocPicture_set_Color.argtypes=[c_void_p, c_int]
        GetDllLibDoc().DocPicture_set_Color(self.Ptr, value.value)

    @property

    def TransparentColor(self)->'Color':
        """
    <summary>
        Gets or sets transparent color
    </summary>
        """
        GetDllLibDoc().DocPicture_get_TransparentColor.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_TransparentColor.restype=c_void_p
        intPtr = GetDllLibDoc().DocPicture_get_TransparentColor(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @TransparentColor.setter
    def TransparentColor(self, value:'Color'):
        GetDllLibDoc().DocPicture_set_TransparentColor.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().DocPicture_set_TransparentColor(self.Ptr, value.Ptr)

    @property
    def IsCrop(self)->bool:
        """
    <summary>
        Gets whether the picture object is cropped.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_IsCrop.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_IsCrop.restype=c_bool
        ret = GetDllLibDoc().DocPicture_get_IsCrop(self.Ptr)
        return ret

    @property

    def HorizontalOrigin(self)->'HorizontalOrigin':
        """
    <summary>
        Gets or sets horizontal origin of the picture.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_HorizontalOrigin.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_HorizontalOrigin.restype=c_int
        ret = GetDllLibDoc().DocPicture_get_HorizontalOrigin(self.Ptr)
        objwraped = HorizontalOrigin(ret)
        return objwraped

    @HorizontalOrigin.setter
    def HorizontalOrigin(self, value:'HorizontalOrigin'):
        GetDllLibDoc().DocPicture_set_HorizontalOrigin.argtypes=[c_void_p, c_int]
        GetDllLibDoc().DocPicture_set_HorizontalOrigin(self.Ptr, value.value)

    @property

    def VerticalOrigin(self)->'VerticalOrigin':
        """
    <summary>
        Gets or sets absolute horizontal position of the picture.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_VerticalOrigin.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_VerticalOrigin.restype=c_int
        ret = GetDllLibDoc().DocPicture_get_VerticalOrigin(self.Ptr)
        objwraped = VerticalOrigin(ret)
        return objwraped

    @VerticalOrigin.setter
    def VerticalOrigin(self, value:'VerticalOrigin'):
        GetDllLibDoc().DocPicture_set_VerticalOrigin.argtypes=[c_void_p, c_int]
        GetDllLibDoc().DocPicture_set_VerticalOrigin(self.Ptr, value.value)

    @property
    def HorizontalPosition(self)->float:
        """
    <summary>
        Gets or sets absolute horizontal position of the picture.
    </summary>
<remarks>
            The value is measured in points and the position is relative to HorizontalOrigin.
            </remarks>
        """
        GetDllLibDoc().DocPicture_get_HorizontalPosition.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_HorizontalPosition.restype=c_float
        ret = GetDllLibDoc().DocPicture_get_HorizontalPosition(self.Ptr)
        return ret

    @HorizontalPosition.setter
    def HorizontalPosition(self, value:float):
        GetDllLibDoc().DocPicture_set_HorizontalPosition.argtypes=[c_void_p, c_float]
        GetDllLibDoc().DocPicture_set_HorizontalPosition(self.Ptr, value)

    @property
    def VerticalPosition(self)->float:
        """
    <summary>
        Gets or sets absolute vertical position of the picture.
    </summary>
<remarks>
            The value is measured in points and the position is relative to VerticalOrigin.
            </remarks>
        """
        GetDllLibDoc().DocPicture_get_VerticalPosition.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_VerticalPosition.restype=c_float
        ret = GetDllLibDoc().DocPicture_get_VerticalPosition(self.Ptr)
        return ret

    @VerticalPosition.setter
    def VerticalPosition(self, value:float):
        GetDllLibDoc().DocPicture_set_VerticalPosition.argtypes=[c_void_p, c_float]
        GetDllLibDoc().DocPicture_set_VerticalPosition(self.Ptr, value)

    @property

    def TextWrappingStyle(self)->'TextWrappingStyle':
        """
    <summary>
        Gets or sets text wrapping style of the picture.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_TextWrappingStyle.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_TextWrappingStyle.restype=c_int
        ret = GetDllLibDoc().DocPicture_get_TextWrappingStyle(self.Ptr)
        objwraped = TextWrappingStyle(ret)
        return objwraped

    @TextWrappingStyle.setter
    def TextWrappingStyle(self, value:'TextWrappingStyle'):
        GetDllLibDoc().DocPicture_set_TextWrappingStyle.argtypes=[c_void_p, c_int]
        GetDllLibDoc().DocPicture_set_TextWrappingStyle(self.Ptr, value.value)

    @property

    def TextWrappingType(self)->'TextWrappingType':
        """
    <summary>
        Gets or sets text wrapping type of the picture.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_TextWrappingType.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_TextWrappingType.restype=c_int
        ret = GetDllLibDoc().DocPicture_get_TextWrappingType(self.Ptr)
        objwraped = TextWrappingType(ret)
        return objwraped

    @TextWrappingType.setter
    def TextWrappingType(self, value:'TextWrappingType'):
        GetDllLibDoc().DocPicture_set_TextWrappingType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().DocPicture_set_TextWrappingType(self.Ptr, value.value)

    @property

    def HorizontalAlignment(self)->'ShapeHorizontalAlignment':
        """
    <summary>
        Returns or setspicture horizontal alignment.
    </summary>
    <remarks>
            If it is set as None, then the picture is explicitly positioned using position properties.
            Otherwise it is positioned according to the alignment specified. The position of the object is relative to HorizontalOrigin.
    </remarks>
        """
        GetDllLibDoc().DocPicture_get_HorizontalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_HorizontalAlignment.restype=c_int
        ret = GetDllLibDoc().DocPicture_get_HorizontalAlignment(self.Ptr)
        objwraped = ShapeHorizontalAlignment(ret)
        return objwraped

    @HorizontalAlignment.setter
    def HorizontalAlignment(self, value:'ShapeHorizontalAlignment'):
        GetDllLibDoc().DocPicture_set_HorizontalAlignment.argtypes=[c_void_p, c_int]
        GetDllLibDoc().DocPicture_set_HorizontalAlignment(self.Ptr, value.value)

    @property

    def VerticalAlignment(self)->'ShapeVerticalAlignment':
        """
    <summary>
        Returns or setspicture vertical alignment.
    </summary>
    <remarks>
            If it is set as None, then the picture is explicitly positioned using position properties. 
            Otherwise it is positioned according to the alignment specified. The position of the object is relative to VerticalOrigin.
    </remarks>
        """
        GetDllLibDoc().DocPicture_get_VerticalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_VerticalAlignment.restype=c_int
        ret = GetDllLibDoc().DocPicture_get_VerticalAlignment(self.Ptr)
        objwraped = ShapeVerticalAlignment(ret)
        return objwraped

    @VerticalAlignment.setter
    def VerticalAlignment(self, value:'ShapeVerticalAlignment'):
        GetDllLibDoc().DocPicture_set_VerticalAlignment.argtypes=[c_void_p, c_int]
        GetDllLibDoc().DocPicture_set_VerticalAlignment(self.Ptr, value.value)

    @property
    def IsUnderText(self)->bool:
        """
    <summary>
        Gets or sets whether picture is below image.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_IsUnderText.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_IsUnderText.restype=c_bool
        ret = GetDllLibDoc().DocPicture_get_IsUnderText(self.Ptr)
        return ret

    @IsUnderText.setter
    def IsUnderText(self, value:bool):
        GetDllLibDoc().DocPicture_set_IsUnderText.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().DocPicture_set_IsUnderText(self.Ptr, value)

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
    <summary>
        Gets shape object's character format.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_CharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().DocPicture_get_CharacterFormat(self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def Title(self)->str:
        """
    <summary>
        Gets the picture title.
    </summary>
    <value>The title.</value>
        """
        GetDllLibDoc().DocPicture_get_Title.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Title.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().DocPicture_get_Title(self.Ptr))
        return ret


    @Title.setter
    def Title(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().DocPicture_set_Title.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().DocPicture_set_Title(self.Ptr, valuePtr)

    @property
    def LayoutInCell(self)->bool:
        """
    <summary>
        Gets or sets the boolean value that represents whether a picture in a table is displayed inside or outside the table.
    </summary>
        """
        GetDllLibDoc().DocPicture_get_LayoutInCell.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_LayoutInCell.restype=c_bool
        ret = GetDllLibDoc().DocPicture_get_LayoutInCell(self.Ptr)
        return ret

    @LayoutInCell.setter
    def LayoutInCell(self, value:bool):
        GetDllLibDoc().DocPicture_set_LayoutInCell.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().DocPicture_set_LayoutInCell(self.Ptr, value)

    @dispatch

    def LoadImage(self ,imgFile:str):
        """
    <summary>
        Loads the image.
    </summary>
    <param name="imgFile">The img file.</param>
        """
        imgFilePtr = StrToPtr(imgFile)
        GetDllLibDoc().DocPicture_LoadImageI.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().DocPicture_LoadImageI(self.Ptr, imgFilePtr)

    @dispatch

    def LoadImage(self ,imgStream:Stream):
        """
    <summary>
        Loads the image.
    </summary>
    <param name="imgStream">The img stream.</param>
        """
        intPtrimgStream:c_void_p = imgStream.Ptr

        GetDllLibDoc().DocPicture_LoadImageI1.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().DocPicture_LoadImageI1(self.Ptr, intPtrimgStream)

    @dispatch

    def LoadImage(self ,imageBytes:bytes):
        """
    <summary>
        Loads image as bytes array.
    </summary>
    <param name="imageBytes"></param>
        """
        #arrayimageBytes:ArrayTypeimageBytes = ""
        list_address:c_void_p = cast((c_ubyte * len(imageBytes)).from_buffer_copy(imageBytes),c_void_p)
        length:c_int = len(imageBytes)

        GetDllLibDoc().DocPicture_LoadImageI11.argtypes=[c_void_p ,c_void_p,c_int]
        GetDllLibDoc().DocPicture_LoadImageI11(self.Ptr,list_address, length)



    def ReplaceImage(self ,imageBytes:bytes,bIsKeepRation:bool):
        """
    <summary>
        Replaces the image.
    </summary>
    <param name="imageBytes">The image bytes.</param>
    <param name="bIsKeepRation"></param>
        """
        #arrayimageBytes:ArrayTypeimageBytes = ""
        list_address:c_void_p = cast((c_ubyte * len(imageBytes)).from_buffer_copy(imageBytes),c_void_p)
        length:c_int = len(imageBytes)

        GetDllLibDoc().DocPicture_ReplaceImage.argtypes=[c_void_p ,c_void_p,c_int,c_bool]
        GetDllLibDoc().DocPicture_ReplaceImage(self.Ptr, list_address,length,bIsKeepRation)



    def AddCaption(self ,name:str,numberingFormat:'CaptionNumberingFormat',captionPosition:'CaptionPosition')->'IParagraph':
        """
    <summary>
        Add Caption for current Picture
    </summary>
    <param name="captionPosition"></param>
    <param name="name"></param>
    <param name="format"></param>
    <returns></returns>
        """
        namePtr = StrToPtr(name)
        enumformat:c_int = numberingFormat.value
        enumcaptionPosition:c_int = captionPosition.value

        GetDllLibDoc().DocPicture_AddCaption.argtypes=[c_void_p ,c_char_p,c_int,c_int]
        GetDllLibDoc().DocPicture_AddCaption.restype=c_void_p
        intPtr = GetDllLibDoc().DocPicture_AddCaption(self.Ptr, namePtr,enumformat,enumcaptionPosition)
        #ret = None if intPtr==None else IParagraph(intPtr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


