from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IFieldsEventArgs (abc.ABC) :
    """
    <summary>
        Interface IFieldsEventArgs
    </summary>
    """
    @property

    @abc.abstractmethod
    def Field(self)->'Field':
        """
    <summary>
        Gets the field.
    </summary>
        """
        pass


