from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class StructureDocumentTagInline (  ParagraphBase, IStructureDocument, ICompositeObject) :
    """

    """
    @dispatch
    def __init__(self, doc:Document):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().StructureDocumentTagInline_CreateStructureDocumentTagInlineD.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_CreateStructureDocumentTagInlineD.restype=c_void_p
        intPtr = GetDllLibDoc().StructureDocumentTagInline_CreateStructureDocumentTagInlineD(intPdoc)
        super(StructureDocumentTagInline, self).__init__(intPtr)

    @property

    def SDTContent(self)->'SDTInlineContent':
        """
    <summary>
        Gets a valie specifies the last known contents of a structured document tag around one or more inline-level structures.
    </summary>
        """
        GetDllLibDoc().StructureDocumentTagInline_get_SDTContent.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_get_SDTContent.restype=c_void_p
        intPtr = GetDllLibDoc().StructureDocumentTagInline_get_SDTContent(self.Ptr)
        ret = None if intPtr==None else SDTInlineContent(intPtr)
        return ret


    @property

    def SDTProperties(self)->'SDTProperties':
        """
    <summary>
        Gets the structured document tag properties.
    </summary>
        """
        GetDllLibDoc().StructureDocumentTagInline_get_SDTProperties.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_get_SDTProperties.restype=c_void_p
        intPtr = GetDllLibDoc().StructureDocumentTagInline_get_SDTProperties(self.Ptr)
        ret = None if intPtr==None else SDTProperties(intPtr)
        return ret


    @property

    def BreakCharacterFormat(self)->'CharacterFormat':
        """
    <summary>
        Gets character format for the break symbol.
    </summary>
        """
        GetDllLibDoc().StructureDocumentTagInline_get_BreakCharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_get_BreakCharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().StructureDocumentTagInline_get_BreakCharacterFormat(self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the entity.
    </summary>
<value>The type of the entity.</value>
        """
        GetDllLibDoc().StructureDocumentTagInline_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().StructureDocumentTagInline_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
    <summary>
        Gets the child entities.
    </summary>
<value>The child entities.</value>
        """
        GetDllLibDoc().StructureDocumentTagInline_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().StructureDocumentTagInline_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    def BackupChildObjects(self):
        """

        """
        GetDllLibDoc().StructureDocumentTagInline_BackupChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_BackupChildObjects(self.Ptr)

    def RevertChildObjects(self):
        """

        """
        GetDllLibDoc().StructureDocumentTagInline_RevertChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_RevertChildObjects(self.Ptr)


    def MakeChanges(self ,acceptChanges:bool):
        """

        """
        
        GetDllLibDoc().StructureDocumentTagInline_MakeChanges.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().StructureDocumentTagInline_MakeChanges(self.Ptr, acceptChanges)

    def UpdateDataBinding(self):
        """

        """
        GetDllLibDoc().StructureDocumentTagInline_UpdateDataBinding.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_UpdateDataBinding(self.Ptr)

