from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBodyPart (SpireObject) :
    """

    """
    @dispatch
    def __init__(self, textBodySelection:TextBodySelection):
        intPtextBodySelection:c_void_p = textBodySelection.Ptr

        GetDllLibDoc().TextBodyPart_CreateTextBodyPartTextBody.argtypes = [c_void_p]
        GetDllLibDoc().TextBodyPart_CreateTextBodyPartTextBody.restype = c_void_p
        intPtr = GetDllLibDoc().TextBodyPart_CreateTextBodyPartTextBody(intPtextBodySelection)
        super(TextBodyPart, self).__init__(intPtr)

    @dispatch
    def __init__(self, textSelection:TextSelection):
        intPtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().TextBodyPart_CreateTextBodyPartT.argtypes = [c_void_p]
        GetDllLibDoc().TextBodyPart_CreateTextBodyPartT.restype = c_void_p
        intPtr = GetDllLibDoc().TextBodyPart_CreateTextBodyPartT(intPtextSelection)
        super(TextBodyPart, self).__init__(intPtr)
    @dispatch
    def __init__(self, doc:'Document'):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().TextBodyPart_CreateTextBodyPartD.argtypes=[c_void_p]
        GetDllLibDoc().TextBodyPart_CreateTextBodyPartD.restype=c_void_p
        intPtr = GetDllLibDoc().TextBodyPart_CreateTextBodyPartD(intPdoc)
        super(TextBodyPart, self).__init__(intPtr)

    @property

    def BodyItems(self)->'BodyRegionCollection':
        """

        """
        GetDllLibDoc().TextBodyPart_get_BodyItems.argtypes=[c_void_p]
        GetDllLibDoc().TextBodyPart_get_BodyItems.restype=c_void_p
        intPtr = GetDllLibDoc().TextBodyPart_get_BodyItems(self.Ptr)
        ret = None if intPtr==None else BodyRegionCollection(intPtr)
        return ret


    def Clear(self):
        """

        """
        GetDllLibDoc().TextBodyPart_Clear.argtypes=[c_void_p]
        GetDllLibDoc().TextBodyPart_Clear(self.Ptr)

    @dispatch

    def Copy(self ,textSel:TextSelection):
        """

        """
        intPtrtextSel:c_void_p = textSel.Ptr

        GetDllLibDoc().TextBodyPart_Copy.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TextBodyPart_Copy(self.Ptr, intPtrtextSel)

    @dispatch

    def Copy(self ,textSel:TextBodySelection):
        """

        """
        intPtrtextSel:c_void_p = textSel.Ptr

        GetDllLibDoc().TextBodyPart_CopyT.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TextBodyPart_CopyT(self.Ptr, intPtrtextSel)

    @dispatch

    def Copy(self ,bodyItem:BodyRegion,clone:bool):
        """

        """
        intPtrbodyItem:c_void_p = bodyItem.Ptr

        GetDllLibDoc().TextBodyPart_CopyBC.argtypes=[c_void_p ,c_void_p,c_bool]
        GetDllLibDoc().TextBodyPart_CopyBC(self.Ptr, intPtrbodyItem,clone)

    @dispatch

    def Copy(self ,pItem:ParagraphBase,clone:bool):
        """

        """
        intPtrpItem:c_void_p = pItem.Ptr

        GetDllLibDoc().TextBodyPart_CopyPC.argtypes=[c_void_p ,c_void_p,c_bool]
        GetDllLibDoc().TextBodyPart_CopyPC(self.Ptr, intPtrpItem,clone)

    @dispatch

    def PasteAfter(self ,bodyItem:BodyRegion):
        """

        """
        intPtrbodyItem:c_void_p = bodyItem.Ptr

        GetDllLibDoc().TextBodyPart_PasteAfter.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TextBodyPart_PasteAfter(self.Ptr, intPtrbodyItem)

    @dispatch

    def PasteAfter(self ,paragraphItem:ParagraphBase):
        """

        """
        intPtrparagraphItem:c_void_p = paragraphItem.Ptr

        GetDllLibDoc().TextBodyPart_PasteAfterP.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TextBodyPart_PasteAfterP(self.Ptr, intPtrparagraphItem)

    @dispatch

    def PasteAt(self ,textBody:IBody,itemIndex:int):
        """

        """
        intPtrtextBody:c_void_p = textBody.Ptr

        GetDllLibDoc().TextBodyPart_PasteAt.argtypes=[c_void_p ,c_void_p,c_int]
        GetDllLibDoc().TextBodyPart_PasteAt(self.Ptr, intPtrtextBody,itemIndex)

    @dispatch

    def PasteAt(self ,textBody:IBody,itemIndex:int,pItemIndex:int):
        """

        """
        intPtrtextBody:c_void_p = textBody.Ptr

        GetDllLibDoc().TextBodyPart_PasteAtTIP.argtypes=[c_void_p ,c_void_p,c_int,c_int]
        GetDllLibDoc().TextBodyPart_PasteAtTIP(self.Ptr, intPtrtextBody,itemIndex,pItemIndex)


    def PasteAtEnd(self ,textBody:'IBody'):
        """

        """
        intPtrtextBody:c_void_p = textBody.Ptr

        GetDllLibDoc().TextBodyPart_PasteAtEnd.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TextBodyPart_PasteAtEnd(self.Ptr, intPtrtextBody)

