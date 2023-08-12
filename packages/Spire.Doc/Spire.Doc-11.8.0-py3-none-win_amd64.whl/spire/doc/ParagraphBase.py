from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ParagraphBase (  DocumentBase, IParagraphBase) :
    """

    """
    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
    <summary>
        Gets the child objects of the entity.
    </summary>
        """
        GetDllLibDoc().ParagraphBase_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphBase_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphBase_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def OwnerParagraph(self)->'Paragraph':
        """
    <summary>
        Gets owner paragraph.
    </summary>
    <value></value>
        """
        GetDllLibDoc().ParagraphBase_get_OwnerParagraph.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphBase_get_OwnerParagraph.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphBase_get_OwnerParagraph(self.Ptr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @property
    def IsInsertRevision(self)->bool:
        """
    <summary>
        Gets a value indicating whether this item was inserted to the document,
        when "Track Changes" is or was set to "true".
    </summary>
    <value>
        if this instance was inserted, set to <c>true</c>.
    </value>
        """
        GetDllLibDoc().ParagraphBase_get_IsInsertRevision.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphBase_get_IsInsertRevision.restype=c_bool
        ret = GetDllLibDoc().ParagraphBase_get_IsInsertRevision(self.Ptr)
        return ret

    @property
    def IsDeleteRevision(self)->bool:
        """
    <summary>
        Gets or set a value indicating whether this item was deleted from the document,
            when "Track Changes" is or was set to "true".
    </summary>
<value>
            	if this instance is delete revision, set to <c>true</c>.
            </value>
        """
        GetDllLibDoc().ParagraphBase_get_IsDeleteRevision.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphBase_get_IsDeleteRevision.restype=c_bool
        ret = GetDllLibDoc().ParagraphBase_get_IsDeleteRevision(self.Ptr)
        return ret

    @property

    def DeleteRevision(self)->'EditRevision':
        """
    <summary>
        Gets the delete revision for this objects.
            Note this can be null. If null does not have delete revision.
    </summary>
        """
        GetDllLibDoc().ParagraphBase_get_DeleteRevision.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphBase_get_DeleteRevision.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphBase_get_DeleteRevision(self.Ptr)
        from spire.doc import EditRevision
        ret = None if intPtr==None else EditRevision(intPtr)
        return ret


    @property

    def InsertRevision(self)->'EditRevision':
        """
    <summary>
        Gets the insert revision for this objects.
            Note this can be null. If null does not have insert revision.
    </summary>
        """
        GetDllLibDoc().ParagraphBase_get_InsertRevision.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphBase_get_InsertRevision.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphBase_get_InsertRevision(self.Ptr)
        from spire.doc import EditRevision
        ret = None if intPtr==None else EditRevision(intPtr)
        return ret


    @property

    def StyleName(self)->str:
        """
    <summary>
        Gets the style name.
    </summary>
        """
        GetDllLibDoc().ParagraphBase_get_StyleName.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphBase_get_StyleName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().ParagraphBase_get_StyleName(self.Ptr))
        return ret


    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
    <summary>
        Gets the character format.
    </summary>
<value>The paragraph item character format.</value>
        """
        GetDllLibDoc().ParagraphBase_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphBase_get_CharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphBase_get_CharacterFormat(self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret



    def ApplyCharacterFormat(self ,charFormat:'CharacterFormat'):
        """
    <summary>
        Sets the character format.
    </summary>
    <param name="charFormat">The character format.</param>
        """
        intPtrcharFormat:c_void_p = charFormat.Ptr

        GetDllLibDoc().ParagraphBase_ApplyCharacterFormat.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ParagraphBase_ApplyCharacterFormat(self.Ptr, intPtrcharFormat)


    def ApplyStyle(self ,styleName:str):
        """

        """
        styleNamePtr = StrToPtr(styleName)
        GetDllLibDoc().ParagraphBase_ApplyStyle.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().ParagraphBase_ApplyStyle(self.Ptr, styleNamePtr)


    def GetPreviousWidgetSibling(self)->'IDocumentObject':
        """

        """
        GetDllLibDoc().ParagraphBase_GetPreviousWidgetSibling.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphBase_GetPreviousWidgetSibling.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphBase_GetPreviousWidgetSibling(self.Ptr)
        ret = None if intPtr==None else IDocumentObject(intPtr)
        return ret



    def GetNextWidgetSibling(self)->'IDocumentObject':
        """

        """
        GetDllLibDoc().ParagraphBase_GetNextWidgetSibling.argtypes=[c_void_p]
        GetDllLibDoc().ParagraphBase_GetNextWidgetSibling.restype=c_void_p
        intPtr = GetDllLibDoc().ParagraphBase_GetNextWidgetSibling(self.Ptr)
        ret = None if intPtr==None else IDocumentObject(intPtr)
        return ret


