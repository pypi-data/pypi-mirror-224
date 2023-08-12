from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ITableCollection (  IDocumentObjectCollection, ICollectionBase, IEnumerable) :
    """

    """

    @abc.abstractmethod
    def get_Item(self ,index:int)->'ITable':
        """

        """
        pass



    @abc.abstractmethod
    def Add(self ,table:'ITable')->int:
        """

        """
        pass



    @abc.abstractmethod
    def IndexOf(self ,table:'ITable')->int:
        """

        """
        pass



    @abc.abstractmethod
    def Contains(self ,table:'ITable')->bool:
        """

        """
        pass


