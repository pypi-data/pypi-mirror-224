from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ITextBox (  IParagraphBase, ICompositeObject) :
    """

    """
    @property

    @abc.abstractmethod
    def Body(self)->'Body':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Format(self)->'TextBoxFormat':
        """

        """
        pass


