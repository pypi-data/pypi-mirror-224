from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CommentMark (  ParagraphBase, IDocumentObject) :
    """
    <summary>
        Represents a container for text of a comment. 
    </summary>
    <summary>
        Class represents comment start marker
    </summary>
    """
    
    @dispatch
    def __init__(self, doc:IDocument):
		
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().CommentMark_CreateCommentMarkD.argtypes=[c_void_p]
        GetDllLibDoc().CommentMark_CreateCommentMarkD.restype = c_void_p
        intPtr = GetDllLibDoc().CommentMark_CreateCommentMarkD(intPdoc)
        super(CommentMark, self).__init__(intPtr)

    @dispatch
    def __init__(self, doc:IDocument, commentMarkType:CommentMarkType):
	
        intPdoc:c_void_p =  doc.Ptr
        iTypetype:c_int = commentMarkType.value

        GetDllLibDoc().CommentMark_CreateCommentMarkDT.argtypes=[c_void_p,c_int]
        GetDllLibDoc().CommentMark_CreateCommentMarkDT.restype = c_void_p
        intPtr = GetDllLibDoc().CommentMark_CreateCommentMarkDT(intPdoc,iTypetype)
        super(CommentMark, self).__init__(intPtr)

		

    @property
    def CommentId(self)->int:
        """
    <summary>
        Gets or sets the id of the comment this mark refers to.
    </summary>
<value>The comment id.</value>
        """
        GetDllLibDoc().CommentMark_get_CommentId.argtypes=[c_void_p]
        GetDllLibDoc().CommentMark_get_CommentId.restype=c_int
        ret = GetDllLibDoc().CommentMark_get_CommentId(self.Ptr)
        return ret

    @CommentId.setter
    def CommentId(self, value:int):
        GetDllLibDoc().CommentMark_set_CommentId.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CommentMark_set_CommentId(self.Ptr, value)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().CommentMark_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().CommentMark_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().CommentMark_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Type(self)->'CommentMarkType':
        """
    <summary>
        Gets or sets the type of the CommentMark.
    </summary>
<value>The type.</value>
        """
        GetDllLibDoc().CommentMark_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().CommentMark_get_Type.restype=c_int
        ret = GetDllLibDoc().CommentMark_get_Type(self.Ptr)
        objwraped = CommentMarkType(ret)
        return objwraped

    @Type.setter
    def Type(self, value:'CommentMarkType'):
        GetDllLibDoc().CommentMark_set_Type.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CommentMark_set_Type(self.Ptr, value.value)

