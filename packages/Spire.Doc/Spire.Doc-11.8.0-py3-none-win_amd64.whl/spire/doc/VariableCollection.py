from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class VariableCollection (  IEnumerable) :
    """

    """

    def get_Item(self ,name:str)->str:
        """
    <summary>
        Gets or sets the variable with the specified name.
    </summary>
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().VariableCollection_get_Item.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().VariableCollection_get_Item.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().VariableCollection_get_Item(self.Ptr, namePtr))
        return ret



    def set_Item(self ,name:str,value:str):
        """

        """
        namePtr = StrToPtr(name)
        valuePtr = StrToPtr(value)
        GetDllLibDoc().VariableCollection_set_Item.argtypes=[c_void_p ,c_char_p,c_char_p]
        GetDllLibDoc().VariableCollection_set_Item(self.Ptr, namePtr,valuePtr)

    @property
    def Count(self)->int:
        """
    <summary>
        Gets the count of variables.
    </summary>
        """
        GetDllLibDoc().VariableCollection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().VariableCollection_get_Count.restype=c_int
        ret = GetDllLibDoc().VariableCollection_get_Count(self.Ptr)
        return ret


    def Add(self ,name:str,value:str):
        """
    <summary>
        Adds variable to document.
    </summary>
    <param name="name">The name.</param>
    <param name="value">The value.</param>
        """
        namePtr = StrToPtr(name)
        valuePtr = StrToPtr(value)
        GetDllLibDoc().VariableCollection_Add.argtypes=[c_void_p ,c_char_p,c_char_p]
        GetDllLibDoc().VariableCollection_Add(self.Ptr, namePtr,valuePtr)


    def GetNameByIndex(self ,index:int)->str:
        """
    <summary>
        Gets variable's key by the index.
    </summary>
    <param name="index">The index.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().VariableCollection_GetNameByIndex.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().VariableCollection_GetNameByIndex.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().VariableCollection_GetNameByIndex(self.Ptr, index))
        return ret



    def GetValueByIndex(self ,index:int)->str:
        """
    <summary>
        Gets variable's value by the index.
    </summary>
    <param name="index">The index.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().VariableCollection_GetValueByIndex.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().VariableCollection_GetValueByIndex.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().VariableCollection_GetValueByIndex(self.Ptr, index))
        return ret



    def Remove(self ,name:str):
        """
    <summary>
        Removes document variable with specified name from the document.
    </summary>
    <param name="name">The name.</param>
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().VariableCollection_Remove.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().VariableCollection_Remove(self.Ptr, namePtr)


    def GetEnumerator(self)->'IEnumerator':
        """

        """
        GetDllLibDoc().VariableCollection_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().VariableCollection_GetEnumerator.restype=c_void_p
        intPtr = GetDllLibDoc().VariableCollection_GetEnumerator(self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret


