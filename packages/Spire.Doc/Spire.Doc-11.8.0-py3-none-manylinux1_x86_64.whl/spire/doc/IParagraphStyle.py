from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IParagraphStyle (  IStyle) :
    """

    """
    @property

    @abc.abstractmethod
    def ParagraphFormat(self)->'ParagraphFormat':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def CharacterFormat(self)->'CharacterFormat':
        """

        """
        pass


