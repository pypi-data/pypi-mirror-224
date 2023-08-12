from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocument (  ICompositeObject, IDocumentObject) :
    """

    """
    @property

    @abc.abstractmethod
    def BuiltinDocumentProperties(self)->'BuiltinDocumentProperties':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def CustomDocumentProperties(self)->'CustomDocumentProperties':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Sections(self)->'SectionCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Styles(self)->'StyleCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def ListStyles(self)->'ListStyleCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Bookmarks(self)->'BookmarkCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def TextBoxes(self)->'TextBoxCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def TOC(self)->'TableOfContent':
        """

        """
        pass


    @TOC.setter
    @abc.abstractmethod
    def TOC(self, value:'TableOfContent'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Comments(self)->'CommentsCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def LastSection(self)->'Section':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def LastParagraph(self)->'Paragraph':
        """

        """
        pass


    @abc.abstractmethod
    def GetProtectionType(self)->'ProtectionType':
        """

        """
        pass


    @abc.abstractmethod
    def SetProtectionType(self, value:'ProtectionType'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def ViewSetup(self)->'ViewSetup':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Watermark(self)->'WatermarkBase':
        """

        """
        pass


    @Watermark.setter
    @abc.abstractmethod
    def Watermark(self, value:'WatermarkBase'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def MailMerge(self)->'MailMerge':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Background(self)->'Background':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Variables(self)->'VariableCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Properties(self)->'DocumentProperties':
        """

        """
        pass


    @property
    @abc.abstractmethod
    def HasChanges(self)->bool:
        """

        """
        pass


    @property
    @abc.abstractmethod
    def IsUpdateFields(self)->bool:
        """

        """
        pass


    @IsUpdateFields.setter
    @abc.abstractmethod
    def IsUpdateFields(self, value:bool):
        """

        """
        pass


    @abc.abstractmethod
    def CreateMinialDocument(self):
        """

        """
        pass



    @abc.abstractmethod
    def AddSection(self)->'Section':
        """

        """
        pass



    @abc.abstractmethod
    def AddParagraphStyle(self ,styleName:str)->'ParagraphStyle':
        """

        """
        pass



    @abc.abstractmethod
    def AddListStyle(self ,listType:'ListType',styleName:str)->'ListStyle':
        """

        """
        pass



    @abc.abstractmethod
    def GetText(self)->str:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def SaveToImages(self ,type:ImageType)->List[SKImage]:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def SaveToImages(self ,pageIndex:int,type:ImageType)->SKImage:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def SaveToImages(self ,pageIndex:int,noOfPages:int,type:ImageType)->List[SKImage]:
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def CreateParagraph(self)->'Paragraph':
        """

        """
        pass



    @abc.abstractmethod
    def Clone(self)->'Document':
        """

        """
        pass



    @abc.abstractmethod
    def AddStyle(self ,builtinStyle:'BuiltinStyle')->'Style':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def Protect(self ,type:ProtectionType):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def Protect(self ,type:ProtectionType,password:str):
        """

        """
        pass



    @abc.abstractmethod
    def Encrypt(self ,password:str):
        """

        """
        pass


    @abc.abstractmethod
    def RemoveEncryption(self):
        """

        """
        pass


    @abc.abstractmethod
    def UpdateWordCount(self):
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def FindPattern(self ,pattern:'Regex')->TextSelection:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def FindString(self ,given:str,caseSensitive:bool,wholeWord:bool)->TextSelection:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def FindPatternInLine(self ,pattern:'Regex')->List[TextSelection]:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def FindStringInLine(self ,given:str,caseSensitive:bool,wholeWord:bool)->List[TextSelection]:
#        """
#
#        """
#        pass
#


#
#    @abc.abstractmethod
#    def FindAllPattern(self ,pattern:'Regex')->List['TextSelection']:
#        """
#
#        """
#        pass
#


#
#    @abc.abstractmethod
#    def FindAllString(self ,given:str,caseSensitive:bool,wholeWord:bool)->List['TextSelection']:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def Replace(self ,pattern:'Regex',replace:str)->int:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def Replace(self ,given:str,replace:str,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def Replace(self ,pattern:'Regex',textSelection:TextSelection)->int:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def Replace(self ,given:str,textSelection:TextSelection,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ReplaceInLine(self ,given:str,replace:str,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def ReplaceInLine(self ,pattern:'Regex',replace:str)->int:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def ReplaceInLine(self ,given:str,replacement:TextSelection,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def ReplaceInLine(self ,pattern:'Regex',replacement:TextSelection)->int:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def FindString(self ,startTextBodyItem:BodyRegion,given:str,caseSensitive:bool,wholeWord:bool)->TextSelection:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def FindPattern(self ,startBodyItem:BodyRegion,pattern:'Regex')->TextSelection:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def FindStringInLine(self ,startTextBodyItem:BodyRegion,given:str,caseSensitive:bool,wholeWord:bool)->List[TextSelection]:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def FindPatternInLine(self ,startBodyItem:BodyRegion,pattern:'Regex')->List[TextSelection]:
#        """
#
#        """
#        pass
#


    @abc.abstractmethod
    def ResetFindState(self):
        """

        """
        pass



    @abc.abstractmethod
    def LoadFromStream(self ,stream:'Stream',fileFormat:'FileFormat'):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def SaveToFile(self ,stream:Stream,fileFormat:FileFormat):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def LoadFromFile(self ,fileName:str):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def LoadFromFile(self ,fileName:str,fileFormat:FileFormat):
        """

        """
        pass



    @abc.abstractmethod
    def LoadFromFileInReadMode(self ,strFileName:str,fileFormat:'FileFormat'):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def SaveToFile(self ,fileName:str):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def SaveToFile(self ,fileName:str,fileFormat:FileFormat):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ImportContent(self ,doc:'IDocument'):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ImportContent(self ,doc:'IDocument',importStyles:bool):
        """

        """
        pass


