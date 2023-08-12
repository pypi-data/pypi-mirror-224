from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Paragraph (  BodyRegion, IParagraph, IStyleHolder, ICompositeObject) :
    """

    """
    @dispatch
    def __init__(self, doc:IDocument):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().Paragraph_CreateParagraphD.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_CreateParagraphD.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_CreateParagraphD(intPdoc)
        super(Paragraph, self).__init__(intPtr)


    @property

    def ParentSection(self)->'Section':
        """

        """
        GetDllLibDoc().Paragraph_get_ParentSection.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_ParentSection.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_get_ParentSection(self.Ptr)
        ret = None if intPtr==None else Section(intPtr)
        return ret


#    @dispatch
#
#    def Find(self ,pattern:'Regex')->TextSelection:
#        """
#
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Paragraph_Find.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().Paragraph_Find.restype=c_void_p
#        intPtr = GetDllLibDoc().Paragraph_Find(self.Ptr, intPtrpattern)
#        ret = None if intPtr==None else TextSelection(intPtr)
#        return ret
#


    @dispatch

    def Find(self ,given:str,caseSensitive:bool,wholeWord:bool)->TextSelection:
        """

        """
        givenPtr = StrToPtr(given)
        GetDllLibDoc().Paragraph_FindGCW.argtypes=[c_void_p ,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Paragraph_FindGCW.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_FindGCW(self.Ptr, givenPtr,caseSensitive,wholeWord) 
        from spire.doc import TextSelection
        ret = None if intPtr==None else TextSelection(intPtr)
        return ret


    @dispatch

    def Replace(self ,pattern:Regex,replace:str)->int:
        """

        """
        replacePtr = StrToPtr(replace)
        intPtrpattern:c_void_p = pattern.Ptr

        GetDllLibDoc().Paragraph_Replace.argtypes=[c_void_p ,c_void_p,c_char_p]
        GetDllLibDoc().Paragraph_Replace.restype=c_int
        ret = GetDllLibDoc().Paragraph_Replace(self.Ptr, intPtrpattern,replacePtr)
        return ret


    @dispatch

    def Replace(self ,given:str,replace:str,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        givenPtr = StrToPtr(given)
        replacePtr = StrToPtr(replace)
        GetDllLibDoc().Paragraph_ReplaceGRCW.argtypes=[c_void_p ,c_char_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Paragraph_ReplaceGRCW.restype=c_int
        ret = GetDllLibDoc().Paragraph_ReplaceGRCW(self.Ptr, givenPtr,replacePtr,caseSensitive,wholeWord)
        return ret

    @dispatch

    def Replace(self ,pattern:Regex,textSelection:TextSelection)->int:
        """

        """
        intPtrpattern:c_void_p = pattern.Ptr
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Paragraph_ReplacePT.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().Paragraph_ReplacePT.restype=c_int
        ret = GetDllLibDoc().Paragraph_ReplacePT(self.Ptr, intPtrpattern,intPtrtextSelection)
        return ret


    @dispatch

    def Replace(self ,pattern:Regex,textSelection:TextSelection,saveFormatting:bool)->int:
        """

        """
        intPtrpattern:c_void_p = pattern.Ptr
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Paragraph_ReplacePTS.argtypes=[c_void_p ,c_void_p,c_void_p,c_bool]
        GetDllLibDoc().Paragraph_ReplacePTS.restype=c_int
        ret = GetDllLibDoc().Paragraph_ReplacePTS(self.Ptr, intPtrpattern,intPtrtextSelection,saveFormatting)
        return ret


    @dispatch

    def Replace(self ,given:str,textSelection:TextSelection,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        givenPtr = StrToPtr(given)
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Paragraph_ReplaceGTCW.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool]
        GetDllLibDoc().Paragraph_ReplaceGTCW.restype=c_int
        ret = GetDllLibDoc().Paragraph_ReplaceGTCW(self.Ptr, givenPtr,intPtrtextSelection,caseSensitive,wholeWord)
        return ret

    @dispatch

    def Replace(self ,given:str,textSelection:TextSelection,caseSensitive:bool,wholeWord:bool,saveFormatting:bool)->int:
        """

        """
        givenPtr = StrToPtr(given)
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Paragraph_ReplaceGTCWS.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool,c_bool]
        GetDllLibDoc().Paragraph_ReplaceGTCWS.restype=c_int
        ret = GetDllLibDoc().Paragraph_ReplaceGTCWS(self.Ptr, givenPtr,intPtrtextSelection,caseSensitive,wholeWord,saveFormatting)
        return ret

    @dispatch

    def InsertSectionBreak(self)->'Section':
        """
    <summary>
        Inserts the section break.
    </summary>
        """
        GetDllLibDoc().Paragraph_InsertSectionBreak.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_InsertSectionBreak.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_InsertSectionBreak(self.Ptr)
        ret = None if intPtr==None else Section(intPtr)
        return ret


    @dispatch

    def InsertSectionBreak(self ,breakType:SectionBreakType)->'Section':
        """
    <summary>
        Inserts the section break.
    </summary>
    <param name="breakType">Type of the break.</param>
        """
        enumbreakType:c_int = breakType.value

        GetDllLibDoc().Paragraph_InsertSectionBreakB.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_InsertSectionBreakB.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_InsertSectionBreakB(self.Ptr, enumbreakType)
        from spire.doc import Section
        ret = None if intPtr==None else Section(intPtr)
        return ret


#
#    def UpdateWordCount(self ,splitchar:'Char[]',includeTbFnEn:bool):
#        """
#
#        """
#        #arraysplitchar:ArrayTypesplitchar = ""
#        countsplitchar = len(splitchar)
#        ArrayTypesplitchar = c_void_p * countsplitchar
#        arraysplitchar = ArrayTypesplitchar()
#        for i in range(0, countsplitchar):
#            arraysplitchar[i] = splitchar[i].Ptr
#
#
#        GetDllLibDoc().Paragraph_UpdateWordCount.argtypes=[c_void_p ,ArrayTypesplitchar,c_bool]
#        GetDllLibDoc().Paragraph_UpdateWordCount(self.Ptr, arraysplitchar,includeTbFnEn)



    def UpdateListValue(self)->str:
        """
    <summary>
        Updates the list value.
            The value of the list number is obtained by dynamic calculation. 
            The value of the list number of the paragraph directly may be incorrect.
            To obtain the correct value, you need to traverse all paragraphs in the document.
    </summary>
    <returns>the value string.</returns>
        """
        GetDllLibDoc().Paragraph_UpdateListValue.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_UpdateListValue.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Paragraph_UpdateListValue(self.Ptr))
        return ret



    def GetListFormatForApplyStyle(self)->'ListFormat':
        """
    <summary>
        Gets the list format for apply style.
    </summary>
    <returns>the list format.</returns>
        """
        GetDllLibDoc().Paragraph_GetListFormatForApplyStyle.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_GetListFormatForApplyStyle.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_GetListFormatForApplyStyle(self.Ptr)
        ret = None if intPtr==None else ListFormat(intPtr)
        return ret



    def GetIndex(self ,entity:'IDocumentObject')->int:
        """

        """
        intPtrentity:c_void_p = entity.Ptr

        GetDllLibDoc().Paragraph_GetIndex.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Paragraph_GetIndex.restype=c_int
        ret = GetDllLibDoc().Paragraph_GetIndex(self.Ptr, intPtrentity)
        return ret

    @property

    def ListText(self)->str:
        """
    <summary>
        Gets the list text.
            The value of the list number is obtained by dynamic calculation. 
            The value of the list number of the paragraph directly may be incorrect.
            To obtain the correct value, you need to traverse all paragraphs in the document.
    </summary>
        """
        GetDllLibDoc().Paragraph_get_ListText.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_ListText.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Paragraph_get_ListText(self.Ptr))
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
        """
        GetDllLibDoc().Paragraph_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().Paragraph_get_DocumentObjectType(self.Ptr)
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
        GetDllLibDoc().Paragraph_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def StyleName(self)->str:
        """
    <summary>
        Gets paragraph style name.
    </summary>
