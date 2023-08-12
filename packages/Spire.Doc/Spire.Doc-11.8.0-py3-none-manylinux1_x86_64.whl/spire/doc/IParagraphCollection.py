from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IParagraphCollection (  IDocumentObjectCollection, ICollectionBase, IEnumerable) :
    """

    """

    @abc.abstractmethod
    def get_Item(self ,index:int)->'Paragraph':
        """

        """
        pass



    @abc.abstractmethod
    def Add(self ,paragraph:'IParagraph')->int:
        """

        """
        pass



    @abc.abstractmethod
    def Insert(self ,index:int,paragraph:'IParagraph'):
        """

        """
        pass



    @abc.abstractmethod
    def IndexOf(self ,paragraph:'IParagraph')->int:
        """

        """
        pass



    @abc.abstractmethod
    def RemoveAt(self ,index:int):
        """

        """
        pass


