from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IField (  ITextRange, IParagraphBase, IDocumentObject) :
    """

    """
    @property

    @abc.abstractmethod
    def Type(self)->'FieldType':
        """

        """
        pass


    @Type.setter
    @abc.abstractmethod
    def Type(self, value:'FieldType'):
        """

        """
        pass