<value></value>
        """
        GetDllLibDoc().Paragraph_get_StyleName.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_StyleName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Paragraph_get_StyleName(self.Ptr))
        return ret


    @property

    def Text(self)->str:
        """
    <summary>
        Returns or sets paragraph text.
    </summary>
<value></value>
<remarks>All internal formatting will be cleared when new text is set.</remarks>
        """
        GetDllLibDoc().Paragraph_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_Text.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Paragraph_get_Text(self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Paragraph_set_Text.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Paragraph_set_Text(self.Ptr, valuePtr)


    def get_Item(self ,index:int)->'ParagraphBase':
        """
    <summary>
        Gets paragraph item by index.
    </summary>
<value></value>
        """
        
        GetDllLibDoc().Paragraph_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_get_Item.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_get_Item(self.Ptr, index)
        ret = None if intPtr==None else ParagraphBase(intPtr)
        return ret


    @property

    def Items(self)->'ParagraphItemCollection':
        """
    <summary>
        Gets paragraph items.
    </summary>
<value>The items.</value>
        """
        GetDllLibDoc().Paragraph_get_Items.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_Items.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_get_Items(self.Ptr)
        ret = None if intPtr==None else ParagraphItemCollection(intPtr)
        return ret


    @property

    def Format(self)->'ParagraphFormat':
        """
    <summary>
        Gets paragraph format.
    </summary>
<value></value>
        """
        GetDllLibDoc().Paragraph_get_Format.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_Format.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_get_Format(self.Ptr)
        from spire.doc import ParagraphFormat
        ret = None if intPtr==None else ParagraphFormat(intPtr)
        return ret


    @property

    def BreakCharacterFormat(self)->'CharacterFormat':
        """
    <summary>
        Gets character format for the break symbol.
    </summary>
<value></value>
        """
        GetDllLibDoc().Paragraph_get_BreakCharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_BreakCharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_get_BreakCharacterFormat(self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def ListFormat(self)->'ListFormat':
        """
    <summary>
        Gets format of the list for the paragraph.
    </summary>
        """
        GetDllLibDoc().Paragraph_get_ListFormat.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_ListFormat.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_get_ListFormat(self.Ptr)
        from spire.doc import ListFormat
        ret = None if intPtr==None else ListFormat(intPtr)
        return ret


    @property
    def IsInCell(self)->bool:
        """
    <summary>
        Gets a value indicating whether this paragraph is in cell.
    </summary>
<value>
            	if this paragraph is in cell, set to <c>true</c>.
            </value>
        """
        GetDllLibDoc().Paragraph_get_IsInCell.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_IsInCell.restype=c_bool
        ret = GetDllLibDoc().Paragraph_get_IsInCell(self.Ptr)
        return ret

    @property
    def IsEndOfSection(self)->bool:
        """
    <summary>
        Gets a value indicating whether this paragraph is end of section.
    </summary>
