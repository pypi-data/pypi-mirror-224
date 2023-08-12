from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocumentObject (abc.ABC) :
    """

    """
    @property

    @abc.abstractmethod
    def Document(self)->'Document':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Owner(self)->'DocumentObject':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def DocumentObjectType(self)->'DocumentObjectType':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def NextSibling(self)->'IDocumentObject':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def PreviousSibling(self)->'IDocumentObject':
        """

        """
        pass


    @property
    @abc.abstractmethod
    def IsComposite(self)->bool:
        """

        """
        pass



    @abc.abstractmethod
    def Clone(self)->'DocumentObject':
        """

        """
        pass



    @abc.abstractmethod
    def GetNextWidgetSibling(self)->'IDocumentObject':
        """

        """
        pass



    @abc.abstractmethod
    def GetPreviousWidgetSibling(self)->'IDocumentObject':
        """

        """
        pass


