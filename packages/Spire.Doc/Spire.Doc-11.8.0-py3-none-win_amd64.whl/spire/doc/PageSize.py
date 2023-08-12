from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PageSize (SpireObject) :
    """

    """
    @staticmethod

    def A3()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_A3.argtypes=[]
        GetDllLibDoc().PageSize_A3.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_A3()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def A4()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_A4.argtypes=[]
        GetDllLibDoc().PageSize_A4.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_A4()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def A5()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_A5.argtypes=[]
        GetDllLibDoc().PageSize_A5.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_A5()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def A6()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_A6.argtypes=[]
        GetDllLibDoc().PageSize_A6.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_A6()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def B4()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_B4.argtypes=[]
        GetDllLibDoc().PageSize_B4.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_B4()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def B5()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_B5.argtypes=[]
        GetDllLibDoc().PageSize_B5.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_B5()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def B6()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_B6.argtypes=[]
        GetDllLibDoc().PageSize_B6.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_B6()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def Letter()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_Letter.argtypes=[]
        GetDllLibDoc().PageSize_Letter.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_Letter()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def HalfLetter()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_HalfLetter.argtypes=[]
        GetDllLibDoc().PageSize_HalfLetter.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_HalfLetter()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def Letter11x17()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_Letter11x17.argtypes=[]
        GetDllLibDoc().PageSize_Letter11x17.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_Letter11x17()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def EnvelopeDL()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_EnvelopeDL.argtypes=[]
        GetDllLibDoc().PageSize_EnvelopeDL.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_EnvelopeDL()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def Quarto()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_Quarto.argtypes=[]
        GetDllLibDoc().PageSize_Quarto.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_Quarto()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def Statement()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_Statement.argtypes=[]
        GetDllLibDoc().PageSize_Statement.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_Statement()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def Ledger()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_Ledger.argtypes=[]
        GetDllLibDoc().PageSize_Ledger.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_Ledger()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def Tabloid()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_Tabloid.argtypes=[]
        GetDllLibDoc().PageSize_Tabloid.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_Tabloid()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def Note()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_Note.argtypes=[]
        GetDllLibDoc().PageSize_Note.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_Note()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def Legal()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_Legal.argtypes=[]
        GetDllLibDoc().PageSize_Legal.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_Legal()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def Flsa()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_Flsa.argtypes=[]
        GetDllLibDoc().PageSize_Flsa.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_Flsa()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def Executive()->'SizeF':
        """

        """
        #GetDllLibDoc().PageSize_Executive.argtypes=[]
        GetDllLibDoc().PageSize_Executive.restype=c_void_p
        intPtr = GetDllLibDoc().PageSize_Executive()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