<value>
            if this paragraph is end of section, set to <c>true</c>.
            </value>
        """
        GetDllLibDoc().Paragraph_get_IsEndOfSection.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_IsEndOfSection.restype=c_bool
        ret = GetDllLibDoc().Paragraph_get_IsEndOfSection(self.Ptr)
        return ret

    @property
    def IsEndOfHeaderFooter(self)->bool:
        """

        """
        GetDllLibDoc().Paragraph_get_IsEndOfHeaderFooter.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_IsEndOfHeaderFooter.restype=c_bool
        ret = GetDllLibDoc().Paragraph_get_IsEndOfHeaderFooter(self.Ptr)
        return ret

    @property
    def IsEndOfDocument(self)->bool:
        """
    <summary>
        Gets a value indicating whether this paragraph is end of document.
    </summary>
<value>
            if this instance is end of document, set to <c>true</c>.
            </value>
        """
        GetDllLibDoc().Paragraph_get_IsEndOfDocument.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_IsEndOfDocument.restype=c_bool
        ret = GetDllLibDoc().Paragraph_get_IsEndOfDocument(self.Ptr)
        return ret

    @property
    def WordCount(self)->int:
        """

        """
        GetDllLibDoc().Paragraph_get_WordCount.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_WordCount.restype=c_int
        ret = GetDllLibDoc().Paragraph_get_WordCount(self.Ptr)
        return ret

    @property
    def CharCount(self)->int:
        """

        """
        GetDllLibDoc().Paragraph_get_CharCount.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_CharCount.restype=c_int
        ret = GetDllLibDoc().Paragraph_get_CharCount(self.Ptr)
        return ret

    @property
    def CharCountIncludeSpace(self)->int:
        """

        """
        GetDllLibDoc().Paragraph_get_CharCountIncludeSpace.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_CharCountIncludeSpace.restype=c_int
        ret = GetDllLibDoc().Paragraph_get_CharCountIncludeSpace(self.Ptr)
        return ret

    @dispatch

    def ApplyStyle(self ,styleName:str):
        """

        """
        styleNamePtr = StrToPtr(styleName)
        GetDllLibDoc().Paragraph_ApplyStyle.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_ApplyStyle(self.Ptr, styleNamePtr)

    @dispatch

    def ApplyStyle(self ,builtinStyle:BuiltinStyle):
        """

        """
        enumbuiltinStyle:c_int = builtinStyle.value

        GetDllLibDoc().Paragraph_ApplyStyleB.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_ApplyStyleB(self.Ptr, enumbuiltinStyle)

    @dispatch

    def ApplyStyle(self ,style:IParagraphStyle):
        """

        """
        intPtrstyle:c_void_p = style.Ptr

        GetDllLibDoc().Paragraph_ApplyStyleS.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Paragraph_ApplyStyleS(self.Ptr, intPtrstyle)


    def GetStyle(self)->'ParagraphStyle':
        """

        """
        GetDllLibDoc().Paragraph_GetStyle.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_GetStyle.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_GetStyle(self.Ptr)
        ret = None if intPtr==None else ParagraphStyle(intPtr)
        return ret


    def RemoveAbsPosition(self):
        """

        """
        GetDllLibDoc().Paragraph_RemoveAbsPosition.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_RemoveAbsPosition(self.Ptr)


    def AppendText(self ,text:str)->'TextRange':
        """
    <summary>
        Appends text to end of document.
    </summary>
    <param name="text"></param>
    <returns></returns>
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().Paragraph_AppendText.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendText.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendText(self.Ptr, textPtr)
        from spire.doc import TextRange
        ret = None if intPtr==None else TextRange(intPtr)
        return ret


