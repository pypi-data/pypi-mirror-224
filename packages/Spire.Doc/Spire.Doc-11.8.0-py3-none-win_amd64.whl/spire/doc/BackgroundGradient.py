from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BackgroundGradient (  VMLFill) :
    """

    """
    @property

    def Color1(self)->'Color':
        """
    <summary>
        Gets or sets first color for gradient.
    </summary>
        """
        GetDllLibDoc().BackgroundGradient_get_Color1.argtypes=[c_void_p]
        GetDllLibDoc().BackgroundGradient_get_Color1.restype=c_void_p
        intPtr = GetDllLibDoc().BackgroundGradient_get_Color1(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @Color1.setter
    def Color1(self, value:'Color'):
        GetDllLibDoc().BackgroundGradient_set_Color1.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().BackgroundGradient_set_Color1(self.Ptr, value.Ptr)

    @property

    def Color2(self)->'Color':
        """
    <summary>
        Gets or sets second color for gradient
            (used when TwoColors set to true).
    </summary>
        """
        GetDllLibDoc().BackgroundGradient_get_Color2.argtypes=[c_void_p]
        GetDllLibDoc().BackgroundGradient_get_Color2.restype=c_void_p
        intPtr = GetDllLibDoc().BackgroundGradient_get_Color2(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @Color2.setter
    def Color2(self, value:'Color'):
        GetDllLibDoc().BackgroundGradient_set_Color2.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().BackgroundGradient_set_Color2(self.Ptr, value.Ptr)

    @property

    def ShadingStyle(self)->'GradientShadingStyle':
        """
    <summary>
        Gets or sets shading style for gradient.
    </summary>
        """
        GetDllLibDoc().BackgroundGradient_get_ShadingStyle.argtypes=[c_void_p]
        GetDllLibDoc().BackgroundGradient_get_ShadingStyle.restype=c_int
        ret = GetDllLibDoc().BackgroundGradient_get_ShadingStyle(self.Ptr)
        objwraped = GradientShadingStyle(ret)
        return objwraped

    @ShadingStyle.setter
    def ShadingStyle(self, value:'GradientShadingStyle'):
        GetDllLibDoc().BackgroundGradient_set_ShadingStyle.argtypes=[c_void_p, c_int]
        GetDllLibDoc().BackgroundGradient_set_ShadingStyle(self.Ptr, value.value)

    @property

    def ShadingVariant(self)->'GradientShadingVariant':
        """
    <summary>
        Gets or sets shading variants.
    </summary>
        """
        GetDllLibDoc().BackgroundGradient_get_ShadingVariant.argtypes=[c_void_p]
        GetDllLibDoc().BackgroundGradient_get_ShadingVariant.restype=c_int
        ret = GetDllLibDoc().BackgroundGradient_get_ShadingVariant(self.Ptr)
        objwraped = GradientShadingVariant(ret)
        return objwraped

    @ShadingVariant.setter
    def ShadingVariant(self, value:'GradientShadingVariant'):
        GetDllLibDoc().BackgroundGradient_set_ShadingVariant.argtypes=[c_void_p, c_int]
        GetDllLibDoc().BackgroundGradient_set_ShadingVariant(self.Ptr, value.value)

