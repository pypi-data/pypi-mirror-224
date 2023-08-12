from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Section (  DocumentContainer, ISection, ICompositeObject) :
    """

    """
    @property

    def Body(self)->'Body':
        """
    <summary>
        Gets the section body.
    </summary>
<value>The body.</value>
        """
        GetDllLibDoc().Section_get_Body.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_Body.restype=c_void_p
        intPtr = GetDllLibDoc().Section_get_Body(self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @property

    def EndnoteOptions(self)->'FootEndnoteOptions':
        """
    <summary>
        Gets or sets options that control numbering and positioning of endnotes in current section. 
    </summary>
        """
        GetDllLibDoc().Section_get_EndnoteOptions.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_EndnoteOptions.restype=c_void_p
        intPtr = GetDllLibDoc().Section_get_EndnoteOptions(self.Ptr)
        ret = None if intPtr==None else FootEndnoteOptions(intPtr)
        return ret


    @property

    def FootnoteOptions(self)->'FootEndnoteOptions':
        """
    <summary>
        Gets or sets options that control numbering and positioning of footnote in current section. 
    </summary>
        """
        GetDllLibDoc().Section_get_FootnoteOptions.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_FootnoteOptions.restype=c_void_p
        intPtr = GetDllLibDoc().Section_get_FootnoteOptions(self.Ptr)
        from spire.doc import FootEndnoteOptions
        ret = None if intPtr==None else FootEndnoteOptions(intPtr)
        return ret


    @property

    def HeadersFooters(self)->'HeadersFooters':
        """
    <summary>
        Gets headers/footers of current section.
    </summary>
        """
        GetDllLibDoc().Section_get_HeadersFooters.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_HeadersFooters.restype=c_void_p
        intPtr = GetDllLibDoc().Section_get_HeadersFooters(self.Ptr)
        from spire.doc import HeadersFooters
        ret = None if intPtr==None else HeadersFooters(intPtr)
        return ret


    @property

    def PageSetup(self)->'PageSetup':
        """
    <summary>
        Gets page Setup of current section.
    </summary>
        """
        GetDllLibDoc().Section_get_PageSetup.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_PageSetup.restype=c_void_p
        intPtr = GetDllLibDoc().Section_get_PageSetup(self.Ptr)
        from spire.doc import PageSetup
        ret = None if intPtr==None else PageSetup(intPtr)
        return ret


    @property

    def Columns(self)->'ColumnCollection':
        """
    <summary>
        Get collection of columns which logically divide page on many.
            printing/publishing areas
    </summary>
        """
        GetDllLibDoc().Section_get_Columns.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_Columns.restype=c_void_p
        intPtr = GetDllLibDoc().Section_get_Columns(self.Ptr)
        ret = None if intPtr==None else ColumnCollection(intPtr)
        return ret


    @property

    def BreakCode(self)->'SectionBreakType':
        """
    <summary>
        Returns or sets break code.
    </summary>
        """
        GetDllLibDoc().Section_get_BreakCode.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_BreakCode.restype=c_int
        ret = GetDllLibDoc().Section_get_BreakCode(self.Ptr)
        objwraped = SectionBreakType(ret)
        return objwraped

    @BreakCode.setter
    def BreakCode(self, value:'SectionBreakType'):
        GetDllLibDoc().Section_set_BreakCode.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Section_set_BreakCode(self.Ptr, value.value)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().Section_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().Section_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
    <summary>
        Gets the child objects.
    </summary>
<value>The child objects.</value>
        """
        GetDllLibDoc().Section_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().Section_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def Paragraphs(self)->ParagraphCollection:
        """
    <summary>
        Gets the paragraphs.
    </summary>
<value>The paragraphs.</value>
        """
        GetDllLibDoc().Section_get_Paragraphs.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_Paragraphs.restype=c_void_p
        intPtr = GetDllLibDoc().Section_get_Paragraphs(self.Ptr)
        ret = None if intPtr==None else ParagraphCollection(intPtr)
        return ret


    @property

    def Tables(self)->'TableCollection':
        """
    <summary>
        Gets the tables.
    </summary>
<value>The tables.</value>
        """
        GetDllLibDoc().Section_get_Tables.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_Tables.restype=c_void_p
        intPtr = GetDllLibDoc().Section_get_Tables(self.Ptr)
        ret = None if intPtr==None else TableCollection(intPtr)
        return ret


    @property

    def TextDirection(self)->'TextDirection':
        """
    <summary>
        Gets or Sets the text direction.
    </summary>
        """
        GetDllLibDoc().Section_get_TextDirection.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_TextDirection.restype=c_int
        ret = GetDllLibDoc().Section_get_TextDirection(self.Ptr)
        objwraped = TextDirection(ret)
        return objwraped

    @TextDirection.setter
    def TextDirection(self, value:'TextDirection'):
        GetDllLibDoc().Section_set_TextDirection.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Section_set_TextDirection(self.Ptr, value.value)

    @property
    def ProtectForm(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether [protect form].
    </summary>
        """
        GetDllLibDoc().Section_get_ProtectForm.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_ProtectForm.restype=c_bool
        ret = GetDllLibDoc().Section_get_ProtectForm(self.Ptr)
        return ret

    @ProtectForm.setter
    def ProtectForm(self, value:bool):
        GetDllLibDoc().Section_set_ProtectForm.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Section_set_ProtectForm(self.Ptr, value)


    def AddColumn(self ,width:float,spacing:float)->'Column':
        """
    <summary>
        Adds new column to the section.
    </summary>
    <param name="width">The width.</param>
    <param name="spacing">The spacing.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().Section_AddColumn.argtypes=[c_void_p ,c_float,c_float]
        GetDllLibDoc().Section_AddColumn.restype=c_void_p
        intPtr = GetDllLibDoc().Section_AddColumn(self.Ptr, width,spacing)
        ret = None if intPtr==None else Column(intPtr)
        return ret


    def MakeColumnsSameWidth(self):
        """
    <summary>
        Makes all columns in current section to be of equal width.
    </summary>
        """
        GetDllLibDoc().Section_MakeColumnsSameWidth.argtypes=[c_void_p]
        GetDllLibDoc().Section_MakeColumnsSameWidth(self.Ptr)


    def Clone(self)->'Section':
        """

        """
        GetDllLibDoc().Section_Clone.argtypes=[c_void_p]
        GetDllLibDoc().Section_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().Section_Clone(self.Ptr)
        ret = None if intPtr==None else Section(intPtr)
        return ret



    def CloneSectionPropertiesTo(self ,destSection:'Section'):
        """
    <summary>
        Clones the properties of the current to the destination section.
    </summary>
    <param name="destSection">The destination section.</param>
        """
        intPtrdestSection:c_void_p = destSection.Ptr

        GetDllLibDoc().Section_CloneSectionPropertiesTo.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Section_CloneSectionPropertiesTo(self.Ptr, intPtrdestSection)


    def AddParagraph(self)->'Paragraph':
        """
    <summary>
        Adds the paragraph.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Section_AddParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Section_AddParagraph.restype=c_void_p
        intPtr = GetDllLibDoc().Section_AddParagraph(self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @dispatch

    def AddTable(self)->Table:
        """
    <summary>
        Adds the table.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Section_AddTable.argtypes=[c_void_p]
        GetDllLibDoc().Section_AddTable.restype=c_void_p
        intPtr = GetDllLibDoc().Section_AddTable(self.Ptr)
        ret = None if intPtr==None else Table(intPtr)
        return ret


    @dispatch

    def AddTable(self ,showBorder:bool)->Table:
        """
    <summary>
        Adds the table.
    </summary>
    <param name="showBorder">Display table borders.True to display;False does not display. </param>
    <returns></returns>
        """
        
        GetDllLibDoc().Section_AddTableS.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().Section_AddTableS.restype=c_void_p
        intPtr = GetDllLibDoc().Section_AddTableS(self.Ptr, showBorder)
        ret = None if intPtr==None else Table(intPtr)
        return ret


