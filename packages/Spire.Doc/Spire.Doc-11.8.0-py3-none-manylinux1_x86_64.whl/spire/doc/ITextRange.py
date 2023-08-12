from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ITextRange (  IParagraphBase, IDocumentObject) :
    """

    """
    @property

    @abc.abstractmethod
    def Text(self)->str:
        """

        """
        pass


    @Text.setter
    @abc.abstractmethod
    def Text(self, value:str):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def CharacterFormat(self)->'CharacterFormat':
        """

        """
        pass



    @abc.abstractmethod
    def ApplyCharacterFormat(self ,charFormat:'CharacterFormat'):
        """

        """
        pass