#    @dispatch
#
#    def AppendPicture(self ,imageBytes:'Byte[]')->DocPicture:
#        """
#    <summary>
#        Appends image to end of paragraph.
#    </summary>
#    <returns></returns>
#        """
#        #arrayimageBytes:ArrayTypeimageBytes = ""
#        countimageBytes = len(imageBytes)
#        ArrayTypeimageBytes = c_void_p * countimageBytes
#        arrayimageBytes = ArrayTypeimageBytes()
#        for i in range(0, countimageBytes):
#            arrayimageBytes[i] = imageBytes[i].Ptr
#
#
#        GetDllLibDoc().Paragraph_AppendPicture.argtypes=[c_void_p ,ArrayTypeimageBytes]
#        GetDllLibDoc().Paragraph_AppendPicture.restype=c_void_p
#        intPtr = GetDllLibDoc().Paragraph_AppendPicture(self.Ptr, arrayimageBytes)
#        ret = None if intPtr==None else DocPicture(intPtr)
#        return ret
#



    def AppendField(self ,fieldName:str,fieldType:FieldType)->'Field':
        """
    <summary>
        Appends the field.
    </summary>
    <returns></returns>
        """
        fieldNamePtr = StrToPtr(fieldName)
        enumfieldType:c_int = fieldType.value

        GetDllLibDoc().Paragraph_AppendField.argtypes=[c_void_p ,c_char_p,c_int]
        GetDllLibDoc().Paragraph_AppendField.restype=IntPtrWithTypeName
        intPtr = GetDllLibDoc().Paragraph_AppendField(self.Ptr, fieldNamePtr, enumfieldType)
        ret = None if intPtr==None else self._create(intPtr)
        return ret

    def _create(self, intPtrWithTypeName:IntPtrWithTypeName)->'Field':
        ret= None
        if intPtrWithTypeName == None:
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Fields.CheckBoxFormField"):
            from spire.doc import CheckBoxFormField
            ret = CheckBoxFormField(intPtr)
        elif (strName == "Spire.Doc.Fields.DropDownFormField"):
            from spire.doc import DropDownFormField
            ret = DropDownFormField(intPtr)
        elif (strName == "Spire.Doc.Fields.ControlField"):
            from spire.doc import ControlField
            ret = ControlField(intPtr)
        elif (strName == "Spire.Doc.Fields.FormField"):
            from spire.doc import FormField
            ret = FormField(intPtr)
        elif (strName == "Spire.Doc.Fields.IfField"):
            from spire.doc import IfField
            ret = IfField(intPtr)
        elif (strName == "Spire.Doc.Fields.MergeField"):
            from spire.doc import MergeField
            ret = MergeField(intPtr)
        elif (strName == "Spire.Doc.Fields.SequenceField"):
            from spire.doc import SequenceField
            ret = SequenceField(intPtr)
        elif (strName == "Spire.Doc.Fields.TextFormField"):
            from spire.doc import TextFormField
            ret = TextFormField(intPtr)
        else:
            from spire.doc import Field
            ret = Field(intPtr)
			
        return ret

    def AppendFieldMark(self ,type:FieldMarkType)->'FieldMark':
        """
    <summary>
        Appends the field mark.
    </summary>
    <param name="type">The type.</param>
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendFieldMark.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_AppendFieldMark.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendFieldMark(self.Ptr, enumtype)
        from spire.doc import FieldMark
        ret = None if intPtr==None else FieldMark(intPtr)
        return ret


    @dispatch

    def AppendHyperlink(self ,link:str,text:str,type:HyperlinkType)->Field:
        """
    <summary>
        Appends the hyperlink.
    </summary>
    <param name="link">The link.</param>
    <param name="text">The text to display.</param>
    <param name="type">The hyperlink type.</param>
    <returns></returns>
        """
        linkPtr = StrToPtr(link)
        textPtr = StrToPtr(text)
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendHyperlink.argtypes=[c_void_p ,c_char_p,c_char_p,c_int]
        GetDllLibDoc().Paragraph_AppendHyperlink.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendHyperlink(self.Ptr, linkPtr,textPtr,enumtype)
        ret = None if intPtr==None else Field(intPtr)
        return ret


    @dispatch

    def AppendHyperlink(self ,link:str,picture:DocPicture,type:HyperlinkType)->Field:
        """
    <summary>
        Appends the hyperlink.
    </summary>
    <param name="link">The link.</param>
    <param name="picture">The picture to display.</param>
    <param name="type">The type of hyperlink.</param>
    <returns></returns>
        """
        linkPtr = StrToPtr(link)
        intPtrpicture:c_void_p = picture.Ptr
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendHyperlinkLPT.argtypes=[c_void_p ,c_char_p,c_void_p,c_int]
        GetDllLibDoc().Paragraph_AppendHyperlinkLPT.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendHyperlinkLPT(self.Ptr, linkPtr,intPtrpicture,enumtype)
        ret = None if intPtr==None else Field(intPtr)
        return ret



    def AppendBookmarkStart(self ,name:str)->'BookmarkStart':
        """
    <summary>
        Appends start of the bookmark with specified name into paragraph.
    </summary>
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().Paragraph_AppendBookmarkStart.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendBookmarkStart.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendBookmarkStart(self.Ptr, namePtr)
        ret = None if intPtr==None else BookmarkStart(intPtr)
        return ret



    def AppendBookmarkEnd(self ,name:str)->'BookmarkEnd':
        """
    <summary>
        Appends end of the bookmark with specified name into paragraph.
    </summary>
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().Paragraph_AppendBookmarkEnd.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendBookmarkEnd.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendBookmarkEnd(self.Ptr, namePtr)
        ret = None if intPtr==None else BookmarkEnd(intPtr)
        return ret



    def AppendPermStart(self ,id:str)->'PermissionStart':
        """
    <summary>
        Appends start of the permission with specified id into paragraph.
    </summary>
        """
        idPtr = StrToPtr(id)
        GetDllLibDoc().Paragraph_AppendPermStart.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendPermStart.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendPermStart(self.Ptr, idPtr)
        ret = None if intPtr==None else PermissionStart(intPtr)
        return ret



    def AppendPermEnd(self ,id:str)->'PermissionEnd':
        """
    <summary>
        Appends end of the permission with specified id into paragraph.
    </summary>
        """
        idPtr = StrToPtr(id)
        GetDllLibDoc().Paragraph_AppendPermEnd.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendPermEnd.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendPermEnd(self.Ptr, idPtr)
        ret = None if intPtr==None else PermissionEnd(intPtr)
        return ret



    def AppendComment(self ,text:str)->'Comment':
        """
    <summary>
        Appends the comment.
    </summary>
    <param name="text">The string.</param>
    <returns>Returns WComment.</returns>
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().Paragraph_AppendComment.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendComment.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendComment(self.Ptr, textPtr)
        from spire.doc import Comment
        ret = None if intPtr==None else Comment(intPtr)
        return ret



    def AppendCommentMark(self ,type:'CommentMarkType')->'CommentMark':
        """
    <summary>
        Appends the comment mark.
    </summary>
    <param name="type">The type.</param>
    <returns>Returns CommentMark.</returns>
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendCommentMark.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_AppendCommentMark.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendCommentMark(self.Ptr, enumtype)
        ret = None if intPtr==None else CommentMark(intPtr)
        return ret


    @dispatch

    def AppendFootnote(self ,type:FootnoteType)->Footnote:
        """
    <summary>
        Appends the footnote.
    </summary>
    <param name="type">The type.</param>
    <returns>returns the footnotes.</returns>
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendFootnote.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_AppendFootnote.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendFootnote(self.Ptr, enumtype)
        ret = None if intPtr==None else Footnote(intPtr)
        return ret


    @dispatch

    def AppendFootnote(self ,type:FootnoteType,bIsAutoNumbered:bool)->Footnote:
        """
    <summary>
        Appends the footnote.
    </summary>
    <param name="type">The type.</param>
    <param name="bIsAutoNumbered">Is auto numbered.</param>
    <returns></returns>
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendFootnoteTB.argtypes=[c_void_p ,c_int,c_bool]
        GetDllLibDoc().Paragraph_AppendFootnoteTB.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendFootnoteTB(self.Ptr, enumtype,bIsAutoNumbered)
        ret = None if intPtr==None else Footnote(intPtr)
        return ret



    def AppendTextBox(self ,width:float,height:float)->'TextBox':
        """
    <summary>
        Append Textbox to the end of the paragraph
    </summary>
    <param name="width">Textbox width</param>
    <param name="height">Textbox height</param>
    <returns></returns>
        """
        
        GetDllLibDoc().Paragraph_AppendTextBox.argtypes=[c_void_p ,c_float,c_float]
        GetDllLibDoc().Paragraph_AppendTextBox.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendTextBox(self.Ptr, width,height)
        from spire.doc import TextBox
        ret = None if intPtr==None else TextBox(intPtr)
        return ret


    @dispatch

    def AppendCheckBox(self)->'CheckBoxFormField':
        """
    <summary>
        Appends the check box form field.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Paragraph_AppendCheckBox.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_AppendCheckBox.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendCheckBox(self.Ptr)
        ret = None if intPtr==None else CheckBoxFormField(intPtr)
        return ret


    @dispatch

    def AppendCheckBox(self ,checkBoxName:str,defaultCheckBoxValue:bool)->'CheckBoxFormField':
        """
    <summary>
        Appends the check box.
    </summary>
    <param name="checkBoxName">Name of the check box.</param>
    <param name="defaultCheckBoxValue">Default checkbox value</param>
    <returns></returns>
        """
        checkBoxNamePtr = StrToPtr(checkBoxName)
        GetDllLibDoc().Paragraph_AppendCheckBoxCD.argtypes=[c_void_p ,c_char_p,c_bool]
        GetDllLibDoc().Paragraph_AppendCheckBoxCD.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendCheckBoxCD(self.Ptr, checkBoxNamePtr,defaultCheckBoxValue)
        ret = None if intPtr==None else CheckBoxFormField(intPtr)
        return ret


    @dispatch

    def AppendTextFormField(self ,defaultText:str)->'TextFormField':
        """
    <summary>
        Appends the text form field.
    </summary>
    <param name="defaultText">The default text. Pass "null" to insert default Word text</param>
    <returns></returns>
        """
        defaultTextPtr = StrToPtr(defaultText)
        GetDllLibDoc().Paragraph_AppendTextFormField.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendTextFormField.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendTextFormField(self.Ptr, defaultTextPtr)
        ret = None if intPtr==None else TextFormField(intPtr)
        return ret


    @dispatch

    def AppendTextFormField(self ,formFieldName:str,defaultText:str)->'TextFormField':
        """
    <summary>
        Appends the text form field.
    </summary>
    <param name="formFieldName">Name of the form field.</param>
    <param name="defaultText">The default text. Pass "null" to insert default Word text</param>
    <returns></returns>
        """
        formFieldNamePtr = StrToPtr(formFieldName)
        defaultTextPtr = StrToPtr(defaultText)
        GetDllLibDoc().Paragraph_AppendTextFormFieldFD.argtypes=[c_void_p ,c_char_p,c_char_p]
        GetDllLibDoc().Paragraph_AppendTextFormFieldFD.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendTextFormFieldFD(self.Ptr, formFieldNamePtr,defaultTextPtr)
        ret = None if intPtr==None else TextFormField(intPtr)
        return ret


    @dispatch

    def AppendDropDownFormField(self)->'DropDownFormField':
        """
    <summary>
        Appends the drop down form field.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Paragraph_AppendDropDownFormField.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_AppendDropDownFormField.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendDropDownFormField(self.Ptr)
        ret = None if intPtr==None else DropDownFormField(intPtr)
        return ret


    @dispatch

    def AppendDropDownFormField(self ,dropDropDownName:str)->'DropDownFormField':
        """
    <summary>
        Appends the drop down form field.
    </summary>
    <param name="dropDropDownName">Name of the drop drop down.</param>
    <returns></returns>
        """
        dropDropDownNamePtr = StrToPtr(dropDropDownName)
        GetDllLibDoc().Paragraph_AppendDropDownFormFieldD.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendDropDownFormFieldD.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendDropDownFormFieldD(self.Ptr, dropDropDownNamePtr)
        ret = None if intPtr==None else DropDownFormField(intPtr)
        return ret



    def AppendSymbol(self ,characterCode:int)->'Symbol':
        """
    <summary>
        Appends special symbol to end of paragraph.
    </summary>
    <param name="characterCode">The character code.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().Paragraph_AppendSymbol.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Paragraph_AppendSymbol.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendSymbol(self.Ptr, characterCode)
        ret = None if intPtr==None else Symbol(intPtr)
        return ret



    def AppendShape(self ,width:float,height:float,shapeType:'ShapeType')->'ShapeObject':
        """
    <summary>
        Append Shape to the end of the paragraph.
    </summary>
    <param name="width">Shape width</param>
    <param name="height">Shape height</param>
    <param name="shapeType">Shape type</param>
    <returns></returns>
        """
        enumshapeType:c_int = shapeType.value

        GetDllLibDoc().Paragraph_AppendShape.argtypes=[c_void_p ,c_float,c_float,c_int]
        GetDllLibDoc().Paragraph_AppendShape.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendShape(self.Ptr, width,height,enumshapeType)
        ret = None if intPtr==None else ShapeObject(intPtr)
        return ret



    def AppendHorizonalLine(self)->'ShapeObject':
        """
    <summary>
        Append Horizonal Line to the end of the paragraph.
    </summary>
        """
        GetDllLibDoc().Paragraph_AppendHorizonalLine.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_AppendHorizonalLine.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendHorizonalLine(self.Ptr)
        ret = None if intPtr==None else ShapeObject(intPtr)
        return ret



    def AppendShapeGroup(self ,width:float,height:float)->'ShapeGroup':
        """
    <summary>
        Append shape Group to the end of the paragraph.
    </summary>
    <param name="width">The width.</param>
    <param name="height">The height.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().Paragraph_AppendShapeGroup.argtypes=[c_void_p ,c_float,c_float]
        GetDllLibDoc().Paragraph_AppendShapeGroup.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendShapeGroup(self.Ptr, width,height)
        from spire.doc import ShapeGroup
        ret = None if intPtr==None else ShapeGroup(intPtr)
        return ret



    def AppendBreak(self ,breakType:'BreakType')->'Break':
        """
    <summary>
        Appends break to end of paragraph.
    </summary>
    <param name="breakType">The break type.</param>
    <returns></returns>
        """
        enumbreakType:c_int = breakType.value

        GetDllLibDoc().Paragraph_AppendBreak.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_AppendBreak.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendBreak(self.Ptr, enumbreakType)
        ret = None if intPtr==None else Break(intPtr)
        return ret



    def AppendTOC(self ,lowerLevel:int,upperLevel:int)->'TableOfContent':
        """
    <summary>
        Appends the table of content.
    </summary>
    <param name="lowerLevel">The starting heading level of the table of content.</param>
    <param name="upperLevel">The ending heading level of the table of content.</param>
    <returns></returns>
        """
        
        GetDllLibDoc().Paragraph_AppendTOC.argtypes=[c_void_p ,c_int,c_int]
        GetDllLibDoc().Paragraph_AppendTOC.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendTOC(self.Ptr, lowerLevel,upperLevel)
        from spire.doc import TableOfContent
        ret = None if intPtr==None else TableOfContent(intPtr)
        return ret


    @dispatch

    def AppendPicture(self ,imgFile:str)->DocPicture:
        """
    <summary>
        Appends the picture.
    </summary>
    <param name="imgFile">The img file.</param>
    <returns>DocPicture.</returns>
        """
        imgFilePtr = StrToPtr(imgFile)
        GetDllLibDoc().Paragraph_AppendPictureI1.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendPictureI1.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendPictureI1(self.Ptr, imgFilePtr)
        from spire.doc import DocPicture
        ret = None if intPtr==None else DocPicture(intPtr)
        return ret


    @dispatch

    def AppendPicture(self ,imgStream:Stream)->DocPicture:
        """
    <summary>
        Appends the picture.
    </summary>
    <param name="imgStream">The img stream.</param>
    <returns>DocPicture.</returns>
        """
        intPtrimgStream:c_void_p = imgStream.Ptr

        GetDllLibDoc().Paragraph_AppendPictureI1.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Paragraph_AppendPictureI1.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendPictureI1(self.Ptr, intPtrimgStream)
        ret = None if intPtr==None else DocPicture(intPtr)
        return ret



    def AppendHTML(self ,html:str):
        """
    <summary>
        Appends the HTML.
    </summary>
    <param name="html">The HTML.</param>
        """
        htmlPtr = StrToPtr(html)
        GetDllLibDoc().Paragraph_AppendHTML.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendHTML(self.Ptr, htmlPtr)

    @dispatch

    def AppendRTF(self ,rtfcode:str,addtolastsection:bool):
        """
    <summary>
        Appends the RTF.
    </summary>
    <param name="rtfcode">the RTF code.</param>
    <param name="addtolastsection">When is true, added to the last section of the document.</param>
        """
        rtfcodePtr = StrToPtr(rtfcode)
        GetDllLibDoc().Paragraph_AppendRTF.argtypes=[c_void_p ,c_char_p,c_bool]
        GetDllLibDoc().Paragraph_AppendRTF(self.Ptr, rtfcodePtr,addtolastsection)

    @dispatch

    def AppendRTF(self ,rtfCode:str):
        """
    <summary>
        Appends the RTF.
    </summary>
    <param name="rtfCode">The RTF code.</param>
        """
        rtfCodePtr = StrToPtr(rtfCode)
        GetDllLibDoc().Paragraph_AppendRTFR.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendRTFR(self.Ptr, rtfCodePtr)

    @dispatch

    def AppendOleObject(self ,oleStream:Stream,olePicture:DocPicture,type:OleObjectType)->DocOleObject:
        """
    <summary>
        Appends the OLE object.
    </summary>
    <param name="oleStorage">The OLE object (file) stream.</param>
    <param name="olePicture">The OLE picture.</param>
    <param name="type">The type of OLE object.</param>
    <returns></returns>
        """
        intPtroleStream:c_void_p = oleStream.Ptr
        intPtrolePicture:c_void_p = olePicture.Ptr
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendOleObject.argtypes=[c_void_p ,c_void_p,c_void_p,c_int]
        GetDllLibDoc().Paragraph_AppendOleObject.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendOleObject(self.Ptr, intPtroleStream,intPtrolePicture,enumtype)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


#    @dispatch
#
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,type:OleObjectType)->DocOleObject:
#        """
#    <summary>
#        Appends the OLE object into paragraph.
#    </summary>
#    <param name="oleBytes">The OLE object (file) bytes.</param>
#    <param name="olePicture">The OLE picture.</param>
#    <param name="type">The type of OLE object.</param>
#    <returns></returns>
#        """
#        #arrayoleBytes:ArrayTypeoleBytes = ""
#        countoleBytes = len(oleBytes)
#        ArrayTypeoleBytes = c_void_p * countoleBytes
#        arrayoleBytes = ArrayTypeoleBytes()
#        for i in range(0, countoleBytes):
#            arrayoleBytes[i] = oleBytes[i].Ptr
#
#        intPtrolePicture:c_void_p = olePicture.Ptr
#        enumtype:c_int = type.value
#
#        GetDllLibDoc().Paragraph_AppendOleObjectOOT.argtypes=[c_void_p ,ArrayTypeoleBytes,c_void_p,c_int]
#        GetDllLibDoc().Paragraph_AppendOleObjectOOT.restype=c_void_p
#        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectOOT(self.Ptr, arrayoleBytes,intPtrolePicture,enumtype)
#        ret = None if intPtr==None else DocOleObject(intPtr)
#        return ret
#


