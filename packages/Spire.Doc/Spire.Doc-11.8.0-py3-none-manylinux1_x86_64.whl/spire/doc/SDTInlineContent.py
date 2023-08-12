from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SDTInlineContent (  DocumentBase, ICompositeObject) :
    """
    <summary>
        This element specifies the last known contents of a structured document tag around one or more inline-level structures.
    </summary>
    """
    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
    <summary>
        Gets the child objects.
    </summary>
<value>The child objects.</value>
        """
        GetDllLibDoc().SDTInlineContent_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().SDTInlineContent_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().SDTInlineContent_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the entity.
    </summary>
<value>The type of the entity.</value>
        """
        GetDllLibDoc().SDTInlineContent_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().SDTInlineContent_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().SDTInlineContent_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def OwnerParagraph(self)->'Paragraph':
        """
    <summary>
        Gets the object owner paragraph.
    </summary>
        """
        GetDllLibDoc().SDTInlineContent_get_OwnerParagraph.argtypes=[c_void_p]
        GetDllLibDoc().SDTInlineContent_get_OwnerParagraph.restype=c_void_p
        intPtr = GetDllLibDoc().SDTInlineContent_get_OwnerParagraph(self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @property

    def Text(self)->str:
        """
    <summary>
         Returns or sets STD text.
    </summary>
        """
        GetDllLibDoc().SDTInlineContent_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().SDTInlineContent_get_Text.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SDTInlineContent_get_Text(self.Ptr))
        return ret



    def get_Item(self ,index:int)->'ParagraphBase':
        """
    <summary>
        Gets paragraph item by index.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().SDTInlineContent_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().SDTInlineContent_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().SDTInlineContent_get_Item(self.Ptr, index)
        ret = None if intPtr==None else ParagraphBase(intPtr)
        return ret


