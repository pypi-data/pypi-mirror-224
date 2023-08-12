from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListLevel (  DocumentSerializable) :
    """

    """
    @property

    def NumberAlignment(self)->'ListNumberAlignment':
        """

        """
        GetDllLibDoc().ListLevel_get_NumberAlignment.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_NumberAlignment.restype=c_int
        ret = GetDllLibDoc().ListLevel_get_NumberAlignment(self.Ptr)
        objwraped = ListNumberAlignment(ret)
        return objwraped

    @NumberAlignment.setter
    def NumberAlignment(self, value:'ListNumberAlignment'):
        GetDllLibDoc().ListLevel_set_NumberAlignment.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ListLevel_set_NumberAlignment(self.Ptr, value.value)

    @property
    def StartAt(self)->int:
        """

        """
        GetDllLibDoc().ListLevel_get_StartAt.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_StartAt.restype=c_int
        ret = GetDllLibDoc().ListLevel_get_StartAt(self.Ptr)
        return ret

    @StartAt.setter
    def StartAt(self, value:int):
        GetDllLibDoc().ListLevel_set_StartAt.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ListLevel_set_StartAt(self.Ptr, value)

    @property
    def TabSpaceAfter(self)->float:
        """

        """
        GetDllLibDoc().ListLevel_get_TabSpaceAfter.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_TabSpaceAfter.restype=c_float
        ret = GetDllLibDoc().ListLevel_get_TabSpaceAfter(self.Ptr)
        return ret

    @TabSpaceAfter.setter
    def TabSpaceAfter(self, value:float):
        GetDllLibDoc().ListLevel_set_TabSpaceAfter.argtypes=[c_void_p, c_float]
        GetDllLibDoc().ListLevel_set_TabSpaceAfter(self.Ptr, value)

    @property
    def TextPosition(self)->float:
        """

        """
        GetDllLibDoc().ListLevel_get_TextPosition.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_TextPosition.restype=c_float
        ret = GetDllLibDoc().ListLevel_get_TextPosition(self.Ptr)
        return ret

    @TextPosition.setter
    def TextPosition(self, value:float):
        GetDllLibDoc().ListLevel_set_TextPosition.argtypes=[c_void_p, c_float]
        GetDllLibDoc().ListLevel_set_TextPosition(self.Ptr, value)

    @property

    def NumberPrefix(self)->str:
        """

        """
        GetDllLibDoc().ListLevel_get_NumberPrefix.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_NumberPrefix.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().ListLevel_get_NumberPrefix(self.Ptr))
        return ret


    @NumberPrefix.setter
    def NumberPrefix(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().ListLevel_set_NumberPrefix.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().ListLevel_set_NumberPrefix(self.Ptr, valuePtr)

    @property

    def NumberSufix(self)->str:
        """
    <summary>
        Gets or sets suffix pattern for numbered level.
    </summary>
        """
        GetDllLibDoc().ListLevel_get_NumberSufix.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_NumberSufix.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().ListLevel_get_NumberSufix(self.Ptr))
        return ret


    @NumberSufix.setter
    def NumberSufix(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().ListLevel_set_NumberSufix.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().ListLevel_set_NumberSufix(self.Ptr, valuePtr)

    @property

    def BulletCharacter(self)->str:
        """

        """
        GetDllLibDoc().ListLevel_get_BulletCharacter.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_BulletCharacter.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().ListLevel_get_BulletCharacter(self.Ptr))
        return ret


    @BulletCharacter.setter
    def BulletCharacter(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().ListLevel_set_BulletCharacter.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().ListLevel_set_BulletCharacter(self.Ptr, valuePtr)

    @property

    def PatternType(self)->'ListPatternType':
        """
    <summary>
        Gets or sets list numbering type.
    </summary>
        """
        GetDllLibDoc().ListLevel_get_PatternType.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_PatternType.restype=c_int
        ret = GetDllLibDoc().ListLevel_get_PatternType(self.Ptr)
        objwraped = ListPatternType(ret)
        return objwraped

    @PatternType.setter
    def PatternType(self, value:'ListPatternType'):
        GetDllLibDoc().ListLevel_set_PatternType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ListLevel_set_PatternType(self.Ptr, value.value)

    @property
    def NoRestartByHigher(self)->bool:
        """

        """
        GetDllLibDoc().ListLevel_get_NoRestartByHigher.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_NoRestartByHigher.restype=c_bool
        ret = GetDllLibDoc().ListLevel_get_NoRestartByHigher(self.Ptr)
        return ret

    @NoRestartByHigher.setter
    def NoRestartByHigher(self, value:bool):
        GetDllLibDoc().ListLevel_set_NoRestartByHigher.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ListLevel_set_NoRestartByHigher(self.Ptr, value)

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
    <summary>
        Gets character format of list symbol.
    </summary>
        """
        GetDllLibDoc().ListLevel_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_CharacterFormat.restype=c_void_p
        intPtr = GetDllLibDoc().ListLevel_get_CharacterFormat(self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def ParagraphFormat(self)->'ParagraphFormat':
        """
    <summary>
        Gets paragraph format of list level.
    </summary>
        """
        GetDllLibDoc().ListLevel_get_ParagraphFormat.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_ParagraphFormat.restype=c_void_p
        intPtr = GetDllLibDoc().ListLevel_get_ParagraphFormat(self.Ptr)
        ret = None if intPtr==None else ParagraphFormat(intPtr)
        return ret


    @property

    def FollowCharacter(self)->'FollowCharacterType':
        """
    <summary>
        Gets or Sets the type of character following the number text for the paragraph.
    </summary>
        """
        GetDllLibDoc().ListLevel_get_FollowCharacter.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_FollowCharacter.restype=c_int
        ret = GetDllLibDoc().ListLevel_get_FollowCharacter(self.Ptr)
        objwraped = FollowCharacterType(ret)
        return objwraped

    @FollowCharacter.setter
    def FollowCharacter(self, value:'FollowCharacterType'):
        GetDllLibDoc().ListLevel_set_FollowCharacter.argtypes=[c_void_p, c_int]
        GetDllLibDoc().ListLevel_set_FollowCharacter(self.Ptr, value.value)

    @property
    def IsLegalStyleNumbering(self)->bool:
        """

        """
        GetDllLibDoc().ListLevel_get_IsLegalStyleNumbering.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_IsLegalStyleNumbering.restype=c_bool
        ret = GetDllLibDoc().ListLevel_get_IsLegalStyleNumbering(self.Ptr)
        return ret

    @IsLegalStyleNumbering.setter
    def IsLegalStyleNumbering(self, value:bool):
        GetDllLibDoc().ListLevel_set_IsLegalStyleNumbering.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ListLevel_set_IsLegalStyleNumbering(self.Ptr, value)

    @property
    def NumberPosition(self)->float:
        """

        """
        GetDllLibDoc().ListLevel_get_NumberPosition.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_NumberPosition.restype=c_float
        ret = GetDllLibDoc().ListLevel_get_NumberPosition(self.Ptr)
        return ret

    @NumberPosition.setter
    def NumberPosition(self, value:float):
        GetDllLibDoc().ListLevel_set_NumberPosition.argtypes=[c_void_p, c_float]
        GetDllLibDoc().ListLevel_set_NumberPosition(self.Ptr, value)

    @property
    def UsePrevLevelPattern(self)->bool:
        """

        """
        GetDllLibDoc().ListLevel_get_UsePrevLevelPattern.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_UsePrevLevelPattern.restype=c_bool
        ret = GetDllLibDoc().ListLevel_get_UsePrevLevelPattern(self.Ptr)
        return ret

    @UsePrevLevelPattern.setter
    def UsePrevLevelPattern(self, value:bool):
        GetDllLibDoc().ListLevel_set_UsePrevLevelPattern.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().ListLevel_set_UsePrevLevelPattern(self.Ptr, value)


    def GetListItemText(self ,listItemIndex:int,listType:'ListType')->str:
        """

        """
        enumlistType:c_int = listType.value

        GetDllLibDoc().ListLevel_GetListItemText.argtypes=[c_void_p ,c_int,c_int]
        GetDllLibDoc().ListLevel_GetListItemText.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().ListLevel_GetListItemText(self.Ptr, listItemIndex,enumlistType))
        return ret



    def Clone(self)->'ListLevel':
        """

        """
        GetDllLibDoc().ListLevel_Clone.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().ListLevel_Clone(self.Ptr)
        ret = None if intPtr==None else ListLevel(intPtr)
        return ret


