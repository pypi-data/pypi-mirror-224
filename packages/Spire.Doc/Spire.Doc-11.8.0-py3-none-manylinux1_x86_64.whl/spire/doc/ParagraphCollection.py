from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ParagraphCollection (  DocumentSubsetCollection, IParagraphCollection) :
    """

    """

    def get_Item(self ,index:int)->'Paragraph':
        """

        """
        
        GetDllLibDoc().ParagraphCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ParagraphCollection_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphCollection_get_Item(self.Ptr, index)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret



    def Add(self ,paragraph:'IParagraph')->int:
        """
    <summary>
        Adds a paragraph to end of text body.
    </summary>
    <param name="paragraph">The paragraph.</param>
    <returns></returns>
        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().ParagraphCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ParagraphCollection_Add.restype=c_int
        ret = GetDllLibDoc().ParagraphCollection_Add(self.Ptr, intPtrparagraph)
        return ret


    def Contains(self ,paragraph:'IParagraph')->bool:
        """
    <summary>
        Determines whether the <see cref="!:Spire.Doc.IParagraphCollection" /> contains a specific value.
    </summary>
    <param name="paragraph">The paragraph.</param>
    <returns>
            	If paragraph is found, set to <c>true</c>.
            </returns>
        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().ParagraphCollection_Contains.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ParagraphCollection_Contains.restype=c_bool
        ret = GetDllLibDoc().ParagraphCollection_Contains(self.Ptr, intPtrparagraph)
        return ret


    def Insert(self ,index:int,paragraph:'IParagraph'):
        """
    <summary>
        Inserts a paragraph into collection at the specified index.
    </summary>
    <param name="index">The index.</param>
    <param name="paragraph">The paragraph.</param>
        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().ParagraphCollection_Insert.argtypes=[c_void_p ,c_int,c_void_p]
        GetDllLibDoc().ParagraphCollection_Insert(self.Ptr, index,intPtrparagraph)


    def IndexOf(self ,paragraph:'IParagraph')->int:
        """
    <summary>
        Returns the zero-based index of the specified paragraph.
    </summary>
    <param name="paragraph">The paragraph.</param>
    <returns></returns>
        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().ParagraphCollection_IndexOf.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ParagraphCollection_IndexOf.restype=c_int
        ret = GetDllLibDoc().ParagraphCollection_IndexOf(self.Ptr, intPtrparagraph)
        return ret


    def Remove(self ,paragraph:'IParagraph'):
        """
    <summary>
        Removes the specified paragraph.
    </summary>
    <param name="paragraph">The paragraph.</param>
        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().ParagraphCollection_Remove.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ParagraphCollection_Remove(self.Ptr, intPtrparagraph)


    def RemoveAt(self ,index:int):
        """
    <summary>
        Removes the paragraph at the specified index from the collection.
    </summary>
    <param name="index">The index.</param>
        """
        
        GetDllLibDoc().ParagraphCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ParagraphCollection_RemoveAt(self.Ptr, index)

