from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocumentSerializable (abc.ABC) :
    """

    """

    @abc.abstractmethod
    def WriteXmlAttributes(self ,writer:'IXDLSAttributeWriter'):
        """

        """
        pass



    @abc.abstractmethod
    def WriteXmlContent(self ,writer:'IXDLSContentWriter'):
        """

        """
        pass



    @abc.abstractmethod
    def ReadXmlAttributes(self ,reader:'IXDLSAttributeReader'):
        """

        """
        pass



    @abc.abstractmethod
    def ReadXmlContent(self ,reader:'IXDLSContentReader')->bool:
        """

        """
        pass


    @property

    @abc.abstractmethod
    def XDLSHolder(self)->'XDLSHolder':
        """

        """
        pass



    @abc.abstractmethod
    def RestoreReference(self ,name:str,value:int):
        """

        """
        pass


