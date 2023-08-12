from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
from decimal import Decimal,getcontext
import abc

class SDTProperties (  DocumentSerializable) :
    """

    """
    @property

    def Id(self)->float:
        """
    <summary>
        Gets the id. specifes that the contents of this attribute contains a decimal number.
    </summary>
        """
        GetDllLibDoc().SDTProperties_get_Id.argtypes=[c_void_p]
        GetDllLibDoc().SDTProperties_get_Id.restype=c_double
        intPtr = GetDllLibDoc().SDTProperties_get_Id(self.Ptr)
        return intPtr



    @Id.setter
    def Id(self, value:float):
        GetDllLibDoc().SDTProperties_set_Id.argtypes=[c_void_p, c_double]
        GetDllLibDoc().SDTProperties_set_Id(self.Ptr, value)


    @property

    def Alias(self)->str:
        """
    <summary>
        Gets or sets the an alias.
    </summary>
        """
        GetDllLibDoc().SDTProperties_get_Alias.argtypes=[c_void_p]
        GetDllLibDoc().SDTProperties_get_Alias.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SDTProperties_get_Alias(self.Ptr))
        return ret


    @Alias.setter
    def Alias(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SDTProperties_set_Alias.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SDTProperties_set_Alias(self.Ptr, valuePtr)

    @property

    def Tag(self)->str:
        """
    <summary>
        Gets or sets the a value specifies that its contents contain a string.
    </summary>
        """
        GetDllLibDoc().SDTProperties_get_Tag.argtypes=[c_void_p]
        GetDllLibDoc().SDTProperties_get_Tag.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SDTProperties_get_Tag(self.Ptr))
        return ret


    @Tag.setter
    def Tag(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SDTProperties_set_Tag.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SDTProperties_set_Tag(self.Ptr, valuePtr)

    @property

    def ControlProperties(self)->'SdtControlProperties':
        """

        """
        GetDllLibDoc().SDTProperties_get_ControlProperties.argtypes=[c_void_p]
        GetDllLibDoc().SDTProperties_get_ControlProperties.restype=IntPtrWithTypeName
        intPtr = GetDllLibDoc().SDTProperties_get_ControlProperties(self.Ptr)
        ret = None if intPtr==None else self._createSdtControlProperties(intPtr)
        return ret

    def _createSdtControlProperties(self, intPtrWithTypeName:IntPtrWithTypeName)->'SdtControlProperties':
        ret= None
        if intPtrWithTypeName == None :
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Documents.SdtBuildingBlockGallery"):
            from spire.doc import SdtBuildingBlockGallery
            ret = SdtBuildingBlockGallery(intPtr)
        elif (strName == "Spire.Doc.Documents.SdtCheckBox"):
            from spire.doc import SdtCheckBox
            ret = SdtCheckBox(intPtr)
        elif (strName == "Spire.Doc.Documents.SdtCitation"):
            from spire.doc import SdtCitation
            ret = SdtCitation(intPtr)
        elif (strName == "Spire.Doc.Documents.SdtComboBox"):
            from spire.doc import SdtComboBox
            ret = SdtComboBox(intPtr)
        elif (strName == "Spire.Doc.Documents.SdtDate"):
            from spire.doc import SdtDate
            ret = SdtDate(intPtr)
        elif (strName == "Spire.Doc.Documents.SdtDropDownList"):
            from spire.doc import SdtDropDownList
            ret = SdtDropDownList(intPtr)
        elif (strName == "Spire.Doc.Documents.SdtPicture"):
            from spire.doc import SdtPicture
            ret = SdtPicture(intPtr)
        else:
            ret = SdtControlProperties(intPtr)

        return ret

    @ControlProperties.setter
    def ControlProperties(self, value:'SdtControlProperties'):
        GetDllLibDoc().SDTProperties_set_ControlProperties.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().SDTProperties_set_ControlProperties(self.Ptr, value.Ptr)

    @property

    def SDTType(self)->'SdtType':
        """

        """
        GetDllLibDoc().SDTProperties_get_SDTType.argtypes=[c_void_p]
        GetDllLibDoc().SDTProperties_get_SDTType.restype=c_int
        ret = GetDllLibDoc().SDTProperties_get_SDTType(self.Ptr)
        objwraped = SdtType(ret)
        return objwraped

    @SDTType.setter
    def SDTType(self, value:'SdtType'):
        GetDllLibDoc().SDTProperties_set_SDTType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().SDTProperties_set_SDTType(self.Ptr, value.value)

    @property

    def LockSettings(self)->'LockSettingsType':
        """
    <summary>
        Gets or sets a value that specifies locking behaviors
    </summary>
        """
        GetDllLibDoc().SDTProperties_get_LockSettings.argtypes=[c_void_p]
        GetDllLibDoc().SDTProperties_get_LockSettings.restype=c_int
        ret = GetDllLibDoc().SDTProperties_get_LockSettings(self.Ptr)
        objwraped = LockSettingsType(ret)
        return objwraped

    @LockSettings.setter
    def LockSettings(self, value:'LockSettingsType'):
        GetDllLibDoc().SDTProperties_set_LockSettings.argtypes=[c_void_p, c_int]
        GetDllLibDoc().SDTProperties_set_LockSettings(self.Ptr, value.value)

    @property
    def IsShowingPlaceHolder(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether this instance is showing place holder.
    </summary>
        """
        GetDllLibDoc().SDTProperties_get_IsShowingPlaceHolder.argtypes=[c_void_p]
        GetDllLibDoc().SDTProperties_get_IsShowingPlaceHolder.restype=c_bool
        ret = GetDllLibDoc().SDTProperties_get_IsShowingPlaceHolder(self.Ptr)
        return ret

    @IsShowingPlaceHolder.setter
    def IsShowingPlaceHolder(self, value:bool):
        GetDllLibDoc().SDTProperties_set_IsShowingPlaceHolder.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().SDTProperties_set_IsShowingPlaceHolder(self.Ptr, value)

    @property
    def IsTemporary(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether remove SDT when contents are edited.
    </summary>
        """
        GetDllLibDoc().SDTProperties_get_IsTemporary.argtypes=[c_void_p]
        GetDllLibDoc().SDTProperties_get_IsTemporary.restype=c_bool
        ret = GetDllLibDoc().SDTProperties_get_IsTemporary(self.Ptr)
        return ret

    @IsTemporary.setter
    def IsTemporary(self, value:bool):
        GetDllLibDoc().SDTProperties_set_IsTemporary.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().SDTProperties_set_IsTemporary(self.Ptr, value)

    @property

    def Appearance(self)->'SdtAppearance':
        """
    <summary>
        Gets or sets a value for the border appearance type.
    </summary>
        """
        GetDllLibDoc().SDTProperties_get_Appearance.argtypes=[c_void_p]
        GetDllLibDoc().SDTProperties_get_Appearance.restype=c_int
        ret = GetDllLibDoc().SDTProperties_get_Appearance(self.Ptr)
        objwraped = SdtAppearance(ret)
        return objwraped

    @Appearance.setter
    def Appearance(self, value:'SdtAppearance'):
        GetDllLibDoc().SDTProperties_set_Appearance.argtypes=[c_void_p, c_int]
        GetDllLibDoc().SDTProperties_set_Appearance(self.Ptr, value.value)

