from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IStyleHolder (abc.ABC) :
    """

    """
    @property

    @abc.abstractmethod
    def StyleName(self)->str:
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ApplyStyle(self ,styleName:str):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ApplyStyle(self ,builtinStyle:BuiltinStyle):
        """

        """
        pass


