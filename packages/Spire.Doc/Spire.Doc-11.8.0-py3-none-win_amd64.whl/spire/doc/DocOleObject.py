from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocOleObject (  ShapeObject, IDocumentObject) :
    """

    """
    @property
    def DisplayAsIcon(self)->bool:
        """
    <summary>
        Gets or sets whether the OLEObject is displayed as an Icon or Content. If True, the OLEObject is displayed as an icon
    </summary>
<value>bool</value>
        """
        GetDllLibDoc().DocOleObject_get_DisplayAsIcon.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_DisplayAsIcon.restype=c_bool
        ret = GetDllLibDoc().DocOleObject_get_DisplayAsIcon(self.Ptr)
        return ret

    @DisplayAsIcon.setter
    def DisplayAsIcon(self, value:bool):
        GetDllLibDoc().DocOleObject_set_DisplayAsIcon.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().DocOleObject_set_DisplayAsIcon(self.Ptr, value)

    @property

    def OlePicture(self)->'DocPicture':
        """
    <summary>
        Gets the OLE picture.
    </summary>
<value>The OLE picture.</value>
        """
        GetDllLibDoc().DocOleObject_get_OlePicture.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_OlePicture.restype=c_void_p
        intPtr = GetDllLibDoc().DocOleObject_get_OlePicture(self.Ptr)
        ret = None if intPtr==None else DocPicture(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().DocOleObject_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().DocOleObject_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Container(self)->'Stream':
        """
    <summary>
        Gets the OLE container.
    </summary>
<value>The container.</value>
        """
        GetDllLibDoc().DocOleObject_get_Container.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_Container.restype=c_void_p
        intPtr = GetDllLibDoc().DocOleObject_get_Container(self.Ptr)
        ret = None if intPtr==None else Stream(intPtr)
        return ret


    @property

    def CharacterFormat(self)->'CharacterFormat':
        """

        """
        GetDllLibDoc().DocOleObject_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_CharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().DocOleObject_get_CharacterFormat(self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def OleStorageName(self)->str:
        """
    <summary>
        Gets or sets the name of the OLE Object storage.
    </summary>
<value>The name of the OLE storage.</value>
        """
        GetDllLibDoc().DocOleObject_get_OleStorageName.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_OleStorageName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().DocOleObject_get_OleStorageName(self.Ptr))
        return ret


    @OleStorageName.setter
    def OleStorageName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().DocOleObject_set_OleStorageName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().DocOleObject_set_OleStorageName(self.Ptr, valuePtr)

    @property

    def LinkPath(self)->str:
        """
    <summary>
        Gets or sets the link path.
    </summary>
<value>The link address.</value>
        """
        GetDllLibDoc().DocOleObject_get_LinkPath.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_LinkPath.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().DocOleObject_get_LinkPath(self.Ptr))
        return ret


    @LinkPath.setter
    def LinkPath(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().DocOleObject_set_LinkPath.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().DocOleObject_set_LinkPath(self.Ptr, valuePtr)

    @property

    def LinkType(self)->'OleLinkType':
        """
    <summary>
        Gets the type of the OLE object.
    </summary>
<value>The type of the OLE obj.</value>
        """
        GetDllLibDoc().DocOleObject_get_LinkType.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_LinkType.restype=c_int
        ret = GetDllLibDoc().DocOleObject_get_LinkType(self.Ptr)
        objwraped = OleLinkType(ret)
        return objwraped

    @property

    def ProgId(self)->str:
        """
    <summary>
        Gets the programmatic identifier of the OLE object of an undefined type.
    </summary>
        """
        GetDllLibDoc().DocOleObject_get_ProgId.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_ProgId.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().DocOleObject_get_ProgId(self.Ptr))
        return ret


    @property

    def ObjectType(self)->str:
        """
    <summary>
        Gets or sets the type of the OLE object.
    </summary>
<value>The type of the object.</value>
        """
        GetDllLibDoc().DocOleObject_get_ObjectType.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_ObjectType.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().DocOleObject_get_ObjectType(self.Ptr))
        return ret


    @ObjectType.setter
    def ObjectType(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().DocOleObject_set_ObjectType.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().DocOleObject_set_ObjectType(self.Ptr, valuePtr)

    @property

    def NativeData(self):
        """
    <summary>
        Gets the native data of embedded OLE object.
    </summary>
    <value>The native data.</value>
        """
        GetDllLibDoc().DocOleObject_get_NativeData.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_NativeData.restype=IntPtrArray
        intPtrArray = GetDllLibDoc().DocOleObject_get_NativeData(self.Ptr)
        ret = GetBytesFromArray(intPtrArray)
        return ret


    @property

    def PackageFileName(self)->str:
        """
    <summary>
        Gets the name of file embedded in the package (only if OleType is "Package").
    </summary>
        """
        GetDllLibDoc().DocOleObject_get_PackageFileName.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_PackageFileName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().DocOleObject_get_PackageFileName(self.Ptr))
        return ret


#
#    def SetNativeData(self ,nativeData:'Byte[]'):
#        """
#    <summary>
#        Sets the native data.
#    </summary>
#    <param name="nativeData">The native data.</param>
#        """
#        #arraynativeData:ArrayTypenativeData = ""
#        countnativeData = len(nativeData)
#        ArrayTypenativeData = c_void_p * countnativeData
#        arraynativeData = ArrayTypenativeData()
#        for i in range(0, countnativeData):
#            arraynativeData[i] = nativeData[i].Ptr
#
#
#        GetDllLibDoc().DocOleObject_SetNativeData.argtypes=[c_void_p ,ArrayTypenativeData]
#        GetDllLibDoc().DocOleObject_SetNativeData(self.Ptr, arraynativeData)



    def SetOlePicture(self ,picture:'DocPicture'):
        """
    <summary>
        Sets the OLE picture.
    </summary>
    <param name="picture">The picture.</param>
        """
        intPtrpicture:c_void_p = picture.Ptr

        GetDllLibDoc().DocOleObject_SetOlePicture.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().DocOleObject_SetOlePicture(self.Ptr, intPtrpicture)

