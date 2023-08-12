from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IWSectionCollection (  IDocumentObjectCollection, ICollectionBase, IEnumerable) :
    """

    """

    @abc.abstractmethod
    def get_Item(self ,index:int)->'Section':
        """

        """
        pass



    @abc.abstractmethod
    def Add(self ,section:'ISection')->int:
        """

        """
        pass



    @abc.abstractmethod
    def IndexOf(self ,section:'ISection')->int:
        """

        """
        pass


