from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SummaryDocumentProperties (  DocumentSerializable) :
    """

    """
    @property

    def Author(self)->str:
        """
    <summary>
        Gets or sets author name
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Author.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Author.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SummaryDocumentProperties_get_Author(self.Ptr))
        return ret


    @Author.setter
    def Author(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Author.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SummaryDocumentProperties_set_Author(self.Ptr, valuePtr)

    @property

    def ApplicationName(self)->str:
        """
    <summary>
        Gets or sets application name
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_ApplicationName.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_ApplicationName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SummaryDocumentProperties_get_ApplicationName(self.Ptr))
        return ret


    @ApplicationName.setter
    def ApplicationName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_ApplicationName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SummaryDocumentProperties_set_ApplicationName(self.Ptr, valuePtr)

    @property

    def Title(self)->str:
        """
    <summary>
        Gets or sets the document title
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Title.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Title.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SummaryDocumentProperties_get_Title(self.Ptr))
        return ret


    @Title.setter
    def Title(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Title.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SummaryDocumentProperties_set_Title(self.Ptr, valuePtr)

    @property

    def Subject(self)->str:
        """
    <summary>
        Gets or sets the subject of the document
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Subject.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Subject.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SummaryDocumentProperties_get_Subject(self.Ptr))
        return ret


    @Subject.setter
    def Subject(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Subject.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SummaryDocumentProperties_set_Subject(self.Ptr, valuePtr)

    @property

    def Keywords(self)->str:
        """
    <summary>
        Gets or sets the document keywords
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Keywords.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Keywords.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SummaryDocumentProperties_get_Keywords(self.Ptr))
        return ret


    @Keywords.setter
    def Keywords(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Keywords.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SummaryDocumentProperties_set_Keywords(self.Ptr, valuePtr)

    @property

    def Comments(self)->str:
        """
    <summary>
        Gets or sets the comments that provide additional information about the document
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Comments.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Comments.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SummaryDocumentProperties_get_Comments(self.Ptr))
        return ret


    @Comments.setter
    def Comments(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Comments.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SummaryDocumentProperties_set_Comments(self.Ptr, valuePtr)

    @property

    def Template(self)->str:
        """
    <summary>
        Gets or sets the template name of the document
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Template.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Template.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SummaryDocumentProperties_get_Template(self.Ptr))
        return ret


    @Template.setter
    def Template(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Template.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SummaryDocumentProperties_set_Template(self.Ptr, valuePtr)

    @property

    def LastAuthor(self)->str:
        """
    <summary>
        Gets or sets the last author name
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_LastAuthor.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_LastAuthor.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SummaryDocumentProperties_get_LastAuthor(self.Ptr))
        return ret


    @LastAuthor.setter
    def LastAuthor(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_LastAuthor.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SummaryDocumentProperties_set_LastAuthor(self.Ptr, valuePtr)

    @property

    def RevisionNumber(self)->str:
        """
    <summary>
        Gets or sets the document revision number
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_RevisionNumber.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_RevisionNumber.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SummaryDocumentProperties_get_RevisionNumber(self.Ptr))
        return ret


    @RevisionNumber.setter
    def RevisionNumber(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_RevisionNumber.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SummaryDocumentProperties_set_RevisionNumber(self.Ptr, valuePtr)

    @property

    def TotalEditingTime(self)->'TimeSpan':
        """
    <summary>
        Gets or sets the document total editing time
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_TotalEditingTime.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_TotalEditingTime.restype=c_void_p
        intPtr = GetDllLibDoc().SummaryDocumentProperties_get_TotalEditingTime(self.Ptr)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @TotalEditingTime.setter
    def TotalEditingTime(self, value:'TimeSpan'):
        GetDllLibDoc().SummaryDocumentProperties_set_TotalEditingTime.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_set_TotalEditingTime(self.Ptr, value.Ptr)

    @property

    def LastPrinted(self)->'DateTime':
        """
    <summary>
        Returns or sets the last print date
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_LastPrinted.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_LastPrinted.restype=c_void_p
        intPtr = GetDllLibDoc().SummaryDocumentProperties_get_LastPrinted(self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @LastPrinted.setter
    def LastPrinted(self, value:'DateTime'):
        GetDllLibDoc().SummaryDocumentProperties_set_LastPrinted.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_set_LastPrinted(self.Ptr, value.Ptr)

    @property

    def CreateDate(self)->'DateTime':
        """
    <summary>
        Gets or sets the document creation date
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_CreateDate.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_CreateDate.restype=c_void_p
        intPtr = GetDllLibDoc().SummaryDocumentProperties_get_CreateDate(self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @CreateDate.setter
    def CreateDate(self, value:'DateTime'):
        GetDllLibDoc().SummaryDocumentProperties_set_CreateDate.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_set_CreateDate(self.Ptr, value.Ptr)

    @property

    def LastSaveDate(self)->'DateTime':
        """
    <summary>
        Returns or sets the last save date
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_LastSaveDate.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_LastSaveDate.restype=c_void_p
        intPtr = GetDllLibDoc().SummaryDocumentProperties_get_LastSaveDate(self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @LastSaveDate.setter
    def LastSaveDate(self, value:'DateTime'):
        GetDllLibDoc().SummaryDocumentProperties_set_LastSaveDate.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_set_LastSaveDate(self.Ptr, value.Ptr)

    @property
    def PageCount(self)->int:
        """
    <summary>
        Gets document pages count
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_PageCount.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_PageCount.restype=c_int
        ret = GetDllLibDoc().SummaryDocumentProperties_get_PageCount(self.Ptr)
        return ret

    @property
    def WordCount(self)->int:
        """
    <summary>
        Gets document words count
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_WordCount.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_WordCount.restype=c_int
        ret = GetDllLibDoc().SummaryDocumentProperties_get_WordCount(self.Ptr)
        return ret

    @property
    def CharCount(self)->int:
        """
    <summary>
        Gets document characters count
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_CharCount.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_CharCount.restype=c_int
        ret = GetDllLibDoc().SummaryDocumentProperties_get_CharCount(self.Ptr)
        return ret

    @property
    def CharCountWithSpace(self)->int:
        """
    <summary>
        Gets document characters count(including spaces)
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_CharCountWithSpace.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_CharCountWithSpace.restype=c_int
        ret = GetDllLibDoc().SummaryDocumentProperties_get_CharCountWithSpace(self.Ptr)
        return ret

    @property

    def Thumbnail(self)->str:
        """
    <summary>
        Returns or setsthumbnail picture for document preview
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Thumbnail.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Thumbnail.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().SummaryDocumentProperties_get_Thumbnail(self.Ptr))
        return ret


    @Thumbnail.setter
    def Thumbnail(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Thumbnail.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().SummaryDocumentProperties_set_Thumbnail(self.Ptr, valuePtr)

    @property
    def DocSecurity(self)->int:
        """
    <summary>
        Gets or sets document security level
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_DocSecurity.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_DocSecurity.restype=c_int
        ret = GetDllLibDoc().SummaryDocumentProperties_get_DocSecurity(self.Ptr)
        return ret

    @DocSecurity.setter
    def DocSecurity(self, value:int):
        GetDllLibDoc().SummaryDocumentProperties_set_DocSecurity.argtypes=[c_void_p, c_int]
        GetDllLibDoc().SummaryDocumentProperties_set_DocSecurity(self.Ptr, value)

    @property
    def Count(self)->int:
        """
    <summary>
        Gets summary count of document properties
    </summary>
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Count.restype=c_int
        ret = GetDllLibDoc().SummaryDocumentProperties_get_Count(self.Ptr)
        return ret


    def Add(self ,key:int,props:'DocumentProperty'):
        """
    <summary>
        Adds the specified name.
    </summary>
    <param name="name">The name.</param>
    <param name="value">The value.</param>
        """
        intPtrprops:c_void_p = props.Ptr

        GetDllLibDoc().SummaryDocumentProperties_Add.argtypes=[c_void_p ,c_int,c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_Add(self.Ptr, key,intPtrprops)

