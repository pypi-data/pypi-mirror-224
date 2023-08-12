from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IMergeField (  IField, ITextRange, IParagraphBase, IDocumentObject) :
    """

    """
    @property

    @abc.abstractmethod
    def FieldName(self)->str:
        """

        """
        pass


    @FieldName.setter
    @abc.abstractmethod
    def FieldName(self, value:str):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def TextBefore(self)->str:
        """

        """
        pass


    @TextBefore.setter
    @abc.abstractmethod
    def TextBefore(self, value:str):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def TextAfter(self)->str:
        """

        """
        pass


    @TextAfter.setter
    @abc.abstractmethod
    def TextAfter(self, value:str):
        """

        """
        pass


