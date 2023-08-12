from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class StyleCollection (  DocumentSerializableCollection, IStyleCollection) :
    """

    """

    def get_Item(self ,index:int)->'IStyle':
        """
    <summary>
        Gets the at the specified index.
    </summary>
<value></value>
    <returns></returns>
        """
        
        GetDllLibDoc().StyleCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().StyleCollection_get_Item.restype=IntPtrWithTypeName
        intPtr = GetDllLibDoc().StyleCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else self._create(intPtr)
        return ret

    def _create(self, intPtrWithTypeName:IntPtrWithTypeName)->IStyle:
        ret= None
        if intPtrWithTypeName == None:
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName =="Spire.Doc.Documents.ListStyle"):
            ret = ListStyle(intPtr)
        elif (strName =="Spire.Doc.Documents.ParagraphStyle"):
            ret = ParagraphStyle(intPtr)
        else:
            ret = Style(intPtr)
        return ret


    def Add(self ,style:'IStyle')->int:
        """
    <summary>
        Adds Style to collection 
    </summary>
    <param name="style">The style.</param>
    <returns></returns>
        """
        intPtrstyle:c_void_p = style.Ptr

        GetDllLibDoc().StyleCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().StyleCollection_Add.restype=c_int
        ret = GetDllLibDoc().StyleCollection_Add(self.Ptr, intPtrstyle)
        return ret

    def ApplyDocDefaultsToNormalStyle(self):
        """
    <summary>
        Applys the document default paragraph format and character format to normal style. 
    </summary>
        """
        GetDllLibDoc().StyleCollection_ApplyDocDefaultsToNormalStyle.argtypes=[c_void_p]
        GetDllLibDoc().StyleCollection_ApplyDocDefaultsToNormalStyle(self.Ptr)

    @dispatch

    def FindByName(self ,name:str)->Style:
        """
    <summary>
        Finds Style by name
    </summary>
    <param name="name">The name.</param>
    <returns></returns>
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().StyleCollection_FindByName.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().StyleCollection_FindByName.restype=c_void_p
        intPtr = GetDllLibDoc().StyleCollection_FindByName(self.Ptr, namePtr)
        ret = None if intPtr==None else Style(intPtr)
        return ret


    @dispatch

    def FindByName(self ,name:str,styleType:StyleType)->IStyle:
        """
    <summary>
        Finds Style by name
    </summary>
    <param name="name">The name.</param>
    <param name="styleType">Type of the style.</param>
    <returns></returns>
        """
        namePtr = StrToPtr(name)
        enumstyleType:c_int = styleType.value

        GetDllLibDoc().StyleCollection_FindByNameNS.argtypes=[c_void_p ,c_char_p,c_int]
        GetDllLibDoc().StyleCollection_FindByNameNS.restype=c_void_p
        intPtr = GetDllLibDoc().StyleCollection_FindByNameNS(self.Ptr, namePtr,enumstyleType)
        ret = None if intPtr==None else IStyle(intPtr)
        return ret



    def FindById(self ,styleId:int)->'IStyle':
        """
    <summary>
        Finds Style by id
    </summary>
    <param name="styleId">The style id.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().StyleCollection_FindById.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().StyleCollection_FindById.restype=c_void_p
        intPtr = GetDllLibDoc().StyleCollection_FindById(self.Ptr, styleId)
        ret = None if intPtr==None else IStyle(intPtr)
        return ret



    def FindByIstd(self ,istd:int)->'IStyle':
        """
    <summary>
        Finds Style by istd.
    </summary>
    <param name="istd">The style istd.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().StyleCollection_FindByIstd.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().StyleCollection_FindByIstd.restype=c_void_p
        intPtr = GetDllLibDoc().StyleCollection_FindByIstd(self.Ptr, istd)
        ret = None if intPtr==None else IStyle(intPtr)
        return ret



    def FindByIdentifier(self ,sIdentifier:int)->'IStyle':
        """
    <summary>
        Finds Style by identifier
    </summary>
    <param name="sIdentifier">The style identifier.
            The parameter value is the <see cref="T:Spire.Doc.Documents.BuiltinStyle" /> enumeration value 
            or the <see cref="T:Spire.Doc.Documents.DefaultTableStyle" /> enumeration value.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().StyleCollection_FindByIdentifier.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().StyleCollection_FindByIdentifier.restype=c_void_p
        intPtr = GetDllLibDoc().StyleCollection_FindByIdentifier(self.Ptr, sIdentifier)
        ret = None if intPtr==None else IStyle(intPtr)
        return ret


