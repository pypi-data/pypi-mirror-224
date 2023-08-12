from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Comment (  ParagraphBase, ICompositeObject) :
    """
    <summary>
        Represents a container for text of a comment.
    </summary>
    """
    @dispatch
    def __init__(self, doc:IDocument):
		
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().Comment_CreateCommentD.argtypes=[c_void_p]
        GetDllLibDoc().Comment_CreateCommentD.restype=c_void_p
        intPtr = GetDllLibDoc().Comment_CreateCommentD(intPdoc)
        super(Comment, self).__init__(intPtr)

		
    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
    <summary>
        Gets the child document objects.
    </summary>
<value>The child entities.</value>
        """
        GetDllLibDoc().Comment_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().Comment_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().Comment_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().Comment_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Body(self)->'Body':
        """
    <summary>
        Gets comment body.
    </summary>
    <value>The text body.</value>
        """
        GetDllLibDoc().Comment_get_Body.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_Body.restype=c_void_p
        intPtr = GetDllLibDoc().Comment_get_Body(self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @property

    def Format(self)->'CommentFormat':
        """
    <summary>
        Gets the format.
    </summary>
    <value>The format.</value>
        """
        GetDllLibDoc().Comment_get_Format.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_Format.restype=c_void_p
        intPtr = GetDllLibDoc().Comment_get_Format(self.Ptr)
        from spire.doc import CommentFormat
        ret = None if intPtr==None else CommentFormat(intPtr)
        return ret


    @property

    def Items(self)->'ParagraphItemCollection':
        """
    <summary>
        Gets the range of commented items.
    </summary>
    <value>The range comment contains.</value>
        """
        GetDllLibDoc().Comment_get_Items.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_Items.restype=c_void_p
        intPtr = GetDllLibDoc().Comment_get_Items(self.Ptr)
        ret = None if intPtr==None else ParagraphItemCollection(intPtr)
        return ret


    @property

    def ReplyCommentItems(self)->'CommentsCollection':
        """
    <summary>
        Gets the range of commented items.
    </summary>
<value>The reply commented range.</value>
        """
        GetDllLibDoc().Comment_get_ReplyCommentItems.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_ReplyCommentItems.restype=c_void_p
        intPtr = GetDllLibDoc().Comment_get_ReplyCommentItems(self.Ptr)
        ret = None if intPtr==None else CommentsCollection(intPtr)
        return ret


    @property

    def ByRepliedComment(self)->'Comment':
        """
    <summary>
        Gets the comment of current comment replied.
    </summary>
<value>Comment of by reply.</value>
        """
        GetDllLibDoc().Comment_get_ByRepliedComment.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_ByRepliedComment.restype=c_void_p
        intPtr = GetDllLibDoc().Comment_get_ByRepliedComment(self.Ptr)
        ret = None if intPtr==None else Comment(intPtr)
        return ret


    @property
    def MarkDone(self)->bool:
        """
    <summary>
        Gets a value indicating whether done.
    </summary>
        """
        GetDllLibDoc().Comment_get_MarkDone.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_MarkDone.restype=c_bool
        ret = GetDllLibDoc().Comment_get_MarkDone(self.Ptr)
        return ret

    @property

    def CommentMarkStart(self)->'CommentMark':
        """
    <summary>
        Gets the begining mark of the comment.
    </summary>
<value>The commentMark of start.</value>
        """
        GetDllLibDoc().Comment_get_CommentMarkStart.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_CommentMarkStart.restype=c_void_p
        intPtr = GetDllLibDoc().Comment_get_CommentMarkStart(self.Ptr)
        ret = None if intPtr==None else CommentMark(intPtr)
        return ret


    @property

    def CommentMarkEnd(self)->'CommentMark':
        """
    <summary>
        Gets the ending mark of the comment.
    </summary>
<value>The commentMark of end.</value>
        """
        GetDllLibDoc().Comment_get_CommentMarkEnd.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_CommentMarkEnd.restype=c_void_p
        intPtr = GetDllLibDoc().Comment_get_CommentMarkEnd(self.Ptr)
        ret = None if intPtr==None else CommentMark(intPtr)
        return ret


    def Clear(self):
        """
    <summary>
        Clears the commented items.
    </summary>
        """
        GetDllLibDoc().Comment_Clear.argtypes=[c_void_p]
        GetDllLibDoc().Comment_Clear(self.Ptr)

    @dispatch

    def Replace(self ,text:str):
        """
    <summary>
        Replace commented items with matchString text.
    </summary>
    <param name="text">The text.</param>
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().Comment_Replace.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Comment_Replace(self.Ptr, textPtr)

    @dispatch

    def Replace(self ,textBodyPart:TextBodyPart):
        """
    <summary>
        Replaces the commented items with specified TextBodyPart.
    </summary>
    <param name="textBodyPart">The text body part.</param>
        """
        intPtrtextBodyPart:c_void_p = textBodyPart.Ptr

        GetDllLibDoc().Comment_ReplaceT.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Comment_ReplaceT(self.Ptr, intPtrtextBodyPart)


    def AddItem(self ,paraItem:'IParagraphBase'):
        """
    <summary>
        Adds the paragraph item to the commented items.
    </summary>
    <param name="paraItem">The paragraph item.</param>
    <returns></returns>
        """
        intPtrparaItem:c_void_p = paraItem.Ptr

        GetDllLibDoc().Comment_AddItem.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Comment_AddItem(self.Ptr, intPtrparaItem)


    def ReplyToComment(self ,replyComment:'Comment'):
        """
    <summary>
        Replies to comment.
    </summary>
    <param name="replyComment">the reply comment.</param>
        """
        intPtrreplyComment:c_void_p = replyComment.Ptr

        GetDllLibDoc().Comment_ReplyToComment.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Comment_ReplyToComment(self.Ptr, intPtrreplyComment)


    def MarkCommentDone(self ,done:bool):
        """
    <summary>
        Marks the comment done.
    </summary>
    <param name="done">the done.</param>
        """
        
        GetDllLibDoc().Comment_MarkCommentDone.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().Comment_MarkCommentDone(self.Ptr, done)

    def EnsureMinimum(self):
        """

        """
        GetDllLibDoc().Comment_EnsureMinimum.argtypes=[c_void_p]
        GetDllLibDoc().Comment_EnsureMinimum(self.Ptr)

