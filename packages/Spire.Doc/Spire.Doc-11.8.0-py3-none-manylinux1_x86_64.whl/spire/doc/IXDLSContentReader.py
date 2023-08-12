from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IXDLSContentReader (abc.ABC) :
    """

    """
    @property

    @abc.abstractmethod
    def TagName(self)->str:
        """

        """
        pass


#    @property
#
#    @abc.abstractmethod
#    def NodeType(self)->'XmlNodeType':
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def GetAttributeValue(self ,name:str)->str:
        """

        """
        pass


#
#    @abc.abstractmethod
#    def ParseElementType(self ,enumType:'Type',elementType:'Enum&')->bool:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def ReadChildElement(self ,value:SpireObject)->bool:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def ReadChildElement(self ,type:'Type')->SpireObject:
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def ReadChildStringContent(self)->str:
        """

        """
        pass


#
#    @abc.abstractmethod
#    def ReadChildBinaryElement(self)->List['Byte']:
#        """
#
#        """
#        pass
#


#    @property
#
#    @abc.abstractmethod
#    def InnerReader(self)->'XmlReader':
#        """
#
#        """
#        pass
#


    @property

    @abc.abstractmethod
    def AttributeReader(self)->'IXDLSAttributeReader':
        """

        """
        pass


