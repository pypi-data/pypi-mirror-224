from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TabCollection (  DocumentSerializableCollection) :
    """
    <summary>
        Represents a collection of <see cref="T:Spire.Doc.Tab" /> objects 
            for paragraph or paragraph format.
    </summary>
    """

    def get_Item(self ,index:int)->'Tab':
        """
    <summary>
        Gets the <see cref="T:Spire.Doc.Tab" /> at the specified index.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().TabCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TabCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().TabCollection_get_Item(self.Ptr, index)
        ret = None if intPtr==None else Tab(intPtr)
        return ret


    @dispatch

    def AddTab(self)->Tab:
        """

        """
        GetDllLibDoc().TabCollection_AddTab.argtypes=[c_void_p]
        GetDllLibDoc().TabCollection_AddTab.restype=c_void_p
        intPtr = GetDllLibDoc().TabCollection_AddTab(self.Ptr)
        ret = None if intPtr==None else Tab(intPtr)
        return ret


    @dispatch

    def AddTab(self ,position:float,justification:TabJustification,leader:TabLeader)->Tab:
        """

        """
        enumjustification:c_int = justification.value
        enumleader:c_int = leader.value

        GetDllLibDoc().TabCollection_AddTabPJL.argtypes=[c_void_p ,c_float,c_int,c_int]
        GetDllLibDoc().TabCollection_AddTabPJL.restype=c_void_p
        intPtr = GetDllLibDoc().TabCollection_AddTabPJL(self.Ptr, position,enumjustification,enumleader)
        ret = None if intPtr==None else Tab(intPtr)
        return ret


    @dispatch

    def AddTab(self ,position:float)->Tab:
        """
    <summary>
        Adds the tab.
    </summary>
    <param name="position">The position.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().TabCollection_AddTabP.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().TabCollection_AddTabP.restype=c_void_p
        intPtr = GetDllLibDoc().TabCollection_AddTabP(self.Ptr, position)
        ret = None if intPtr==None else Tab(intPtr)
        return ret


    def Clear(self):
        """
    <summary>
        Removes all the tabs from the tab collection.
    </summary>
        """
        GetDllLibDoc().TabCollection_Clear.argtypes=[c_void_p]
        GetDllLibDoc().TabCollection_Clear(self.Ptr)


    def RemoveAt(self ,index:int):
        """
    <summary>
        Removes the tab at the specified index from the tab collection
    </summary>
    <param name="index"></param>
        """
        
        GetDllLibDoc().TabCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TabCollection_RemoveAt(self.Ptr, index)

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        GetDllLibDoc().TabCollection_Equals.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TabCollection_Equals.restype=c_bool
        ret = GetDllLibDoc().TabCollection_Equals(self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,other:'TabCollection')->bool:
        """

        """
        intPtrother:c_void_p = other.Ptr

        GetDllLibDoc().TabCollection_EqualsO.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TabCollection_EqualsO.restype=c_bool
        ret = GetDllLibDoc().TabCollection_EqualsO(self.Ptr, intPtrother)
        return ret

