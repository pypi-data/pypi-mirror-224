from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IBody (  ICompositeObject, IDocumentObject) :
    """

    """
    @property

    @abc.abstractmethod
    def Tables(self)->'TableCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Paragraphs(self)->'ParagraphCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def FormFields(self)->'FormFieldCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def LastParagraph(self)->'IParagraph':
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


    @dispatch

    @abc.abstractmethod
    def InsertXHTML(self ,html:str):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def InsertXHTML(self ,html:str,paragraphIndex:int):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def InsertXHTML(self ,html:str,paragraphIndex:int,paragraphItemIndex:int):
        """

        """
        pass


    @abc.abstractmethod
    def EnsureMinimum(self):
        """

        """
        pass


