from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ImageType(Enum):
    """
    <summary>
        Specifies the image type.
    </summary>
    """
    Bitmap = 0
    Metafile = 1

