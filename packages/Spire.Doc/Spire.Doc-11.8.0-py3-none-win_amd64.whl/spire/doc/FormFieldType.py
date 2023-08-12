from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FormFieldType(Enum):
    """
    <summary>
        Specifies the type of a form field.
    </summary>
    """
    TextInput = 0
    CheckBox = 1
    DropDown = 2
    Unknown = 3

