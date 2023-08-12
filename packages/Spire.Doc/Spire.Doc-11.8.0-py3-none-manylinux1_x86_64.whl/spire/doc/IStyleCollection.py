from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IStyleCollection (  ICollectionBase, IEnumerable) :
    """

    """

    @abc.abstractmethod
    def get_Item(self ,index:int)->'IStyle':
        """

        """
        pass



    @abc.abstractmethod
    def Add(self ,style:'IStyle')->int:
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def FindByName(self ,name:str)->'Style':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def FindByName(self ,name:str,styleType:StyleType)->'IStyle':
        """

        """
        pass


