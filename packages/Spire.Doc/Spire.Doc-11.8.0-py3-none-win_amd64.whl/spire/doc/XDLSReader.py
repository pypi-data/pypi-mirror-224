from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class XDLSReader (  IXDLSAttributeReader, IXDLSContentReader) :
    """

    """

    def Deserialize(self ,value:'IDocumentSerializable'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().XDLSReader_Deserialize.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().XDLSReader_Deserialize(self.Ptr, intPtrvalue)


    def HasAttribute(self ,name:str)->bool:
        """

        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().XDLSReader_HasAttribute.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().XDLSReader_HasAttribute.restype=c_bool
        ret = GetDllLibDoc().XDLSReader_HasAttribute(self.Ptr, namePtr)
        return ret


    def ReadString(self ,name:str)->str:
        """

        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().XDLSReader_ReadString.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().XDLSReader_ReadString.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().XDLSReader_ReadString(self.Ptr, namePtr))
        return ret



    def ReadInt(self ,name:str)->int:
        """

        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().XDLSReader_ReadInt.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().XDLSReader_ReadInt.restype=c_int
        ret = GetDllLibDoc().XDLSReader_ReadInt(self.Ptr, namePtr)
        return ret


    def ReadShort(self ,name:str)->'Int16':
        """

        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().XDLSReader_ReadShort.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().XDLSReader_ReadShort.restype=c_void_p
        intPtr = GetDllLibDoc().XDLSReader_ReadShort(self.Ptr, namePtr)
        ret = None if intPtr==None else Int16(intPtr)
        return ret



    def ReadDouble(self ,name:str)->float:
        """

        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().XDLSReader_ReadDouble.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().XDLSReader_ReadDouble.restype=c_double
        ret = GetDllLibDoc().XDLSReader_ReadDouble(self.Ptr, namePtr)
        return ret


    def ReadFloat(self ,name:str)->float:
        """

        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().XDLSReader_ReadFloat.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().XDLSReader_ReadFloat.restype=c_float
        ret = GetDllLibDoc().XDLSReader_ReadFloat(self.Ptr, namePtr)
        return ret


    def ReadBoolean(self ,name:str)->bool:
        """

        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().XDLSReader_ReadBoolean.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().XDLSReader_ReadBoolean.restype=c_bool
        ret = GetDllLibDoc().XDLSReader_ReadBoolean(self.Ptr, namePtr)
        return ret


    def ReadByte(self ,name:str)->int:
        """

        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().XDLSReader_ReadByte.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().XDLSReader_ReadByte.restype=c_int
        ret = GetDllLibDoc().XDLSReader_ReadByte(self.Ptr, namePtr)
        return ret

#
#    def ReadEnum(self ,name:str,enumType:'Type')->'Enum':
#        """
#
#        """
#        intPtrenumType:c_void_p = enumType.Ptr
#
#        GetDllLibDoc().XDLSReader_ReadEnum.argtypes=[c_void_p ,c_wchar_p,c_void_p]
#        GetDllLibDoc().XDLSReader_ReadEnum.restype=c_int
#        ret = GetDllLibDoc().XDLSReader_ReadEnum(self.Ptr, name,intPtrenumType)
#        objwraped = Enum(ret)
#        return objwraped



    def ReadColor(self ,name:str)->'Color':
        """

        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().XDLSReader_ReadColor.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().XDLSReader_ReadColor.restype=c_void_p
        intPtr = GetDllLibDoc().XDLSReader_ReadColor(self.Ptr, namePtr)
        ret = None if intPtr==None else Color(intPtr)
        return ret



    def ReadDateTime(self ,name:str)->'DateTime':
        """

        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().XDLSReader_ReadDateTime.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().XDLSReader_ReadDateTime.restype=c_void_p
        intPtr = GetDllLibDoc().XDLSReader_ReadDateTime(self.Ptr, namePtr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @property

    def TagName(self)->str:
        """

        """
        GetDllLibDoc().XDLSReader_get_TagName.argtypes=[c_void_p]
        GetDllLibDoc().XDLSReader_get_TagName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().XDLSReader_get_TagName(self.Ptr))
        return ret


