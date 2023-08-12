from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IXDLSSerializableCollection (  IEnumerable) :
    """

    """

    @abc.abstractmethod
    def AddNewItem(self ,reader:'IXDLSContentReader')->'IDocumentSerializable':
        """

        """
        pass



    @abc.abstractmethod
    def CreateNewItem(self ,reader:'IXDLSContentReader')->'IDocumentSerializable':
        """

        """
        pass



    @abc.abstractmethod
    def AddItem(self ,item:'IDocumentSerializable'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def TagItemName(self)->str:
        """

        """
        pass


    @property
    @abc.abstractmethod
    def Count(self)->int:
        """

        """
        pass


