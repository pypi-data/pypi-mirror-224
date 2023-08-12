from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ShapeObject (  Shape, IDocumentObject) :
    """

    """
    @dispatch
    def __init__(self, doc:'IDocument'):
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().ShapeObject_CreateShapeObjectD.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_CreateShapeObjectD.restype=c_void_p
        intPtr = GetDllLibDoc().ShapeObject_CreateShapeObjectD(intPdoc)
        super(ShapeObject, self).__init__(intPtr)

    @dispatch
    def __init__(self, doc:'IDocument', shapeType:ShapeType):
        intPdoc:c_void_p =  doc.Ptr
        iTypeshapeType:c_int = shapeType.value

        GetDllLibDoc().ShapeObject_CreateShapeObjectDS.argtypes = [c_void_p,c_int]
        GetDllLibDoc().ShapeObject_CreateShapeObjectDS.restype = c_void_p
        intPtr = GetDllLibDoc().ShapeObject_CreateShapeObjectDS(intPdoc,iTypeshapeType)
        super(ShapeObject, self).__init__(intPtr)

    @property

    def Chart(self)->'Chart':
        """
    <summary>
        Returns a chart object.
            If there is a chart associated with this shape,
            it allows for the manipulation of chart.
    </summary>
        """
        GetDllLibDoc().ShapeObject_get_Chart.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_Chart.restype=c_void_p
        intPtr = GetDllLibDoc().ShapeObject_get_Chart(self.Ptr)
        ret = None if intPtr==None else Chart(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
<value>The type of the document object.</value>
        """
        GetDllLibDoc().ShapeObject_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().ShapeObject_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
    <summary>
        Gets shape object's character format.
    </summary>
        """
        GetDllLibDoc().ShapeObject_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_CharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().ShapeObject_get_CharacterFormat(self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def FillColor(self)->'Color':
        """

        """
        GetDllLibDoc().ShapeObject_get_FillColor.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_FillColor.restype=c_void_p
        intPtr = GetDllLibDoc().ShapeObject_get_FillColor(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @FillColor.setter
    def FillColor(self, value:'Color'):
        GetDllLibDoc().ShapeObject_set_FillColor.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().ShapeObject_set_FillColor(self.Ptr, value.Ptr)

    #@FillTransparency.setter
    def FillTransparency(self, value:float):
        GetDllLibDoc().ShapeObject_set_FillTransparency.argtypes=[c_void_p, c_double]
        GetDllLibDoc().ShapeObject_set_FillTransparency(self.Ptr, value)

    @property
    def StrokeWeight(self)->float:
        """

        """
        GetDllLibDoc().ShapeObject_get_StrokeWeight.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_StrokeWeight.restype=c_double
        ret = GetDllLibDoc().ShapeObject_get_StrokeWeight(self.Ptr)
        return ret

    @StrokeWeight.setter
    def StrokeWeight(self, value:float):
        GetDllLibDoc().ShapeObject_set_StrokeWeight.argtypes=[c_void_p, c_double]
        GetDllLibDoc().ShapeObject_set_StrokeWeight(self.Ptr, value)

    @property

    def StrokeColor(self)->'Color':
        """

        """
        GetDllLibDoc().ShapeObject_get_StrokeColor.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_StrokeColor.restype=c_void_p
        intPtr = GetDllLibDoc().ShapeObject_get_StrokeColor(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @StrokeColor.setter
    def StrokeColor(self, value:'Color'):
        GetDllLibDoc().ShapeObject_set_StrokeColor.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().ShapeObject_set_StrokeColor(self.Ptr, value.Ptr)

    @property

    def LineStyle(self)->'ShapeLineStyle':
        """

        """
        GetDllLibDoc().ShapeObject_get_LineStyle.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_LineStyle.restype=c_int
        ret = GetDllLibDoc().ShapeObject_get_LineStyle(self.Ptr)
        objwraped = ShapeLineStyle(ret)
        return objwraped

    @LineStyle.setter
    def LineStyle(self, value:'ShapeLineStyle'):
        GetDllLibDoc().ShapeObject_set_LineStyle.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ShapeObject_set_LineStyle(self.Ptr, value.value)

    @property

    def LineDashing(self)->'LineDashing':
        """
    <summary>
        Defines the line dashing of the stroke.
    </summary>
        """
        GetDllLibDoc().ShapeObject_get_LineDashing.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_LineDashing.restype=c_int
        ret = GetDllLibDoc().ShapeObject_get_LineDashing(self.Ptr)
        objwraped = LineDashing(ret)
        return objwraped

    @LineDashing.setter
    def LineDashing(self, value:'LineDashing'):
        GetDllLibDoc().ShapeObject_set_LineDashing.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ShapeObject_set_LineDashing(self.Ptr, value.value)

    @property

    def WordArt(self)->'WordArt':
        """

        """
        GetDllLibDoc().ShapeObject_get_WordArt.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_WordArt.restype=c_void_p
        intPtr = GetDllLibDoc().ShapeObject_get_WordArt(self.Ptr)
        from spire.doc import WordArt
        ret = None if intPtr==None else WordArt(intPtr)
        return ret


    @property
    def ExtrusionEnabled(self)->bool:
        """

        """
        GetDllLibDoc().ShapeObject_get_ExtrusionEnabled.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_ExtrusionEnabled.restype=c_bool
        ret = GetDllLibDoc().ShapeObject_get_ExtrusionEnabled(self.Ptr)
        return ret

    @property
    def ShadowEnabled(self)->bool:
        """

        """
        GetDllLibDoc().ShapeObject_get_ShadowEnabled.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_ShadowEnabled.restype=c_bool
        ret = GetDllLibDoc().ShapeObject_get_ShadowEnabled(self.Ptr)
        return ret

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
    <summary>
        Gets the child objects of the entity.
    </summary>
        """
        GetDllLibDoc().ShapeObject_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().ShapeObject_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


