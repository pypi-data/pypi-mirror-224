from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IParagraph (  IBodyRegion, IStyleHolder, ICompositeObject) :
    """

    """
    @property

    @abc.abstractmethod
    def Text(self)->str:
        """

        """
        pass


    @Text.setter
    @abc.abstractmethod
    def Text(self, value:str):
        """

        """
        pass



    @abc.abstractmethod
    def get_Item(self ,index:int)->'ParagraphBase':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Items(self)->'ParagraphItemCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Format(self)->'ParagraphFormat':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def ListFormat(self)->'ListFormat':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def BreakCharacterFormat(self)->'CharacterFormat':
        """

        """
        pass


    @property
    @abc.abstractmethod
    def IsInCell(self)->bool:
        """

        """
        pass


    @property
    @abc.abstractmethod
    def IsEndOfSection(self)->bool:
        """

        """
        pass


    @property
    @abc.abstractmethod
    def IsEndOfDocument(self)->bool:
        """

        """
        pass



    @abc.abstractmethod
    def AppendText(self ,text:str)->'TextRange':
        """

        """
        pass


#
#    @abc.abstractmethod
#    def AppendPicture(self ,imageBytes:'Byte[]')->'DocPicture':
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def AppendField(self ,fieldName:str,fieldType:'FieldType')->'Field':
        """

        """
        pass



    @abc.abstractmethod
    def AppendBookmarkStart(self ,name:str)->'BookmarkStart':
        """

        """
        pass



    @abc.abstractmethod
    def AppendBookmarkEnd(self ,name:str)->'BookmarkEnd':
        """

        """
        pass



    @abc.abstractmethod
    def AppendComment(self ,text:str)->'Comment':
        """

        """
        pass



    @abc.abstractmethod
    def AppendFootnote(self ,type:'FootnoteType')->'Footnote':
        """

        """
        pass



    @abc.abstractmethod
    def AppendTextBox(self ,width:float,height:float)->'TextBox':
        """

        """
        pass



    @abc.abstractmethod
    def AppendSymbol(self ,characterCode:int)->'Symbol':
        """

        """
        pass



    @abc.abstractmethod
    def AppendBreak(self ,breakType:'BreakType')->'Break':
        """

        """
        pass



    @abc.abstractmethod
    def AppendHTML(self ,html:str):
        """

        """
        pass



    @abc.abstractmethod
    def GetStyle(self)->'ParagraphStyle':
        """

        """
        pass



    @abc.abstractmethod
    def Replace(self ,given:str,textSelection:'TextSelection',caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendCheckBox(self)->'CheckBoxFormField':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendTextFormField(self ,defaultText:str)->'TextFormField':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendDropDownFormField(self)->'DropDownFormField':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendCheckBox(self ,checkBoxName:str,defaultCheckBoxValue:bool)->'CheckBoxFormField':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendTextFormField(self ,formFieldName:str,defaultText:str)->'TextFormField':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendDropDownFormField(self ,dropDropDownName:str)->'DropDownFormField':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendHyperlink(self ,link:str,text:str,type:HyperlinkType)->'Field':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendHyperlink(self ,link:str,picture:'DocPicture',type:HyperlinkType)->'Field':
        """

        """
        pass


    @abc.abstractmethod
    def RemoveAbsPosition(self):
        """

        """
        pass



    @abc.abstractmethod
    def AppendTOC(self ,lowerHeadingLevel:int,upperHeadingLevel:int)->'TableOfContent':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendOleObject(self ,oleStream:Stream,olePicture:'DocPicture',type:OleObjectType)->'DocOleObject':
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,type:OleObjectType)->DocOleObject:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def AppendOleObject(self ,pathToFile:str,olePicture:'DocPicture',type:OleObjectType)->'DocOleObject':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendOleObject(self ,pathToFile:str,olePicture:'DocPicture')->'DocOleObject':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendOleObject(self ,stream:Stream,pic:'DocPicture',oleLinkType:OleLinkType)->'DocOleObject':
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,oleLinkType:OleLinkType)->DocOleObject:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,fileExtension:str)->DocOleObject:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def AppendOleObject(self ,oleStream:Stream,olePicture:'DocPicture',fileExtension:str)->'DocOleObject':
        """

        """
        pass


