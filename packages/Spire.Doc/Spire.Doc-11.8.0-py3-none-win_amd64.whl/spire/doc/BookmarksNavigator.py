from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BookmarksNavigator (SpireObject) :
    """

    """
    @dispatch
    def __init__(self, doc:IDocument):
        intPdoc:c_void_p = doc.Ptr;

        GetDllLibDoc().BookmarksNavigator_CreateBookmarksNavigatorD.argtypes = [c_void_p]
        GetDllLibDoc().BookmarksNavigator_CreateBookmarksNavigatorD.restype = c_void_p
        intPtr = GetDllLibDoc().BookmarksNavigator_CreateBookmarksNavigatorD(intPdoc)
        super(BookmarksNavigator, self).__init__(intPtr)

    @property

    def Document(self)->'IDocument':
        """

        """
        GetDllLibDoc().BookmarksNavigator_get_Document.argtypes=[c_void_p]
        GetDllLibDoc().BookmarksNavigator_get_Document.restype=c_void_p
        intPtr = GetDllLibDoc().BookmarksNavigator_get_Document(self.Ptr)
        ret = None if intPtr==None else IDocument(intPtr)
        return ret


    @Document.setter
    def Document(self, value:'IDocument'):
        GetDllLibDoc().BookmarksNavigator_set_Document.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().BookmarksNavigator_set_Document(self.Ptr, value.Ptr)

    @property

    def CurrentBookmark(self)->'Bookmark':
        """

        """
        GetDllLibDoc().BookmarksNavigator_get_CurrentBookmark.argtypes=[c_void_p]
        GetDllLibDoc().BookmarksNavigator_get_CurrentBookmark.restype=c_void_p
        intPtr = GetDllLibDoc().BookmarksNavigator_get_CurrentBookmark(self.Ptr)
        ret = None if intPtr==None else Bookmark(intPtr)
        return ret


    @dispatch

    def MoveToBookmark(self ,bookmarkName:str):
        """

        """
        bookmarkNamePtr = StrToPtr(bookmarkName)
        GetDllLibDoc().BookmarksNavigator_MoveToBookmark.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().BookmarksNavigator_MoveToBookmark(self.Ptr, bookmarkNamePtr)

    @dispatch

    def MoveToBookmark(self ,bookmarkName:str,isStart:bool,isAfter:bool):
        """

        """
        bookmarkNamePtr = StrToPtr(bookmarkName)
        GetDllLibDoc().BookmarksNavigator_MoveToBookmarkBII.argtypes=[c_void_p ,c_char_p,c_bool,c_bool]
        GetDllLibDoc().BookmarksNavigator_MoveToBookmarkBII(self.Ptr, bookmarkNamePtr,isStart,isAfter)

    @dispatch

    def InsertText(self ,text:str)->'ITextRange':
        """

        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().BookmarksNavigator_InsertText.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().BookmarksNavigator_InsertText.restype=c_void_p
        intPtr = GetDllLibDoc().BookmarksNavigator_InsertText(self.Ptr, textPtr)
        ret = None if intPtr==None else ITextRange(intPtr)
        return ret


    @dispatch

    def InsertText(self ,text:str,saveFormatting:bool)->'ITextRange':
        """

        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().BookmarksNavigator_InsertTextTS.argtypes=[c_void_p ,c_char_p,c_bool]
        GetDllLibDoc().BookmarksNavigator_InsertTextTS.restype=c_void_p
        intPtr = GetDllLibDoc().BookmarksNavigator_InsertTextTS(self.Ptr, textPtr,saveFormatting)
        ret = None if intPtr==None else ITextRange(intPtr)
        return ret



    def InsertTable(self ,table:'ITable'):
        """

        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().BookmarksNavigator_InsertTable.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().BookmarksNavigator_InsertTable(self.Ptr, intPtrtable)


    def InsertParagraphItem(self ,itemType:'ParagraphItemType')->'IParagraphBase':
        """

        """
        enumitemType:c_int = itemType.value

        GetDllLibDoc().BookmarksNavigator_InsertParagraphItem.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().BookmarksNavigator_InsertParagraphItem.restype=c_void_p
        intPtr = GetDllLibDoc().BookmarksNavigator_InsertParagraphItem(self.Ptr, enumitemType)
        ret = None if intPtr==None else IParagraphBase(intPtr)
        return ret



    def InsertParagraph(self ,paragraph:'IParagraph'):
        """

        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().BookmarksNavigator_InsertParagraph.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().BookmarksNavigator_InsertParagraph(self.Ptr, intPtrparagraph)


    def InsertTextBodyPart(self ,bodyPart:'TextBodyPart'):
        """

        """
        intPtrbodyPart:c_void_p = bodyPart.Ptr

        GetDllLibDoc().BookmarksNavigator_InsertTextBodyPart.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().BookmarksNavigator_InsertTextBodyPart(self.Ptr, intPtrbodyPart)


    def GetBookmarkContent(self)->'TextBodyPart':
        """

        """
        GetDllLibDoc().BookmarksNavigator_GetBookmarkContent.argtypes=[c_void_p]
        GetDllLibDoc().BookmarksNavigator_GetBookmarkContent.restype=c_void_p
        intPtr = GetDllLibDoc().BookmarksNavigator_GetBookmarkContent(self.Ptr)
        ret = None if intPtr==None else TextBodyPart(intPtr)
        return ret



    def DeleteBookmarkContent(self ,saveFormatting:bool):
        """

        """
        
        GetDllLibDoc().BookmarksNavigator_DeleteBookmarkContent.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().BookmarksNavigator_DeleteBookmarkContent(self.Ptr, saveFormatting)

    @dispatch

    def ReplaceBookmarkContent(self ,bodyPart:TextBodyPart):
        """

        """
        intPtrbodyPart:c_void_p = bodyPart.Ptr

        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContent.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContent(self.Ptr, intPtrbodyPart)

    @dispatch

    def ReplaceBookmarkContent(self ,bodyPart:TextBodyPart,isKeepSourceFirstParaFormat:bool):
        """

        """
        intPtrbodyPart:c_void_p = bodyPart.Ptr

        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentBI.argtypes=[c_void_p ,c_void_p,c_bool]
        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentBI(self.Ptr, intPtrbodyPart,isKeepSourceFirstParaFormat)

    @dispatch

    def ReplaceBookmarkContent(self ,bodyPart:TextBodyPart,isKeepSourceFirstParaFormat:bool,saveFormatting:bool):
        """

        """
        intPtrbodyPart:c_void_p = bodyPart.Ptr

        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentBIS.argtypes=[c_void_p ,c_void_p,c_bool,c_bool]
        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentBIS(self.Ptr, intPtrbodyPart,isKeepSourceFirstParaFormat,saveFormatting)

    @dispatch

    def ReplaceBookmarkContent(self ,text:str,saveFormatting:bool):
        """

        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentTS.argtypes=[c_void_p ,c_char_p,c_bool]
        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentTS(self.Ptr, textPtr,saveFormatting)

