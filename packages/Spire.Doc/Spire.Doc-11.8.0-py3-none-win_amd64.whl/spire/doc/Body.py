from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Body (  DocumentContainer, IBody, ICompositeObject) :
    """

    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().Body_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().Body_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Paragraphs(self)->'ParagraphCollection':
        """
    <summary>
        Gets inner paragraphs
    </summary>
        """
        GetDllLibDoc().Body_get_Paragraphs.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_Paragraphs.restype=c_void_p
        intPtr = GetDllLibDoc().Body_get_Paragraphs(self.Ptr)
        ret = None if intPtr==None else ParagraphCollection(intPtr)
        return ret


    @property

    def Tables(self)->'TableCollection':
        """
    <summary>
        Gets inner tables
    </summary>
        """
        GetDllLibDoc().Body_get_Tables.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_Tables.restype=c_void_p
        intPtr = GetDllLibDoc().Body_get_Tables(self.Ptr)
        from spire.doc import TableCollection
        ret = None if intPtr==None else TableCollection(intPtr)
        return ret


    @property

    def FormFields(self)->'FormFieldCollection':
        """
    <summary>
        Gets the form fields.
    </summary>
<value>The form fields.</value>
        """
        GetDllLibDoc().Body_get_FormFields.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_FormFields.restype=c_void_p
        intPtr = GetDllLibDoc().Body_get_FormFields(self.Ptr)
        from spire.doc import FormFieldCollection
        ret = None if intPtr==None else FormFieldCollection(intPtr)
        return ret


    @property

    def LastParagraph(self)->'IParagraph':
        """
    <summary>
        Gets the last paragraph.
    </summary>
<value>The last paragraph.</value>
        """
        GetDllLibDoc().Body_get_LastParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_LastParagraph.restype=c_void_p
        intPtr = GetDllLibDoc().Body_get_LastParagraph(self.Ptr)
        #ret = None if intPtr==None else IParagraph(intPtr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @property

    def FirstParagraph(self)->'IParagraph':
        """
    <summary>
        Gets the First paragraph.
    </summary>
<value>The last paragraph.</value>
        """
        GetDllLibDoc().Body_get_FirstParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_FirstParagraph.restype=c_void_p
        intPtr = GetDllLibDoc().Body_get_FirstParagraph(self.Ptr)
        #ret = None if intPtr==None else IParagraph(intPtr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @property

    def ChildObjects(self)->DocumentObjectCollection:
        """

        """
        GetDllLibDoc().Body_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().Body_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret



    def AddParagraph(self)->'Paragraph':
        """
    <summary>
        Adds paragraph at end of section.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Body_AddParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Body_AddParagraph.restype=c_void_p
        intPtr = GetDllLibDoc().Body_AddParagraph(self.Ptr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @dispatch

    def AddTable(self)->'Table':
        """
    <summary>
        Adds the table.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Body_AddTable.argtypes=[c_void_p]
        GetDllLibDoc().Body_AddTable.restype=c_void_p
        intPtr = GetDllLibDoc().Body_AddTable(self.Ptr)
        from spire.doc import Table
        ret = None if intPtr==None else Table(intPtr)
        return ret


    @dispatch

    def AddTable(self ,showBorder:bool)->'Table':
        """
    <summary>
        Adds the table.
    </summary>
    <param name="showBorder">Is Show Border</param>
    <returns></returns>
        """
        
        GetDllLibDoc().Body_AddTableS.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().Body_AddTableS.restype=c_void_p
        intPtr = GetDllLibDoc().Body_AddTableS(self.Ptr, showBorder)
        from spire.doc import Table
        ret = None if intPtr==None else Table(intPtr)
        return ret


    @dispatch

    def InsertXHTML(self ,html:str):
        """
    <summary>
        Inserts html at end of text body.
    </summary>
        """
        htmlPtr = StrToPtr(html)
        GetDllLibDoc().Body_InsertXHTML.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Body_InsertXHTML(self.Ptr, htmlPtr)

    @dispatch

    def InsertXHTML(self ,html:str,paragraphIndex:int):
        """
    <summary>
        Inserts html. Inserting begins from paragraph specified by paragraphIndex
    </summary>
        """
        htmlPtr = StrToPtr(html)
        GetDllLibDoc().Body_InsertXHTMLHP.argtypes=[c_void_p ,c_char_p,c_int]
        GetDllLibDoc().Body_InsertXHTMLHP(self.Ptr, htmlPtr,paragraphIndex)

    @dispatch

    def InsertXHTML(self ,html:str,paragraphIndex:int,paragraphItemIndex:int):
        """
    <summary>
        Inserts html. Inserting begins from paragraph specified by paragraphIndex, 
            and paragraph item specified by paragraphItemIndex
    </summary>
        """
        htmlPtr = StrToPtr(html)
        GetDllLibDoc().Body_InsertXHTMLHPP.argtypes=[c_void_p ,c_char_p,c_int,c_int]
        GetDllLibDoc().Body_InsertXHTMLHPP(self.Ptr, htmlPtr,paragraphIndex,paragraphItemIndex)

    @dispatch

    def IsValidXHTML(self ,html:str,type:XHTMLValidationType)->bool:
        """
    <summary>
        Validates the XHTML.
    </summary>
    <param name="html">The HTML.</param>
    <param name="type">The validation type.</param>
    <returns>
            	if it is valid XHTML, set to <c>true</c>.
            </returns>
        """
        htmlPtr = StrToPtr(html)
        enumtype:c_int = type.value

        GetDllLibDoc().Body_IsValidXHTML.argtypes=[c_void_p ,c_char_p,c_int]
        GetDllLibDoc().Body_IsValidXHTML.restype=c_bool
        ret = GetDllLibDoc().Body_IsValidXHTML(self.Ptr, htmlPtr,enumtype)
        return ret

#    @dispatch
#
#    def IsValidXHTML(self ,html:str,type:XHTMLValidationType,exceptionMessage:'String&')->bool:
#        """
#
#        """
#        enumtype:c_int = type.value
#        intPtrexceptionMessage:c_void_p = exceptionMessage.Ptr
#
#        GetDllLibDoc().Body_IsValidXHTMLHTE.argtypes=[c_void_p ,c_wchar_p,c_int,c_void_p]
#        GetDllLibDoc().Body_IsValidXHTMLHTE.restype=c_bool
#        ret = GetDllLibDoc().Body_IsValidXHTMLHTE(self.Ptr, html,enumtype,intPtrexceptionMessage)
#        return ret


    def EnsureMinimum(self):
        """
    <summary>
        If the text body has no paragraphs, creates and appends one Paragraph.
    </summary>
        """
        GetDllLibDoc().Body_EnsureMinimum.argtypes=[c_void_p]
        GetDllLibDoc().Body_EnsureMinimum(self.Ptr)

