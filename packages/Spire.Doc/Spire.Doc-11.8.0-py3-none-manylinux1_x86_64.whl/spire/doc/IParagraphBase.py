from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IParagraphBase (  IDocumentObject) :
    """

    """
    @property

    @abc.abstractmethod
    def OwnerParagraph(self)->'Paragraph':
        """

        """
        pass



    @abc.abstractmethod
    def ApplyStyle(self ,styleName:str):
        """
    <summary>
        Applys the character style.
    </summary>
    <param name="styleName">the style name.</param>
        """
        pass


    @property

    @abc.abstractmethod
    def StyleName(self)->str:
        """
    <summary>
        Gets the style name.
    </summary>
        """
        pass