#    @property
#
#    def NodeType(self)->'XmlNodeType':
#        """
#
#        """
#        GetDllLibDoc().XDLSReader_get_NodeType.argtypes=[c_void_p]
#        GetDllLibDoc().XDLSReader_get_NodeType.restype=c_int
#        ret = GetDllLibDoc().XDLSReader_get_NodeType(self.Ptr)
#        objwraped = XmlNodeType(ret)
#        return objwraped



    def GetAttributeValue(self ,name:str)->str:
        """

        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().XDLSReader_GetAttributeValue.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().XDLSReader_GetAttributeValue.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().XDLSReader_GetAttributeValue(self.Ptr, namePtr))
        return ret


#
#    def ParseElementType(self ,enumType:'Type',elementType:'Enum&')->bool:
#        """
#
#        """
#        intPtrenumType:c_void_p = enumType.Ptr
#        intPtrelementType:c_void_p = elementType.Ptr
#
#        GetDllLibDoc().XDLSReader_ParseElementType.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().XDLSReader_ParseElementType.restype=c_bool
#        ret = GetDllLibDoc().XDLSReader_ParseElementType(self.Ptr, intPtrenumType,intPtrelementType)
#        return ret


    @dispatch

    def ReadChildElement(self ,value:SpireObject)->bool:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().XDLSReader_ReadChildElement.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().XDLSReader_ReadChildElement.restype=c_bool
        ret = GetDllLibDoc().XDLSReader_ReadChildElement(self.Ptr, intPtrvalue)
        return ret

#    @dispatch
#
#    def ReadChildElement(self ,type:'Type')->SpireObject:
#        """
#
#        """
#        intPtrtype:c_void_p = type.Ptr
#
#        GetDllLibDoc().XDLSReader_ReadChildElementT.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().XDLSReader_ReadChildElementT.restype=c_void_p
#        intPtr = GetDllLibDoc().XDLSReader_ReadChildElementT(self.Ptr, intPtrtype)
#        ret = None if intPtr==None else SpireObject(intPtr)
#        return ret
#



    def ReadChildStringContent(self)->str:
        """

        """
        GetDllLibDoc().XDLSReader_ReadChildStringContent.argtypes=[c_void_p]
        GetDllLibDoc().XDLSReader_ReadChildStringContent.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().XDLSReader_ReadChildStringContent(self.Ptr))
        return ret


#
#    def ReadChildBinaryElement(self)->List['Byte']:
#        """
#
#        """
#        GetDllLibDoc().XDLSReader_ReadChildBinaryElement.argtypes=[c_void_p]
#        GetDllLibDoc().XDLSReader_ReadChildBinaryElement.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().XDLSReader_ReadChildBinaryElement(self.Ptr)
#        ret = GetVectorFromArray(intPtrArray, Byte)
#        return ret


#    @property
#
#    def InnerReader(self)->'XmlReader':
#        """
#
#        """
#        GetDllLibDoc().XDLSReader_get_InnerReader.argtypes=[c_void_p]
#        GetDllLibDoc().XDLSReader_get_InnerReader.restype=c_void_p
#        intPtr = GetDllLibDoc().XDLSReader_get_InnerReader(self.Ptr)
#        ret = None if intPtr==None else XmlReader(intPtr)
#        return ret
#


    @property

    def AttributeReader(self)->'IXDLSAttributeReader':
        """

        """
        GetDllLibDoc().XDLSReader_get_AttributeReader.argtypes=[c_void_p]
        GetDllLibDoc().XDLSReader_get_AttributeReader.restype=c_void_p
        intPtr = GetDllLibDoc().XDLSReader_get_AttributeReader(self.Ptr)
        ret = None if intPtr==None else IXDLSAttributeReader(intPtr)
        return ret


