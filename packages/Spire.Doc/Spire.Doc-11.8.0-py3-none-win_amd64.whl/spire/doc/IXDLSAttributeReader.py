from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IXDLSAttributeReader (abc.ABC) :
    """

    """

    @abc.abstractmethod
    def HasAttribute(self ,name:str)->bool:
        """

        """
        pass



    @abc.abstractmethod
    def ReadString(self ,name:str)->str:
        """

        """
        pass



    @abc.abstractmethod
    def ReadInt(self ,name:str)->int:
        """

        """
        pass



    @abc.abstractmethod
    def ReadShort(self ,name:str)->'Int16':
        """

        """
        pass



    @abc.abstractmethod
    def ReadFloat(self ,name:str)->float:
        """

        """
        pass



    @abc.abstractmethod
    def ReadDouble(self ,name:str)->float:
        """

        """
        pass



    @abc.abstractmethod
    def ReadBoolean(self ,name:str)->bool:
        """

        """
        pass



    @abc.abstractmethod
    def ReadByte(self ,name:str)->int:
        """

        """
        pass


#
#    @abc.abstractmethod
#    def ReadEnum(self ,name:str,enumType:'Type')->'Enum':
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def ReadColor(self ,name:str)->'Color':
        """

        """
        pass



    @abc.abstractmethod
    def ReadDateTime(self ,s:str)->'DateTime':
        """

        """
        pass


