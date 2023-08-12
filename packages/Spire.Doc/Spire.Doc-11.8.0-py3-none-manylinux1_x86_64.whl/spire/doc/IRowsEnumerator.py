from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IRowsEnumerator (abc.ABC) :
    """

    """
    @abc.abstractmethod
    def Reset(self):
        """

        """
        pass


    @abc.abstractmethod
    def NextRow(self)->bool:
        """

        """
        pass



    @abc.abstractmethod
    def GetCellValue(self ,columnName:str)->'SpireObject':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def ColumnNames(self)->List[str]:
        """

        """
        pass


    @property
    @abc.abstractmethod
    def RowsCount(self)->int:
        """

        """
        pass


    @property
    @abc.abstractmethod
    def CurrentRowIndex(self)->int:
        """

        """
        pass


    @property

    @abc.abstractmethod
    def TableName(self)->str:
        """

        """
        pass


    @property
    @abc.abstractmethod
    def IsEnd(self)->bool:
        """

        """
        pass


    @property
    @abc.abstractmethod
    def IsLast(self)->bool:
        """

        """
        pass


