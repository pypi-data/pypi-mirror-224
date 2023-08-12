from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocCloneable (abc.ABC) :
    """

    """

    @abc.abstractmethod
    def Clone(self)->'SpireObject':
        """

        """
        pass


