from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ITextBoxItemCollection (abc.ABC) :
    """

    """

    @abc.abstractmethod
    def get_Item(self ,index:int)->'ITextBox':
        """

        """
        pass



    @abc.abstractmethod
    def Add(self ,textBox:'ITextBox')->int:
        """

        """
        pass