#    @dispatch
#
#    def AppendOleObject(self ,progId:str,clsId:str,nativeData:'Byte[]',olePicture:DocPicture)->DocOleObject:
#        """
#    <summary>
#        Appends the OLE object into paragraph.
#    </summary>
#    <param name="progId">The programmatic identifier.</param>
#    <param name="clsId">The class identifier.</param>
#    <param name="nativeData">The native data of embedded OLE object.</param>
#    <param name="olePicture">The OLE picture.</param>
#    <returns></returns>
#        """
#        #arraynativeData:ArrayTypenativeData = ""
#        countnativeData = len(nativeData)
#        ArrayTypenativeData = c_void_p * countnativeData
#        arraynativeData = ArrayTypenativeData()
#        for i in range(0, countnativeData):
#            arraynativeData[i] = nativeData[i].Ptr
#
#        intPtrolePicture:c_void_p = olePicture.Ptr
#
#        GetDllLibDoc().Paragraph_AppendOleObjectPCNO.argtypes=[c_void_p ,c_wchar_p,c_wchar_p,ArrayTypenativeData,c_void_p]
#        GetDllLibDoc().Paragraph_AppendOleObjectPCNO.restype=c_void_p
#        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectPCNO(self.Ptr, progId,clsId,arraynativeData,intPtrolePicture)
#        ret = None if intPtr==None else DocOleObject(intPtr)
#        return ret
#


    @dispatch

    def AppendOleObject(self ,pathToFile:str,olePicture:DocPicture,type:OleObjectType)->DocOleObject:
        """
    <summary>
        Appends the OLE object into paragraph.
    </summary>
    <param name="pathToFile">The path to file.</param>
    <param name="olePicture">The OLE picture.</param>
    <param name="type">The type of OLE object.</param>
    <returns></returns>
        """
        pathToFilePtr = StrToPtr(pathToFile)
        intPtrolePicture:c_void_p = olePicture.Ptr
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendOleObjectPOT.argtypes=[c_void_p ,c_char_p,c_void_p,c_int]
        GetDllLibDoc().Paragraph_AppendOleObjectPOT.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectPOT(self.Ptr, pathToFilePtr,intPtrolePicture,enumtype)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


    @dispatch

    def AppendOleObject(self ,pathToFile:str,olePicture:DocPicture)->DocOleObject:
        """
    <summary>
        Appends the OLE object.
    </summary>
    <param name="pathToFile">The path to file.</param>
    <param name="olePicture">The OLE picture.</param>
    <returns></returns>
        """
        pathToFilePtr = StrToPtr(pathToFile)
        intPtrolePicture:c_void_p = olePicture.Ptr

        GetDllLibDoc().Paragraph_AppendOleObjectPO.argtypes=[c_void_p ,c_char_p,c_void_p]
        GetDllLibDoc().Paragraph_AppendOleObjectPO.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectPO(self.Ptr, pathToFilePtr,intPtrolePicture)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


    @dispatch

    def AppendOleObject(self ,oleStream:Stream,olePicture:DocPicture,oleLinkType:OleLinkType)->DocOleObject:
        """
    <summary>
        Appends the OLE object into paragraph.
    </summary>
    <param name="oleStorage">The OLE storage.</param>
    <param name="olePicture">The OLE picture.</param>
    <param name="oleLinkType">The type of OLE object link type.</param>
    <returns></returns>
        """
        intPtroleStream:c_void_p = oleStream.Ptr
        intPtrolePicture:c_void_p = olePicture.Ptr
        enumoleLinkType:c_int = oleLinkType.value

        GetDllLibDoc().Paragraph_AppendOleObjectOOO.argtypes=[c_void_p ,c_void_p,c_void_p,c_int]
        GetDllLibDoc().Paragraph_AppendOleObjectOOO.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectOOO(self.Ptr, intPtroleStream,intPtrolePicture,enumoleLinkType)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


