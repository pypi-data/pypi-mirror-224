from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IStructureDocument (  ICompositeObject, IDocumentObject) :
    """

    """
    @property

    @abc.abstractmethod
    def SDTProperties(self)->'SDTProperties':
        """
    <summary>
        Get the Sdt properties.
    </summary>
        """
        pass


    @property

    @abc.abstractmethod
    def BreakCharacterFormat(self)->'CharacterFormat':
        """
    <summary>
        Get the character format of the break.
    </summary>
        """
        pass


    @abc.abstractmethod
    def UpdateDataBinding(self):
        """
    <summary>
        Updates stuctured documnet tag content with bound data.
    </summary>
        """
        pass


