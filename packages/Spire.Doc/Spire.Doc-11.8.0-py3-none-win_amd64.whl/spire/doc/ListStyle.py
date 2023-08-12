from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListStyle (  Style, IStyle) :
    """

    """
    @dispatch
    def __init__(self, doc:IDocument, listType:ListType):
        intPdoc:c_void_p =  doc.Ptr
        iTypelistType:c_int = listType.value

        GetDllLibDoc().ListStyle_CreateListStyleDL.argtypes=[c_void_p,c_int]
        GetDllLibDoc().ListStyle_CreateListStyleDL.restype=c_void_p
        intPtr = GetDllLibDoc().ListStyle_CreateListStyleDL(intPdoc,iTypelistType)
        super(ListStyle, self).__init__(intPtr)

    @property

    def ListType(self)->'ListType':
        """

        """
        GetDllLibDoc().ListStyle_get_ListType.argtypes=[c_void_p]
        GetDllLibDoc().ListStyle_get_ListType.restype=c_int
        ret = GetDllLibDoc().ListStyle_get_ListType(self.Ptr)
        objwraped = ListType(ret)
        return objwraped

    @ListType.setter
    def ListType(self, value:'ListType'):
        GetDllLibDoc().ListStyle_set_ListType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ListStyle_set_ListType(self.Ptr, value.value)

    @property

    def Levels(self)->'ListLevelCollection':
        """

        """
        GetDllLibDoc().ListStyle_get_Levels.argtypes=[c_void_p]
        GetDllLibDoc().ListStyle_get_Levels.restype=c_void_p
        intPtr = GetDllLibDoc().ListStyle_get_Levels(self.Ptr)
        ret = None if intPtr==None else ListLevelCollection(intPtr)
        return ret


    @property

    def StyleType(self)->'StyleType':
        """

        """
        GetDllLibDoc().ListStyle_get_StyleType.argtypes=[c_void_p]
        GetDllLibDoc().ListStyle_get_StyleType.restype=c_int
        ret = GetDllLibDoc().ListStyle_get_StyleType(self.Ptr)
        objwraped = StyleType(ret)
        return objwraped

    @staticmethod

    def CreateEmptyListStyle(doc:'IDocument',listType:'ListType',isOneLevelList:bool)->'ListStyle':
        """

        """
        intPtrdoc:c_void_p = doc.Ptr
        enumlistType:c_int = listType.value

        GetDllLibDoc().ListStyle_CreateEmptyListStyle.argtypes=[ c_void_p,c_int,c_bool]
        GetDllLibDoc().ListStyle_CreateEmptyListStyle.restype=c_void_p
        intPtr = GetDllLibDoc().ListStyle_CreateEmptyListStyle( intPtrdoc,enumlistType,isOneLevelList)
        ret = None if intPtr==None else ListStyle(intPtr)
        return ret



    def Clone(self)->'IStyle':
        """

        """
        GetDllLibDoc().ListStyle_Clone.argtypes=[c_void_p]
        GetDllLibDoc().ListStyle_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().ListStyle_Clone(self.Ptr)
        ret = None if intPtr==None else IStyle(intPtr)
        return ret



    def GetNearLevel(self ,levelNumber:int)->'ListLevel':
        """

        """
        
        GetDllLibDoc().ListStyle_GetNearLevel.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ListStyle_GetNearLevel.restype=c_void_p
        intPtr = GetDllLibDoc().ListStyle_GetNearLevel(self.Ptr, levelNumber)
        ret = None if intPtr==None else ListLevel(intPtr)
        return ret


