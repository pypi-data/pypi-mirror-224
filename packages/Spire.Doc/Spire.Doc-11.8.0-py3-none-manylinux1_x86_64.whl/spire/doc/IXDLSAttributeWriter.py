from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IXDLSAttributeWriter (abc.ABC) :
    """

    """
    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:float):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:float):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:int):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:str):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:Enum):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:bool):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:Color):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:DateTime):
        """

        """
        pass


