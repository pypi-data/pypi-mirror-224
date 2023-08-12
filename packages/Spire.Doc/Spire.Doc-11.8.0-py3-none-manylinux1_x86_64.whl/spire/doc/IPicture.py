from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IPicture (  IParagraphBase, IDocumentObject) :
    """

    """
    @property
    @abc.abstractmethod
    def Height(self)->float:
        """

        """
        pass


    @Height.setter
    @abc.abstractmethod
    def Height(self, value:float):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def Width(self)->float:
        """

        """
        pass


    @Width.setter
    @abc.abstractmethod
    def Width(self, value:float):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def HeightScale(self)->float:
        """

        """
        pass


    @HeightScale.setter
    @abc.abstractmethod
    def HeightScale(self, value:float):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def WidthScale(self)->float:
        """

        """
        pass


    @WidthScale.setter
    @abc.abstractmethod
    def WidthScale(self, value:float):
        """

        """
        pass


#
#    @abc.abstractmethod
#    def LoadImage(self ,imageBytes:'Byte[]'):
#        """
#
#        """
#        pass
#


#    @property
#
#    @abc.abstractmethod
#    def ImageBytes(self)->List['Byte']:
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def AddCaption(self ,name:str,format:'CaptionNumberingFormat',captionPosition:'CaptionPosition')->'IParagraph':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def HorizontalOrigin(self)->'HorizontalOrigin':
        """

        """
        pass


    @HorizontalOrigin.setter
    @abc.abstractmethod
    def HorizontalOrigin(self, value:'HorizontalOrigin'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def VerticalOrigin(self)->'VerticalOrigin':
        """

        """
        pass


    @VerticalOrigin.setter
    @abc.abstractmethod
    def VerticalOrigin(self, value:'VerticalOrigin'):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def HorizontalPosition(self)->float:
        """

        """
        pass


    @HorizontalPosition.setter
    @abc.abstractmethod
    def HorizontalPosition(self, value:float):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def VerticalPosition(self)->float:
        """

        """
        pass


    @VerticalPosition.setter
    @abc.abstractmethod
    def VerticalPosition(self, value:float):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def TextWrappingStyle(self)->'TextWrappingStyle':
        """

        """
        pass


    @TextWrappingStyle.setter
    @abc.abstractmethod
    def TextWrappingStyle(self, value:'TextWrappingStyle'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def TextWrappingType(self)->'TextWrappingType':
        """

        """
        pass


    @TextWrappingType.setter
    @abc.abstractmethod
    def TextWrappingType(self, value:'TextWrappingType'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def HorizontalAlignment(self)->'ShapeHorizontalAlignment':
        """

        """
        pass


    @HorizontalAlignment.setter
    @abc.abstractmethod
    def HorizontalAlignment(self, value:'ShapeHorizontalAlignment'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def VerticalAlignment(self)->'ShapeVerticalAlignment':
        """

        """
        pass


    @VerticalAlignment.setter
    @abc.abstractmethod
    def VerticalAlignment(self, value:'ShapeVerticalAlignment'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def AlternativeText(self)->str:
        """

        """
        pass


    @AlternativeText.setter
    @abc.abstractmethod
    def AlternativeText(self, value:str):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Title(self)->str:
        """

        """
        pass


    @Title.setter
    @abc.abstractmethod
    def Title(self, value:str):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def IsUnderText(self)->bool:
        """

        """
        pass


    @IsUnderText.setter
    @abc.abstractmethod
    def IsUnderText(self, value:bool):
        """

        """
        pass


