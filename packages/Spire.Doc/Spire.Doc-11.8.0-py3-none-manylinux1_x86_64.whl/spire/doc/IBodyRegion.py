from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IBodyRegion (  IDocumentObject) :
    """

    """
#    @dispatch
#
#    @abc.abstractmethod
#    def Replace(self ,pattern:'Regex',replace:str)->int:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def Replace(self ,given:str,replace:str,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def Replace(self ,pattern:'Regex',textSelection:TextSelection)->int:
#        """
#
#        """
#        pass
#


