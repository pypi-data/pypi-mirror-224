from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ITable (  ICompositeObject, IDocumentObject) :
    """

    """
    @property

    @abc.abstractmethod
    def Rows(self)->'RowCollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def TableFormat(self)->'RowFormat':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def LastCell(self)->'TableCell':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def FirstRow(self)->'TableRow':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def LastRow(self)->'TableRow':
        """

        """
        pass



    @abc.abstractmethod
    def get_Item(self ,row:int,column:int)->'TableCell':
        """

        """
        pass


    @property
    @abc.abstractmethod
    def Width(self)->float:
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AddRow(self)->TableRow:
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AddRow(self ,isCopyFormat:bool)->TableRow:
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AddRow(self ,isCopyFormat:bool,autoPopulateCells:bool)->TableRow:
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ResetCells(self ,rowsNum:int,columnsNum:int):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ResetCells(self ,rowsNum:int,columnsNum:int,format:RowFormat,cellWidth:float):
        """

        """
        pass



    @abc.abstractmethod
    def ApplyVerticalMerge(self ,columnIndex:int,startRowIndex:int,endRowIndex:int):
        """

        """
        pass



    @abc.abstractmethod
    def ApplyHorizontalMerge(self ,rowIndex:int,startCellIndex:int,endCellIndex:int):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def IndentFromLeft(self)->float:
        """

        """
        pass


    @IndentFromLeft.setter
    @abc.abstractmethod
    def IndentFromLeft(self, value:float):
        """

        """
        pass


    @abc.abstractmethod
    def RemoveAbsPosition(self):
        """

        """
        pass


