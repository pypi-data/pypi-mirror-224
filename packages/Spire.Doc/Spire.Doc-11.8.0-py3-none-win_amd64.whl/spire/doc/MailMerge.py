from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MailMerge (SpireObject) :
    """

    """

    def ExecuteGroup(self ,dataSource:'MailMergeDataTable'):
        """

        """
        intPtrdataSource:c_void_p = dataSource.Ptr

        GetDllLibDoc().MailMerge_ExecuteGroup.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().MailMerge_ExecuteGroup(self.Ptr, intPtrdataSource)

    @property
    def ClearFields(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether [clear fields]. by default value is true.
    </summary>
<value>
  <c>true</c> if it clears the fields, set to <c>true</c>.</value>
        """
        GetDllLibDoc().MailMerge_get_ClearFields.argtypes=[c_void_p]
        GetDllLibDoc().MailMerge_get_ClearFields.restype=c_bool
        ret = GetDllLibDoc().MailMerge_get_ClearFields(self.Ptr)
        return ret

    @ClearFields.setter
    def ClearFields(self, value:bool):
        GetDllLibDoc().MailMerge_set_ClearFields.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().MailMerge_set_ClearFields(self.Ptr, value)

    @property

    def MailMergeMainDocumentType(self)->'MailMergeMainDocumentType':
        """

        """
        GetDllLibDoc().MailMerge_get_MailMergeMainDocumentType.argtypes=[c_void_p]
        GetDllLibDoc().MailMerge_get_MailMergeMainDocumentType.restype=c_int
        ret = GetDllLibDoc().MailMerge_get_MailMergeMainDocumentType(self.Ptr)
        objwraped = MailMergeMainDocumentType(ret)
        return objwraped

    @MailMergeMainDocumentType.setter
    def MailMergeMainDocumentType(self, value:'MailMergeMainDocumentType'):
        GetDllLibDoc().MailMerge_set_MailMergeMainDocumentType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().MailMerge_set_MailMergeMainDocumentType(self.Ptr, value.value)

    @property
    def ClearGroupTag(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether [clear group tag]. by default value is false.
    </summary>
        """
        GetDllLibDoc().MailMerge_get_ClearGroupTag.argtypes=[c_void_p]
        GetDllLibDoc().MailMerge_get_ClearGroupTag.restype=c_bool
        ret = GetDllLibDoc().MailMerge_get_ClearGroupTag(self.Ptr)
        return ret

    @ClearGroupTag.setter
    def ClearGroupTag(self, value:bool):
        GetDllLibDoc().MailMerge_set_ClearGroupTag.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().MailMerge_set_ClearGroupTag(self.Ptr, value)

    @property
    def HideEmptyParagraphs(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to remove paragraphs which contain empty merge fields
    </summary>
        """
        GetDllLibDoc().MailMerge_get_HideEmptyParagraphs.argtypes=[c_void_p]
        GetDllLibDoc().MailMerge_get_HideEmptyParagraphs.restype=c_bool
        ret = GetDllLibDoc().MailMerge_get_HideEmptyParagraphs(self.Ptr)
        return ret

    @HideEmptyParagraphs.setter
    def HideEmptyParagraphs(self, value:bool):
        GetDllLibDoc().MailMerge_set_HideEmptyParagraphs.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().MailMerge_set_HideEmptyParagraphs(self.Ptr, value)

    @property
    def HideEmptyGroup(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to remove groups which contain empty merge fields
    </summary>
        """
        GetDllLibDoc().MailMerge_get_HideEmptyGroup.argtypes=[c_void_p]
        GetDllLibDoc().MailMerge_get_HideEmptyGroup.restype=c_bool
        ret = GetDllLibDoc().MailMerge_get_HideEmptyGroup(self.Ptr)
        return ret

    @HideEmptyGroup.setter
    def HideEmptyGroup(self, value:bool):
        GetDllLibDoc().MailMerge_set_HideEmptyGroup.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().MailMerge_set_HideEmptyGroup(self.Ptr, value)

#    @property
#
#    def MappedFields(self)->'Dictionary2':
#        """
#
#        """
#        GetDllLibDoc().MailMerge_get_MappedFields.argtypes=[c_void_p]
#        GetDllLibDoc().MailMerge_get_MappedFields.restype=c_void_p
#        intPtr = GetDllLibDoc().MailMerge_get_MappedFields(self.Ptr)
#        ret = None if intPtr==None else Dictionary2(intPtr)
#        return ret
#



    def add_MergeField(self ,value:'MergeFieldEventHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().MailMerge_add_MergeField.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().MailMerge_add_MergeField(self.Ptr, intPtrvalue)


    def remove_MergeField(self ,value:'MergeFieldEventHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().MailMerge_remove_MergeField.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().MailMerge_remove_MergeField(self.Ptr, intPtrvalue)


    def add_MergeImageField(self ,value:'MergeImageFieldEventHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().MailMerge_add_MergeImageField.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().MailMerge_add_MergeImageField(self.Ptr, intPtrvalue)


    def remove_MergeImageField(self ,value:'MergeImageFieldEventHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().MailMerge_remove_MergeImageField.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().MailMerge_remove_MergeImageField(self.Ptr, intPtrvalue)


    def add_MergeGroup(self ,value:'MergeGroupEventHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().MailMerge_add_MergeGroup.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().MailMerge_add_MergeGroup(self.Ptr, intPtrvalue)


    def remove_MergeGroup(self ,value:'MergeGroupEventHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().MailMerge_remove_MergeGroup.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().MailMerge_remove_MergeGroup(self.Ptr, intPtrvalue)

    @dispatch

    def Execute(self ,fieldNames:List[str],fieldValues:List[str]):
        """

        """
        #arrayfieldNames:ArrayTypefieldNames = ""
        countfieldNames = len(fieldNames)
        ArrayTypefieldNames = c_char_p * countfieldNames
        arrayfieldNames = ArrayTypefieldNames()
        for i in range(0, countfieldNames):
            arrayfieldNames[i] = StrToPtr(fieldNames[i])

        #arrayfieldValues:ArrayTypefieldValues = ""
        countfieldValues = len(fieldValues)
        ArrayTypefieldValues = c_char_p * countfieldValues
        arrayfieldValues = ArrayTypefieldValues()   
        for i in range(0, countfieldValues):
            arrayfieldValues[i] = StrToPtr(fieldValues[i])


        GetDllLibDoc().MailMerge_Execute.argtypes=[c_void_p ,ArrayTypefieldNames,c_int,ArrayTypefieldValues,c_int]
        GetDllLibDoc().MailMerge_Execute(self.Ptr, arrayfieldNames,countfieldNames,arrayfieldValues,countfieldValues)

#    @dispatch
#
#    def Execute(self ,row:'DataRow'):
#        """
#    <summary>
#        Performs mail merge from a DataRow into the document
#    </summary>
#    <param name="row"></param>
#        """
#        intPtrrow:c_void_p = row.Ptr
#
#        GetDllLibDoc().MailMerge_ExecuteR.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().MailMerge_ExecuteR(self.Ptr, intPtrrow)


    @dispatch

    def Execute(self ,dataSource:IEnumerable):
        """
    <summary>
        Performs mail merge operation.
    </summary>
    <param name="dataSource">IEnumerable data source</param>
        """
        intPtrdataSource:c_void_p = dataSource.Ptr

        GetDllLibDoc().MailMerge_ExecuteD.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().MailMerge_ExecuteD(self.Ptr, intPtrdataSource)

#    @dispatch
#
#    def Execute(self ,table:'DataTable'):
#        """
#    <summary>
#        Performs mail merge from a DataTable
#    </summary>
#    <param name="table"></param>
#        """
#        intPtrtable:c_void_p = table.Ptr
#
#        GetDllLibDoc().MailMerge_ExecuteT.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().MailMerge_ExecuteT(self.Ptr, intPtrtable)


#    @dispatch
#
#    def Execute(self ,dataView:'DataView'):
#        """
#    <summary>
#         Performs mail merge from a DataView
#    </summary>
#    <param name="dataView"></param>
#        """
#        intPtrdataView:c_void_p = dataView.Ptr
#
#        GetDllLibDoc().MailMerge_ExecuteD1.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().MailMerge_ExecuteD1(self.Ptr, intPtrdataView)


#    @dispatch
#
#    def Execute(self ,dataReader:'IDataReader'):
#        """
#    <summary>
#        Performs mail merge from a DataView
#    </summary>
#    <param name="dataReader"></param>
#        """
#        intPtrdataReader:c_void_p = dataReader.Ptr
#
#        GetDllLibDoc().MailMerge_ExecuteD11.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().MailMerge_ExecuteD11(self.Ptr, intPtrdataReader)


#    @dispatch
#
#    def ExecuteWidthRegion(self ,table:'DataTable'):
#        """
#    <summary>
#        Performs Mail Merge within a region from a DataTable.
#    </summary>
#    <param name="table"></param>
#        """
#        intPtrtable:c_void_p = table.Ptr
#
#        GetDllLibDoc().MailMerge_ExecuteWidthRegion.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().MailMerge_ExecuteWidthRegion(self.Ptr, intPtrtable)


#    @dispatch
#
#    def ExecuteWidthRegion(self ,dataView:'DataView'):
#        """
#    <summary>
#        Performs Mail Merge within a region from a DataView.
#    </summary>
#    <param name="dataView"></param>
#        """
#        intPtrdataView:c_void_p = dataView.Ptr
#
#        GetDllLibDoc().MailMerge_ExecuteWidthRegionD.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().MailMerge_ExecuteWidthRegionD(self.Ptr, intPtrdataView)


#    @dispatch
#
#    def ExecuteWidthRegion(self ,dataReader:'IDataReader'):
#        """
#    <summary>
#        Performs Mail Merge within a region from a DataReader.
#    </summary>
#    <param name="dataReader"></param>
#        """
#        intPtrdataReader:c_void_p = dataReader.Ptr
#
#        GetDllLibDoc().MailMerge_ExecuteWidthRegionD1.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().MailMerge_ExecuteWidthRegionD1(self.Ptr, intPtrdataReader)


#    @dispatch
#
#    def ExecuteWidthNestedRegion(self ,dataSource:MailMergeDataSet,filters:'List1'):
#        """
#    <summary>
#        Performs mail merge operation.
#    </summary>
#    <param name="dataSource">MailMergeDataSet</param>
#    <param name="commands">Commands list</param>
#        """
#        intPtrdataSource:c_void_p = dataSource.Ptr
#        intPtrfilters:c_void_p = filters.Ptr
#
#        GetDllLibDoc().MailMerge_ExecuteWidthNestedRegion.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().MailMerge_ExecuteWidthNestedRegion(self.Ptr, intPtrdataSource,intPtrfilters)


#    @dispatch
#
#    def ExecuteWidthNestedRegion(self ,conn:'DbConnection',commands:'List1'):
#        """
#    <summary>
#        Executes nested mailmerge within a region for the specified data.
#    </summary>
#    <param name="conn">The Connection.</param>
#    <param name="commands">The commands.</param>
#        """
#        intPtrconn:c_void_p = conn.Ptr
#        intPtrcommands:c_void_p = commands.Ptr
#
#        GetDllLibDoc().MailMerge_ExecuteWidthNestedRegionCC.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().MailMerge_ExecuteWidthNestedRegionCC(self.Ptr, intPtrconn,intPtrcommands)


#    @dispatch
#
#    def ExecuteWidthNestedRegion(self ,dataSet:'DataSet',commands:'List1'):
#        """
#    <summary>
#        Executes the nested region.
#    </summary>
#    <param name="dataSet">The data set.</param>
#    <param name="commands">The commands.</param>
#        """
#        intPtrdataSet:c_void_p = dataSet.Ptr
#        intPtrcommands:c_void_p = commands.Ptr
#
#        GetDllLibDoc().MailMerge_ExecuteWidthNestedRegionDC.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().MailMerge_ExecuteWidthNestedRegionDC(self.Ptr, intPtrdataSet,intPtrcommands)


    @dispatch

    def GetMergeFieldNames(self)->List[str]:
        """
    <summary>
        Returns a collection of mergefield names found in the document.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().MailMerge_GetMergeFieldNames.argtypes=[c_void_p]
        GetDllLibDoc().MailMerge_GetMergeFieldNames.restype=IntPtrArray
        intPtrArray = GetDllLibDoc().MailMerge_GetMergeFieldNames(self.Ptr)
        ret = GetStrVectorFromArray(intPtrArray,c_void_p)
        return ret

    @dispatch

    def GetMergeFieldNames(self ,groupName:str)->List[str]:
        """
    <summary>
        Gets the merge field names.
    </summary>
    <param name="groupName">Name of the region.</param>
    <returns></returns>
        """
        groupNamePtr = StrToPtr(groupName)
        GetDllLibDoc().MailMerge_GetMergeFieldNamesG.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().MailMerge_GetMergeFieldNamesG.restype=IntPtrArray
        intPtrArray = GetDllLibDoc().MailMerge_GetMergeFieldNamesG(self.Ptr, groupNamePtr)
        ret = GetStrVectorFromArray(intPtrArray, c_void_p)
        return ret


    def GetMergeGroupNames(self)->List[str]:
        """
    <summary>
        Gets the merge field names.
    </summary>
    <param name="groupName">Name of the region.</param>
    <returns></returns>
        """
        GetDllLibDoc().MailMerge_GetMergeGroupNames.argtypes=[c_void_p]
        GetDllLibDoc().MailMerge_GetMergeGroupNames.restype=IntPtrArray
        intPtrArray = GetDllLibDoc().MailMerge_GetMergeGroupNames(self.Ptr)
        ret = GetStrVectorFromArray(intPtrArray,c_void_p)
        return ret