#    @dispatch
#
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,oleLinkType:OleLinkType)->DocOleObject:
#        """
#    <summary>
#        Appends the OLE object.
#    </summary>
#    <param name="oleBytes">The OLE storage bytes.</param>
#    <param name="olePicture">The OLE picture.</param>
#    <param name="oleLinkType">Type of the OLE link.</param>
#    <returns></returns>
#        """
#        #arrayoleBytes:ArrayTypeoleBytes = ""
#        countoleBytes = len(oleBytes)
#        ArrayTypeoleBytes = c_void_p * countoleBytes
#        arrayoleBytes = ArrayTypeoleBytes()
#        for i in range(0, countoleBytes):
#            arrayoleBytes[i] = oleBytes[i].Ptr
#
#        intPtrolePicture:c_void_p = olePicture.Ptr
#        enumoleLinkType:c_int = oleLinkType.value
#
#        GetDllLibDoc().Paragraph_AppendOleObjectOOO1.argtypes=[c_void_p ,ArrayTypeoleBytes,c_void_p,c_int]
#        GetDllLibDoc().Paragraph_AppendOleObjectOOO1.restype=c_void_p
#        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectOOO1(self.Ptr, arrayoleBytes,intPtrolePicture,enumoleLinkType)
#        ret = None if intPtr==None else DocOleObject(intPtr)
#        return ret
#


    @dispatch

    def AppendOleObject(self ,linkFile:str,olePicture:DocPicture,oleLinkType:OleLinkType)->DocOleObject:
        """
    <summary>
        Appends the OLE object.
    </summary>
    <param name="linkFile">The link file. </param>
    <param name="olePicture">The OLE picture.</param>
    <param name="oleLinkType">Type of the OLE link.</param>
    <returns></returns>
        """
        linkFilePtr = StrToPtr(linkFile)
        intPtrolePicture:c_void_p = olePicture.Ptr
        enumoleLinkType:c_int = oleLinkType.value

        GetDllLibDoc().Paragraph_AppendOleObjectLOO.argtypes=[c_void_p ,c_char_p,c_void_p,c_int]
        GetDllLibDoc().Paragraph_AppendOleObjectLOO.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectLOO(self.Ptr, linkFilePtr,intPtrolePicture,enumoleLinkType)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


