from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class OfficeMath (  ParagraphBase, ICompositeObject) :
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
        GetDllLibDoc().OfficeMath_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().OfficeMath_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().OfficeMath_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def ParentParagraph(self)->'Paragraph':
        """
    <summary>
        Gets the parent paragraph.
    </summary>
<value>The parent paragraph.</value>
        """
        GetDllLibDoc().OfficeMath_get_ParentParagraph.argtypes=[c_void_p]
        GetDllLibDoc().OfficeMath_get_ParentParagraph.restype=c_void_p
        intPtr = GetDllLibDoc().OfficeMath_get_ParentParagraph(self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret



    def FromMathMLCode(self ,mathMLCode:str):
        """
    <summary>
        Froms the mathML code.
    </summary>
    <param name="mathMLCode">The Math ML code.</param>
        """
        mathMLCodePtr = StrToPtr(mathMLCode)
        GetDllLibDoc().OfficeMath_FromMathMLCode.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().OfficeMath_FromMathMLCode(self.Ptr, mathMLCodePtr)


    def FromLatexMathCode(self ,latexMathCode:str):
        """
    <summary>
        Froms the latex math code.
    </summary>
    <param name="latexMathCode">The latex math code.</param>
        """
        latexMathCodePtr = StrToPtr(latexMathCode)
        GetDllLibDoc().OfficeMath_FromLatexMathCode.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().OfficeMath_FromLatexMathCode(self.Ptr, latexMathCodePtr)

#
#    def SaveAsImage(self ,imageType:'ImageType')->'SKImage':
#        """
#    <summary>
#        Save the OfficeMath object as Image
#    </summary>
#        """
#        enumimageType:c_int = imageType.value
#
#        GetDllLibDoc().OfficeMath_SaveAsImage.argtypes=[c_void_p ,c_int]
#        GetDllLibDoc().OfficeMath_SaveAsImage.restype=c_void_p
#        intPtr = GetDllLibDoc().OfficeMath_SaveAsImage(self.Ptr, enumimageType)
#        ret = None if intPtr==None else SKImage(intPtr)
#        return ret
#



    def ToMathMLCode(self)->str:
        """
    <summary>
        To the mathML code.
    </summary>
    <returns>System.String.</returns>
        """
        GetDllLibDoc().OfficeMath_ToMathMLCode.argtypes=[c_void_p]
        GetDllLibDoc().OfficeMath_ToMathMLCode.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().OfficeMath_ToMathMLCode(self.Ptr))
        return ret


    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """

        """
        GetDllLibDoc().OfficeMath_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().OfficeMath_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().OfficeMath_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


