from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IStyle (abc.ABC) :
    """

    """
    @property

    @abc.abstractmethod
    def Name(self)->str:
        """

        """
        pass


    @Name.setter
    @abc.abstractmethod
    def Name(self, value:str):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def StyleId(self)->str:
        """

        """
        pass


    @property

    @abc.abstractmethod
    def GetStyleType(self)->'StyleType':
        """

        """
        pass



    @abc.abstractmethod
    def Clone(self)->'IStyle':
        """

        """
        pass


