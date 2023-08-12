from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IXDLSContentWriter (abc.ABC) :
    """

    """
#
#    @abc.abstractmethod
#    def WriteChildBinaryElement(self ,name:str,value:'Byte[]'):
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def WriteChildStringElement(self ,name:str,value:str):
        """

        """
        pass



    @abc.abstractmethod
    def WriteChildElement(self ,name:str,value:'SpireObject'):
        """

        """
        pass



    @abc.abstractmethod
    def WriteChildRefElement(self ,name:str,refToElement:int):
        """

        """
        pass


#    @property
#
#    @abc.abstractmethod
#    def InnerWriter(self)->'XmlWriter':
#        """
#
#        """
#        pass
#


