from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ISection (  ICompositeObject, IDocumentObject) :
    """

    """
    @property

    @abc.abstractmethod
    def Paragraphs(self)->'ParagraphCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Tables(self)->'TableCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Body(self)->'Body':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def PageSetup(self)->'PageSetup':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Columns(self)->'ColumnCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def BreakCode(self)->'SectionBreakType':
        """

        """
        pass


    @BreakCode.setter
    @abc.abstractmethod
    def BreakCode(self, value:'SectionBreakType'):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def ProtectForm(self)->bool:
        """

        """
        pass


    @ProtectForm.setter
    @abc.abstractmethod
    def ProtectForm(self, value:bool):
        """

        """
        pass



    @abc.abstractmethod
    def AddColumn(self ,width:float,spacing:float)->'Column':
        """

        """
        pass



    @abc.abstractmethod
    def AddParagraph(self)->'Paragraph':
        """

        """
        pass



    @abc.abstractmethod
    def AddTable(self)->'Table':
        """

        """
        pass



    @abc.abstractmethod
    def Clone(self)->'Section':
        """

        """
        pass


    @abc.abstractmethod
    def MakeColumnsSameWidth(self):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def HeadersFooters(self)->'HeadersFooters':
        """

        """
        pass