#    @dispatch
#
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,fileExtension:str)->DocOleObject:
#        """
#    <summary>
#        Appends the package OLE object (ole object without specified type).
#    </summary>
#    <param name="oleBytes">The OLE object bytes.</param>
#    <param name="olePicture">The OLE picture.</param>
#    <param name="fileExtension">The file extension.</param>
#    <returns></returns>
#        """
#        #arrayoleBytes:ArrayTypeoleBytes = ""
#        countoleBytes = len(oleBytes)
#        ArrayTypeoleBytes = c_void_p * countoleBytes
#        arrayoleBytes = ArrayTypeoleBytes()
#        for i in range(0, countoleBytes):
#            arrayoleBytes[i] = oleBytes[i].Ptr
#
#        intPtrolePicture:c_void_p = olePicture.Ptr
#
#        GetDllLibDoc().Paragraph_AppendOleObjectOOF.argtypes=[c_void_p ,ArrayTypeoleBytes,c_void_p,c_wchar_p]
#        GetDllLibDoc().Paragraph_AppendOleObjectOOF.restype=c_void_p
#        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectOOF(self.Ptr, arrayoleBytes,intPtrolePicture,fileExtension)
#        ret = None if intPtr==None else DocOleObject(intPtr)
#        return ret
#


    @dispatch

    def AppendOleObject(self ,oleStream:Stream,olePicture:DocPicture,fileExtension:str)->DocOleObject:
        """
    <summary>
        Appends the package OLE object (ole object without specified type).
    </summary>
    <param name="oleStream">The OLE file stream.</param>
    <param name="olePicture">The OLE picture.</param>
    <param name="fileExtension">The file extension.</param>
    <returns></returns>
        """
        fileExtensionPtr = StrToPtr(fileExtension)
        intPtroleStream:c_void_p = oleStream.Ptr
        intPtrolePicture:c_void_p = olePicture.Ptr

        GetDllLibDoc().Paragraph_AppendOleObjectOOF1.argtypes=[c_void_p ,c_void_p,c_void_p,c_char_p]
        GetDllLibDoc().Paragraph_AppendOleObjectOOF1.restype=c_void_p
        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectOOF1(self.Ptr, intPtroleStream,intPtrolePicture,fileExtensionPtr)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


    def RemoveFrame(self):
        """
    <summary>
        Remove a frame.
    </summary>
        """
        GetDllLibDoc().Paragraph_RemoveFrame.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_RemoveFrame(self.Ptr)

