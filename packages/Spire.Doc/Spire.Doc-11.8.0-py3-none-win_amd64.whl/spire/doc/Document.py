from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Document (  DocumentContainer, IDocument, ICompositeObject) :
    """

    """

    @dispatch
    def __init__(self, stream:Stream, password:str, useNewEngine:bool):
        passwordPtr = StrToPtr(password)
        intPstream:c_void_p = stream.Ptr;

        GetDllLibDoc().Document_CreateDocumentSPU.argtypes=[c_void_p,c_char_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentSPU.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentSPU(intPstream,passwordPtr,useNewEngine)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, stream:Stream, fileFormat:FileFormat, password:str):
        passwordPtr = StrToPtr(password)
        intPstream:c_void_p = stream.Ptr;
        iTypetype:c_int = fileFormat.value;

        GetDllLibDoc().Document_CreateDocumentSTP.argtypes=[c_void_p,c_int,c_char_p]
        GetDllLibDoc().Document_CreateDocumentSTP.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentSTP(intPstream,iTypetype,passwordPtr)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, stream:Stream, fileFormat:FileFormat, password:str, useNewEngine:bool):
        passwordPtr = StrToPtr(password)
        intPstream:c_void_p = stream.Ptr;
        iTypetype:c_int = fileFormat.value;

        GetDllLibDoc().Document_CreateDocumentSTPU.argtypes=[c_void_p,c_int,c_char_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentSTPU.restype=c_void_p
        intPtr =GetDllLibDoc().Document_CreateDocumentSTPU(intPstream,iTypetype,passwordPtr,useNewEngine)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str):
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_CreateDocumentF.argtypes=[c_char_p]
        GetDllLibDoc().Document_CreateDocumentF.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentF(fileNamePtr)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str, useNewEngine:bool):
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_CreateDocumentFU.argtypes=[c_char_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentFU.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentFU(fileNamePtr,useNewEngine)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str, password:str):
        fileNamePtr = StrToPtr(fileName)
        passwordPtr = StrToPtr(password)
        GetDllLibDoc().Document_CreateDocumentFP.argtypes=[c_char_p,c_char_p]
        GetDllLibDoc().Document_CreateDocumentFP.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentFP(fileNamePtr,passwordPtr)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str, password:str, useNewEngine:bool):

        fileNamePtr = StrToPtr(fileName)
        passwordPtr = StrToPtr(password)
        GetDllLibDoc().Document_CreateDocumentFPU.argtypes=[c_char_p,c_char_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentFPU.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentFPU(fileNamePtr,passwordPtr,useNewEngine)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat):
        fileNamePtr = StrToPtr(fileName)
        iTypetype:c_int = fileFormat.value

        GetDllLibDoc().Document_CreateDocumentFT.argtypes=[c_char_p,c_int]
        GetDllLibDoc().Document_CreateDocumentFT.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentFT(fileNamePtr,iTypetype)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat, useNewEngine:bool):

        fileNamePtr = StrToPtr(fileName)
        iTypetype:c_int = fileFormat.value

        GetDllLibDoc().Document_CreateDocumentFTU.argtypes=[c_char_p,c_int,c_bool]
        GetDllLibDoc().Document_CreateDocumentFTU.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentFTU(fileNamePtr,iTypetype,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat, validationType:XHTMLValidationType):

        fileNamePtr = StrToPtr(fileName)
        iTypetype:c_int = fileFormat.value
        iTypevalidationType:c_int = validationType.value

        GetDllLibDoc().Document_CreateDocumentFTV.argtypes=[c_char_p,c_int,c_int]
        GetDllLibDoc().Document_CreateDocumentFTV.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentFTV(fileNamePtr,iTypetype,iTypevalidationType)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat, validationType:XHTMLValidationType, useNewEngine:bool):

        fileNamePtr = StrToPtr(fileName)
        iTypetype:c_int = fileFormat.value
        iTypevalidationType:c_int = validationType.value

        GetDllLibDoc().Document_CreateDocumentFTVU.argtypes=[c_char_p,c_int,c_int,c_bool]
        GetDllLibDoc().Document_CreateDocumentFTVU.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentFTVU(fileNamePtr,iTypetype,iTypevalidationType,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat, password:str):
        fileNamePtr = StrToPtr(fileName)
        passwordPtr = StrToPtr(password)
        iTypetype:c_int = fileFormat.value

        GetDllLibDoc().Document_CreateDocumentFTP.argtypes=[c_char_p,c_int,c_char_p]
        GetDllLibDoc().Document_CreateDocumentFTP.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentFTP(fileNamePtr,iTypetype,passwordPtr);
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat, password:str, useNewEngine:bool):
        fileNamePtr = StrToPtr(fileName)
        passwordPtr = StrToPtr(password)
        iTypetype:c_int = fileFormat.value
    
        GetDllLibDoc().Document_CreateDocumentFTPU.argtypes=[c_char_p,c_int,c_char_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentFTPU.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentFTPU(fileNamePtr,iTypetype,passwordPtr,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, fileFormat:FileFormat, validationType:XHTMLValidationType):

        intPstream:c_void_p = stream.Ptr
        iTypetype:c_int = fileFormat.value
        iTypevalidationType:c_int = validationType.value

        GetDllLibDoc().Document_CreateDocumentSTV.argtypes=[c_void_p,c_int,c_int]
        GetDllLibDoc().Document_CreateDocumentSTV.restype=c_void_p
        intPtr =GetDllLibDoc().Document_CreateDocumentSTV(intPstream,iTypetype,iTypevalidationType)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, fileFormat:FileFormat, validationType:XHTMLValidationType, useNewEngine:bool):
        intPstream:c_void_p = stream.Ptr
        iTypetype:c_int = fileFormat.value
        iTypevalidationType:c_int = validationType.value

        GetDllLibDoc().Document_CreateDocumentSTVU.argtypes=[c_void_p,c_int,c_int,c_bool]
        GetDllLibDoc().Document_CreateDocumentSTVU.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentSTVU(intPstream,iTypetype,iTypevalidationType,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self):
        GetDllLibDoc().Document_CreateDocument.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocument()
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, useNewEngine:bool):
        GetDllLibDoc().Document_CreateDocumentU.argtypes=[c_bool]
        GetDllLibDoc().Document_CreateDocumentU.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentU(useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, useNewEngine:bool):
        intPstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_CreateDocumentSU.argtypes=[c_void_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentSU.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentSU(intPstream,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream):
        intPstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_CreateDocumentS.argtypes=[c_void_p]
        GetDllLibDoc().Document_CreateDocumentS.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentS(intPstream)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, useNewEngine:bool):
		
        intPstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_CreateDocumentSU.argtypes=[c_void_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentSU.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentSU(intPstream,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream,  fileFormat:FileFormat):
		
        intPstream:c_void_p = stream.Ptr
        iTypetype:c_int = fileFormat.value
        GetDllLibDoc().Document_CreateDocumentST.argtypes=[c_void_p,c_int]
        GetDllLibDoc().Document_CreateDocumentST.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentST(intPstream,iTypetype)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, fileFormat:FileFormat, useNewEngine:bool):
		
        intPstream:c_void_p = stream.Ptr
        iTypetype:c_int = fileFormat.value

        GetDllLibDoc().Document_CreateDocumentSTU.argtypes=[c_void_p,c_int,c_bool]
        GetDllLibDoc().Document_CreateDocumentSTU.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentSTU(intPstream,iTypetype,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, password:str):
        passwordPtr = StrToPtr(password)
        intPstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_CreateDocumentSP.argtypes=[c_void_p,c_char_p]
        GetDllLibDoc().Document_CreateDocumentSP.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateDocumentSP(intPstream,passwordPtr)
        super(Document, self).__init__(intPtr)

    @property
    def ForceTableRelayout(self)->bool:
        """

        """
        GetDllLibDoc().Document_get_ForceTableRelayout.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ForceTableRelayout.restype=c_bool
        ret = GetDllLibDoc().Document_get_ForceTableRelayout(self.Ptr)
        return ret

    @ForceTableRelayout.setter
    def ForceTableRelayout(self, value:bool):
        GetDllLibDoc().Document_set_ForceTableRelayout.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_ForceTableRelayout(self.Ptr, value)

    def ClearMacros(self):
        """
    <summary>
        Removes the macros from the document.
    </summary>
        """
        GetDllLibDoc().Document_ClearMacros.argtypes=[c_void_p]
        GetDllLibDoc().Document_ClearMacros(self.Ptr)


    def SetDateTimeOfUnitTest(self ,dateTime:'DateTime'):
        """
    <summary>
        Sets date and time of the unit test.
            For unit testing use only.
    </summary>
    <param name="dateTime">The date and time used in the test document.</param>
        """
        intPtrdateTime:c_void_p = dateTime.Ptr

        GetDllLibDoc().Document_SetDateTimeOfUnitTest.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_SetDateTimeOfUnitTest(self.Ptr, intPtrdateTime)

    def ResetPageLayoutCache(self):
        """
    <summary>
        Reset the page layout cache data of the new engine.
    </summary>
        """
        GetDllLibDoc().Document_ResetPageLayoutCache.argtypes=[c_void_p]
        GetDllLibDoc().Document_ResetPageLayoutCache(self.Ptr)

    def UpdateTableLayout(self):
        """
    <summary>
        Update table grid before saving the document when using the new engine.
    </summary>
        """
        GetDllLibDoc().Document_UpdateTableLayout.argtypes=[c_void_p]
        GetDllLibDoc().Document_UpdateTableLayout(self.Ptr)

    @property

    def OriginalFileFormat(self)->'FileFormat':
        """

        """
        GetDllLibDoc().Document_get_OriginalFileFormat.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_OriginalFileFormat.restype=c_int
        ret = GetDllLibDoc().Document_get_OriginalFileFormat(self.Ptr)
        objwraped = FileFormat(ret)
        return objwraped

    @dispatch
    def Cleanup(self):
        """

        """
        GetDllLibDoc().Document_Cleanup.argtypes=[c_void_p]
        GetDllLibDoc().Document_Cleanup(self.Ptr)

    @dispatch

    def Cleanup(self ,options:CleanupOptions):
        """

        """
        intPtroptions:c_void_p = options.Ptr

        GetDllLibDoc().Document_CleanupO.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_CleanupO(self.Ptr, intPtroptions)


    def SaveToOnlineBin(self ,fileName:str)->bool:
        """
    <summary>
        Saves the document in Spire.Online format.
    </summary>
    <param name="fileName">Spire.Online file path</param>
    <returns>Save Success: true; Failed: false</returns>
        """
        fileNamePtr = StrToPtr(fileName)
        
        GetDllLibDoc().Document_SaveToOnlineBin.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_SaveToOnlineBin.restype=c_bool
        ret = GetDllLibDoc().Document_SaveToOnlineBin(self.Ptr, fileNamePtr)
        return ret

    @dispatch

    def SaveToStream(self ,stream:Stream,paramList:ToPdfParameterList):
        """
    <summary>
        Saves the document into stream.
    </summary>
    <param name="stream">The stream.</param>
    <param name="paramList"></param>
        """
        intPtrstream:c_void_p = stream.Ptr
        intPtrparamList:c_void_p = paramList.Ptr

        GetDllLibDoc().Document_SaveToStream.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().Document_SaveToStream(self.Ptr, intPtrstream,intPtrparamList)

    @dispatch

    def LoadFromStream(self ,stream:Stream,fileFormat:FileFormat,validationType:XHTMLValidationType):
        """
    <summary>
        Opens the HTML document from stream .
    </summary>
    <param name="stream">The stream.</param>
    <param name="formatType">Type of the format.</param>
    <param name="validationType">Type of the validation.</param>
        """
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value
        enumvalidationType:c_int = validationType.value

        GetDllLibDoc().Document_LoadFromStream.argtypes=[c_void_p ,c_void_p,c_int,c_int]
        GetDllLibDoc().Document_LoadFromStream(self.Ptr, intPtrstream,enumfileFormat,enumvalidationType)

    @dispatch

    def LoadFromStream(self ,stream:Stream,fileFormat:FileFormat):
        """
    <summary>
        Opens the document from stream in Xml or Microsoft Word format.
    </summary>
    <param name="stream"></param>
    <param name="formatType"></param>
        """
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_LoadFromStreamSF.argtypes=[c_void_p ,c_void_p,c_int]
        GetDllLibDoc().Document_LoadFromStreamSF(self.Ptr, intPtrstream,enumfileFormat)

    @dispatch

    def LoadFromStream(self ,stream:Stream,fileFormat:FileFormat,password:str):
        """
    <summary>
        Opens the document from stream in Xml or Microsoft Word format.
    </summary>
    <param name="stream">The stream.</param>
    <param name="formatType">Type of the format.</param>
    <param name="password">The password.</param>
        """
        passwordPtr = StrToPtr(password)
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_LoadFromStreamSFP.argtypes=[c_void_p ,c_void_p,c_int,c_char_p]
        GetDllLibDoc().Document_LoadFromStreamSFP(self.Ptr, intPtrstream,enumfileFormat,passwordPtr)

    @dispatch

    def SaveToStream(self ,stream:Stream,fileFormat:FileFormat,certificatePath:str,securePassword:str):
        """
    <summary>
        Saves document to stream and digitally sign, Only DOC and DOCX are supported.
    </summary>
    <param name="stream">The stream.</param>
    <param name="fileFormat">The file format.</param>
    <param name="certificatePath">Path to the file certificate</param>
    <param name="securePassword">Password of the certificate.</param>
        """
        certificatePathPtr = StrToPtr(certificatePath)
        securePasswordPtr = StrToPtr(securePassword)
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_SaveToStreamSFCS.argtypes=[c_void_p ,c_void_p,c_int,c_char_p,c_char_p]
        GetDllLibDoc().Document_SaveToStreamSFCS(self.Ptr, intPtrstream,enumfileFormat,certificatePathPtr,securePasswordPtr)

#    @dispatch
#
#    def SaveToStream(self ,stream:Stream,fileFormat:FileFormat,certificateData:'Byte[]',securePassword:str):
#        """
#    <summary>
#        Saves document to stream and digitally sign, Only DOC and DOCX are supported.
#    </summary>
#    <param name="stream">The stream.</param>
#    <param name="fileFormat">The file format.</param>
#    <param name="certificateData">The certificate data.</param>
#    <param name="securePassword">Password of the certificate.</param>
#        """
#        intPtrstream:c_void_p = stream.Ptr
#        enumfileFormat:c_int = fileFormat.value
#        #arraycertificateData:ArrayTypecertificateData = ""
#        countcertificateData = len(certificateData)
#        ArrayTypecertificateData = c_void_p * countcertificateData
#        arraycertificateData = ArrayTypecertificateData()
#        for i in range(0, countcertificateData):
#            arraycertificateData[i] = certificateData[i].Ptr
#
#
#        GetDllLibDoc().Document_SaveToStreamSFCS1.argtypes=[c_void_p ,c_void_p,c_int,ArrayTypecertificateData,c_wchar_p]
#        GetDllLibDoc().Document_SaveToStreamSFCS1(self.Ptr, intPtrstream,enumfileFormat,arraycertificateData,securePassword)


    @dispatch

    def SaveToFile(self ,fileName:str,fileFormat:FileFormat,certificatePath:str,securePassword:str):
        """
    <summary>
        Saves document to file and digitally sign, Only DOC and DOCX are supported.
    </summary>
    <param name="stream">The file.</param>
    <param name="fileFormat">The file format.</param>
    <param name="certificatePath">Path to the file certificate</param>
    <param name="securePassword">Password of the certificate.</param>
        """
        fileNamePtr = StrToPtr(fileName)
        certificatePathPtr = StrToPtr(certificatePath)
        securePasswordPtr = StrToPtr(securePassword)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_SaveToFile.argtypes=[c_void_p ,c_char_p,c_int,c_char_p,c_char_p]
        GetDllLibDoc().Document_SaveToFile(self.Ptr, fileNamePtr,enumfileFormat,certificatePathPtr,securePasswordPtr)

#    @dispatch
#
#    def SaveToFile(self ,fileName:str,fileFormat:FileFormat,certificateData:'Byte[]',securePassword:str):
#        """
#    <summary>
#        Saves document to file and digitally sign, Only DOC and DOCX are supported.
#    </summary>
#    <param name="stream">The file.</param>
#    <param name="fileFormat">The file format.</param>
#    <param name="certificateData">The certificate data.</param>
#    <param name="securePassword">Password of the certificate.</param>
#        """
#        enumfileFormat:c_int = fileFormat.value
#        #arraycertificateData:ArrayTypecertificateData = ""
#        countcertificateData = len(certificateData)
#        ArrayTypecertificateData = c_void_p * countcertificateData
#        arraycertificateData = ArrayTypecertificateData()
#        for i in range(0, countcertificateData):
#            arraycertificateData[i] = certificateData[i].Ptr
#
#
#        GetDllLibDoc().Document_SaveToFileFFCS.argtypes=[c_void_p ,c_wchar_p,c_int,ArrayTypecertificateData,c_wchar_p]
#        GetDllLibDoc().Document_SaveToFileFFCS(self.Ptr, fileName,enumfileFormat,arraycertificateData,securePassword)


    @dispatch

    def SaveToStream(self ,stream:Stream,fileFormat:FileFormat):
        """
    <summary>
        Saves the document into stream in Xml or Microsoft Word format.
    </summary>
    <param name="stream"></param>
    <param name="formatType"></param>
        """
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_SaveToStreamSF.argtypes=[c_void_p ,c_void_p,c_int]
        GetDllLibDoc().Document_SaveToStreamSF(self.Ptr, intPtrstream,enumfileFormat)

    @dispatch

    def SaveToFile(self ,stream:Stream,fileFormat:FileFormat):
        """
    <summary>
        Saves the document into stream in Xml or Microsoft Word format.
    </summary>
    <param name="stream"></param>
    <param name="formatType"></param>
        """
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_SaveToFileSF.argtypes=[c_void_p ,c_void_p,c_int]
        GetDllLibDoc().Document_SaveToFileSF(self.Ptr, intPtrstream,enumfileFormat)

    def Close(self):
        """
    <summary>
        Closes this instance.
    </summary>
        """
        GetDllLibDoc().Document_Close.argtypes=[c_void_p]
        GetDllLibDoc().Document_Close(self.Ptr)

    def Dispose(self):
        """
    <summary>
        Prerforms application-defined tasks associated with freeing,releasing, or
            resetting unmanaged resources.
    </summary>
        """
        GetDllLibDoc().Document_Dispose.argtypes=[c_void_p]
        GetDllLibDoc().Document_Dispose(self.Ptr)

#    @dispatch
#
#    def SaveToImages(self ,type:ImageType)->List[SKImage]:
#        """
#    <summary>
#        Save the whole document into images
#    </summary>
#    <param name="type">The ImageType</param>
#    <returns>Return the images</returns>
#        """
#        enumtype:c_int = type.value
#
#        GetDllLibDoc().Document_SaveToImages.argtypes=[c_void_p ,c_int]
#        GetDllLibDoc().Document_SaveToImages.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_SaveToImages(self.Ptr, enumtype)
#        ret = GetObjVectorFromArray(intPtrArray, SKImage)
#        return ret


#    @dispatch
#
#    def SaveToImages(self ,pageIndex:int,pageCount:int,type:ImageType)->List[SKImage]:
#        """
#    <summary>
#        Save the specified range of pages into images
#    </summary>
#    <param name="pageIndex">Page index (Zero based)</param>
#    <param name="pageCount">Number of pages</param>
#    <param name="type">The ImageType</param>
#    <returns>Return the images</returns>
#        """
#        enumtype:c_int = type.value
#
#        GetDllLibDoc().Document_SaveToImagesPPT.argtypes=[c_void_p ,c_int,c_int,c_int]
#        GetDllLibDoc().Document_SaveToImagesPPT.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_SaveToImagesPPT(self.Ptr, pageIndex,pageCount,enumtype)
#        ret = GetObjVectorFromArray(intPtrArray, SKImage)
#        return ret


#    @dispatch
#
#    def SaveToImages(self ,pageIndex:int,type:ImageType)->SKImage:
#        """
#    <summary>
#        Save the specified page into image
#    </summary>
#    <param name="pageIndex">Page index</param>
#    <param name="type"> The ImageType</param>
#    <returns>Returns the image</returns>
#        """
#        enumtype:c_int = type.value
#
#        GetDllLibDoc().Document_SaveToImagesPT.argtypes=[c_void_p ,c_int,c_int]
#        GetDllLibDoc().Document_SaveToImagesPT.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_SaveToImagesPT(self.Ptr, pageIndex,enumtype)
#        ret = None if intPtr==None else SKImage(intPtr)
#        return ret
#


#    @dispatch
#
#    def SaveToImages(self ,type:ImageType,toImageOption:ToImageOption)->List[SKImage]:
#        """
#    <summary>
#        Save the specified page into image
#    </summary>
#    <param name="type">The ImageType</param>
#    <param name="toImageOption"></param>
#    <returns>Returns the image array</returns>
#        """
#        enumtype:c_int = type.value
#        intPtrtoImageOption:c_void_p = toImageOption.Ptr
#
#        GetDllLibDoc().Document_SaveToImagesTT.argtypes=[c_void_p ,c_int,c_void_p]
#        GetDllLibDoc().Document_SaveToImagesTT.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_SaveToImagesTT(self.Ptr, enumtype,intPtrtoImageOption)
#        ret = GetObjVectorFromArray(intPtrArray, SKImage)
#        return ret


    @dispatch
#
    def SaveImageToStreams(self ,pageIndex:int,pageCount:int,type:ImageType)->List[Stream]:
#        """
#    <summary>
#        Save the specified range of pages as image return streams. 
#            The default is PNG format image.
#    </summary>
#    <param name="pageIndex">Index of the page.</param>
#    <param name="pageCount">The page count.</param>
#    <param name="type">The type.</param>
#    <returns>System.IO.Stream[].</returns>
#        """
        enumtype:c_int = type.value

        GetDllLibDoc().Document_SaveImageToStreamsPPI.argtypes=[c_void_p ,c_int,c_int,c_int]
        GetDllLibDoc().Document_SaveImageToStreamsPPI.restype=IntPtrArray
        intPtrArray = GetDllLibDoc().Document_SaveImageToStreamsPPI(self.Ptr, pageIndex,pageCount,enumtype)
        ret = GetObjVectorFromArray(intPtrArray, Stream)
        return ret


    @dispatch

    def SaveImageToStreams(self ,pageIndex:int,type:ImageType)->Stream:
        """
    <summary>
        Save the specified page as image return stream.
            The default is PNG format image.
    </summary>
    <param name="pageIndex">Index of the page.</param>
    <param name="type">The type.</param>
    <returns>System.IO.Stream.</returns>
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Document_SaveImageToStreamsPI.argtypes=[c_void_p ,c_int,c_int]
        GetDllLibDoc().Document_SaveImageToStreamsPI.restype=c_void_p
        intPtr = GetDllLibDoc().Document_SaveImageToStreamsPI(self.Ptr, pageIndex,enumtype)
        ret = None if intPtr==None else Stream(intPtr)
        return ret


    @dispatch
#
    def SaveImageToStreams(self ,type:ImageType)->List[Stream]:
#        """
#    <summary>
#        Save the specified page as image return streams.
#            The default is PNG format image.
#    </summary>
#    <param name="type">The type.</param>
#    <returns>System.IO.Stream[].</returns>
#        """
        enumtype:c_int = type.value

        GetDllLibDoc().Document_SaveImageToStreamsI.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Document_SaveImageToStreamsI.restype=IntPtrArray
        intPtrArray = GetDllLibDoc().Document_SaveImageToStreamsI(self.Ptr, enumtype)
        ret = GetObjVectorFromArray(intPtrArray, Stream)
        return ret


#    @dispatch
#
#    def FindPattern(self ,pattern:'Regex')->TextSelection:
#        """
#    <summary>
#        Finds and returns entry of specified regular expression along with formatting.
#    </summary>
#    <param name="pattern">regex pattern</param>
#    <returns>Found text selection</returns>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_FindPattern.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().Document_FindPattern.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_FindPattern(self.Ptr, intPtrpattern)
#        ret = None if intPtr==None else TextSelection(intPtr)
#        return ret
#


#    @dispatch
#
#    def FindPatternInLine(self ,pattern:'Regex')->List[TextSelection]:
#        """
#    <summary>
#        Finds the first entry of specified pattern in single-line mode.
#    </summary>
#    <param name="pattern">The pattern.</param>
#    <returns></returns>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_FindPatternInLine.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().Document_FindPatternInLine.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_FindPatternInLine(self.Ptr, intPtrpattern)
#        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
#        return ret


    @dispatch

    def FindString(self ,stringValue:str,caseSensitive:bool,wholeWord:bool)->TextSelection:
        """
    <summary>
        Finds and returns string along with formatting.
    </summary>
    <param name="matchString"></param>
    <param name="caseSensitive"></param>
    <param name="wholeWord"></param>
    <returns></returns>
        """
        stringValuePtr = StrToPtr(stringValue)
        GetDllLibDoc().Document_FindString.argtypes=[c_void_p ,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Document_FindString.restype=c_void_p
        intPtr = GetDllLibDoc().Document_FindString(self.Ptr, stringValuePtr,caseSensitive,wholeWord)
        ret = None if intPtr==None else TextSelection(intPtr)
        return ret


#    @dispatch
#
#    def FindStringInLine(self ,given:str,caseSensitive:bool,wholeWord:bool)->List[TextSelection]:
#        """
#    <summary>
#        Finds the first entry of matchString text in single-line mode.
#    </summary>
#    <param name="matchString">The string to find.</param>
#    <param name="caseSensitive">if set to <c>true</c> use case sensitive search.</param>
#    <param name="wholeWord">if it search the whole word, set to <c>true</c>.</param>
#    <returns></returns>
#        """
#        
#        GetDllLibDoc().Document_FindStringInLine.argtypes=[c_void_p ,c_wchar_p,c_bool,c_bool]
#        GetDllLibDoc().Document_FindStringInLine.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_FindStringInLine(self.Ptr, given,caseSensitive,wholeWord)
#        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
#        return ret


#    @dispatch
#
    def FindAllPattern(self ,pattern:'Regex')->List[TextSelection]:
#        """
#    <summary>
#        Returns all entries of matchString regex.
#    </summary>
#    <param name="pattern"></param>
#        """
        intPtrpattern:c_void_p = pattern.Ptr

        GetDllLibDoc().Document_FindAllPattern.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_FindAllPattern.restype=IntPtrArray
        intPtrArray = GetDllLibDoc().Document_FindAllPattern(self.Ptr, intPtrpattern)
        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
        return ret


#    @dispatch
#
#    def FindAllPattern(self ,pattern:'Regex',isAdvancedSearch:bool)->List[TextSelection]:
#        """
#    <summary>
#        Returns all entries of matchString regex.
#    </summary>
#    <param name="pattern"></param>
#    <param name="isAdvancedSearch"></param>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_FindAllPatternPI.argtypes=[c_void_p ,c_void_p,c_bool]
#        GetDllLibDoc().Document_FindAllPatternPI.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_FindAllPatternPI(self.Ptr, intPtrpattern,isAdvancedSearch)
#        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
#        return ret


#
    def FindAllString(self ,matchString:str,caseSensitive:bool,wholeWord:bool)->List['TextSelection']:
#        """
#    <summary>
#        Returns all entries of matchString string, taking into consideration caseSensitive
#            and wholeWord options.
#    </summary>
#    <param name="matchString"></param>
#    <param name="caseSensitive"></param>
#    <param name="wholeWord"></param>
#    <returns></returns>
#        """
        matchStringPtr = StrToPtr(matchString)
        GetDllLibDoc().Document_FindAllString.argtypes=[c_void_p ,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Document_FindAllString.restype=IntPtrArray
        intPtrArray = GetDllLibDoc().Document_FindAllString(self.Ptr, matchStringPtr,caseSensitive,wholeWord)
        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
        return ret


    @dispatch
#
    def Replace(self ,pattern:Regex,replace:str)->int:
#        """
#    <summary>
#        Replaces all entries of matchString regular expression with newValue string.
#    </summary>
#    <param name="pattern"></param>
#    <param name="newValue"></param>
#    <returns></returns>
#        """
        intPtrpattern:c_void_p = pattern.Ptr
        replacePtr = StrToPtr(replace)

        GetDllLibDoc().Document_Replace.argtypes=[c_void_p ,c_void_p,c_char_p]
        GetDllLibDoc().Document_Replace.restype=c_int
        ret = GetDllLibDoc().Document_Replace(self.Ptr, intPtrpattern,replacePtr)
        return ret


    @dispatch

    def Replace(self ,matchString:str,newValue:str,caseSensitive:bool,wholeWord:bool)->int:
        """
    <summary>
        Replaces all entries of matchString string with newValue string, taking into
            consideration caseSensitive and wholeWord options.
    </summary>
    <param name="matchString"></param>
    <param name="newValue"></param>
    <param name="caseSensitive"></param>
    <param name="wholeWord"></param>
        """
        matchStringPtr = StrToPtr(matchString)
        newValuePtr = StrToPtr(newValue)
        GetDllLibDoc().Document_ReplaceMNCW.argtypes=[c_void_p ,c_char_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Document_ReplaceMNCW.restype=c_int
        ret = GetDllLibDoc().Document_ReplaceMNCW(self.Ptr, matchStringPtr,newValuePtr,caseSensitive,wholeWord)
        return ret

    @dispatch

    def Replace(self ,matchString:str,textSelection:TextSelection,caseSensitive:bool,wholeWord:bool)->int:
        """
    <summary>
        Replaces all entries of matchString string with TextSelection, taking into
            consideration caseSensitive and wholeWord options.
    </summary>
    <param name="matchString">The matchString.</param>
    <param name="textSelection">The text selection.</param>
    <param name="caseSensitive">if it is case sensitive, set to <c>true</c>.</param>
    <param name="wholeWord">if it specifies whole word, set to <c>true</c>.</param>
    <returns></returns>
        """
        matchStringPtr = StrToPtr(matchString)
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Document_ReplaceMTCW.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool]
        GetDllLibDoc().Document_ReplaceMTCW.restype=c_int
        ret = GetDllLibDoc().Document_ReplaceMTCW(self.Ptr, matchStringPtr,intPtrtextSelection,caseSensitive,wholeWord)
        return ret

#    @dispatch
#
#    def Replace(self ,pattern:'Regex',textSelection:TextSelection)->int:
#        """
#    <summary>
#        Replaces all entries of matchString regular expression with TextRangesHolder.
#    </summary>
#    <param name="pattern">The pattern.</param>
#    <param name="textSelection">The text selection.</param>
#    <returns></returns>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#        intPtrtextSelection:c_void_p = textSelection.Ptr
#
#        GetDllLibDoc().Document_ReplacePT.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().Document_ReplacePT.restype=c_int
#        ret = GetDllLibDoc().Document_ReplacePT(self.Ptr, intPtrpattern,intPtrtextSelection)
#        return ret



    def CloneWebSettingsTo(self ,destDoc:'Document'):
        """
    <summary>
        clone Websettings to other document
    </summary>
    <param name="otherDoc">The other doc</param>
    <returns></returns>
        """
        intPtrdestDoc:c_void_p = destDoc.Ptr

        GetDllLibDoc().Document_CloneWebSettingsTo.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_CloneWebSettingsTo(self.Ptr, intPtrdestDoc)

    @dispatch

    def Replace(self ,matchString:str,matchDoc:IDocument,caseSensitive:bool,wholeWord:bool)->int:
        """
    <summary>
        Replaces the specified matchString.
    </summary>
    <param name="matchString">The matchString.</param>
    <param name="matchDoc">The newValue doc.</param>
    <param name="caseSensitive">if it is case sensitive, set to <c>true</c>.</param>
    <param name="wholeWord">if specifies whole word,set to <c>true</c>.</param>
    <returns></returns>
        """
        matchStringPtr = StrToPtr(matchString)
        intPtrmatchDoc:c_void_p = matchDoc.Ptr

        GetDllLibDoc().Document_ReplaceMMCW.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool]
        GetDllLibDoc().Document_ReplaceMMCW.restype=c_int
        ret = GetDllLibDoc().Document_ReplaceMMCW(self.Ptr, matchStringPtr,intPtrmatchDoc,caseSensitive,wholeWord)
        return ret

    @dispatch
    def UpdateWordCount(self):
        """
    <summary>
        Update Paragraphs count, Word count and Character count
    </summary>
        """
        GetDllLibDoc().Document_UpdateWordCount.argtypes=[c_void_p]
        GetDllLibDoc().Document_UpdateWordCount(self.Ptr)

#    @dispatch
#
#    def UpdateWordCount(self ,splitchar:'Char[]'):
#        """
#    <summary>
#        Update Paragraphs count, Word count and Character count.
#    </summary>
#    <param name="splitchar">The word separator. </param>
#        """
#        #arraysplitchar:ArrayTypesplitchar = ""
#        countsplitchar = len(splitchar)
#        ArrayTypesplitchar = c_void_p * countsplitchar
#        arraysplitchar = ArrayTypesplitchar()
#        for i in range(0, countsplitchar):
#            arraysplitchar[i] = splitchar[i].Ptr
#
#
#        GetDllLibDoc().Document_UpdateWordCountS.argtypes=[c_void_p ,ArrayTypesplitchar]
#        GetDllLibDoc().Document_UpdateWordCountS(self.Ptr, arraysplitchar)


#    @dispatch
#
#    def UpdateWordCount(self ,splitchar:'Char[]',includeTbFnEn:bool):
#        """
#    <summary>
#        Update Paragraphs count, Word count and Character count.
#    </summary>
#    <param name="splitchar">The word separator.</param>
#    <param name="includeTbFnEn">The include text boxes,footnotes and endnotes.</param>
#        """
#        #arraysplitchar:ArrayTypesplitchar = ""
#        countsplitchar = len(splitchar)
#        ArrayTypesplitchar = c_void_p * countsplitchar
#        arraysplitchar = ArrayTypesplitchar()
#        for i in range(0, countsplitchar):
#            arraysplitchar[i] = splitchar[i].Ptr
#
#
#        GetDllLibDoc().Document_UpdateWordCountSI.argtypes=[c_void_p ,ArrayTypesplitchar,c_bool]
#        GetDllLibDoc().Document_UpdateWordCountSI(self.Ptr, arraysplitchar,includeTbFnEn)



    def CheckProtectionPassWord(self ,password:str)->bool:
        """
    <summary>
        Check that the password entered is the same as the permission protection password
    </summary>
    <param name="password">The enter password</param>
    <returns>whether the password entered is the same as the permission protection password</returns>
        """
        passwordPtr = StrToPtr(password)
        
        GetDllLibDoc().Document_CheckProtectionPassWord.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_CheckProtectionPassWord.restype=c_bool
        ret = GetDllLibDoc().Document_CheckProtectionPassWord(self.Ptr, passwordPtr)
        return ret

    def GetPageCount(self)->int:
        """
    <summary>
        Gets total number of pages for document.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Document_GetPageCount.argtypes=[c_void_p]
        GetDllLibDoc().Document_GetPageCount.restype=c_int
        ret = GetDllLibDoc().Document_GetPageCount(self.Ptr)
        return ret

    @dispatch
    def UpdateTableOfContents(self):
        """
    <summary>
        Update Table of contents in the document.
    </summary>
        """
        GetDllLibDoc().Document_UpdateTableOfContents.argtypes=[c_void_p]
        GetDllLibDoc().Document_UpdateTableOfContents(self.Ptr)

    @dispatch
    
    def UpdateTableOfContents(self ,toc:TableOfContent):
        """
    <summary>
        Update specified Table of content in the document.
    </summary>
        """
        intPtrtoc:c_void_p = toc.Ptr

        GetDllLibDoc().Document_UpdateTableOfContentsT.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_UpdateTableOfContentsT(self.Ptr, intPtrtoc)

    @dispatch
    def UpdateTOCPageNumbers(self):
        """
    <summary>
        Update Table of contents page numbers in the document.
    </summary>
        """
        GetDllLibDoc().Document_UpdateTOCPageNumbers.argtypes=[c_void_p]
        GetDllLibDoc().Document_UpdateTOCPageNumbers(self.Ptr)

    @dispatch

    def UpdateTOCPageNumbers(self ,toc:'TableOfContent'):
        """
    <summary>
        Update specified Table of content page numbers in the document.
    </summary>
    <param name="toc">specified Table of content</param>
        """
        intPtrtoc:c_void_p = toc.Ptr

        GetDllLibDoc().Document_UpdateTOCPageNumbersT.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_UpdateTOCPageNumbersT(self.Ptr, intPtrtoc)

    @dispatch

    def Compare(self ,document:'Document',author:str):
        """
    <summary>
        Compares this document with another document.
    </summary>
    <param name="document">Document to compare</param>
    <param name="author">The author to use for revisions</param>
        """
        authorPtr = StrToPtr(author)
        intPtrdocument:c_void_p = document.Ptr

        GetDllLibDoc().Document_Compare.argtypes=[c_void_p ,c_void_p,c_char_p]
        GetDllLibDoc().Document_Compare(self.Ptr, intPtrdocument,authorPtr)

    @dispatch

    def Compare(self ,document:'Document',author:str,options:CompareOptions):
        """
    <summary>
        Compares this document with another document.
    </summary>
    <param name="document">Document to compare</param>
    <param name="author">The author to use for revisions</param>
    <param name="options">The comparison parameter</param>
        """
        authorPtr = StrToPtr(author)
        intPtrdocument:c_void_p = document.Ptr
        intPtroptions:c_void_p = options.Ptr

        GetDllLibDoc().Document_CompareDAO.argtypes=[c_void_p ,c_void_p,c_char_p,c_void_p]
        GetDllLibDoc().Document_CompareDAO(self.Ptr, intPtrdocument,authorPtr,intPtroptions)

    @dispatch

    def Compare(self ,document:'Document',author:str,dateTime:DateTime):
        """
    <summary>
        Compares this document with another document.
    </summary>
    <param name="document">Document to compare</param>
    <param name="author">The author to use for revisions</param>
    <param name="dateTime">The date and time to use for revisions</param>
        """
        authorPtr = StrToPtr(author)
        intPtrdocument:c_void_p = document.Ptr
        intPtrdateTime:c_void_p = dateTime.Ptr

        GetDllLibDoc().Document_CompareDAD.argtypes=[c_void_p ,c_void_p,c_char_p,c_void_p]
        GetDllLibDoc().Document_CompareDAD(self.Ptr, intPtrdocument,authorPtr,intPtrdateTime)

    @dispatch

    def Compare(self ,document:'Document',author:str,dateTime:DateTime,options:CompareOptions):
        """
    <summary>
        Compares this document with another document.
    </summary>
    <param name="document">Document to compare</param>
    <param name="author">The author to use for revisions</param>
    <param name="dateTime">The date and time to use for revisions</param>
    <param name="options">The comparison parameter</param>
        """
        authorPtr = StrToPtr(author)
        intPtrdocument:c_void_p = document.Ptr
        intPtrdateTime:c_void_p = dateTime.Ptr
        intPtroptions:c_void_p = options.Ptr

        GetDllLibDoc().Document_CompareDADO.argtypes=[c_void_p ,c_void_p,c_char_p,c_void_p,c_void_p]
        GetDllLibDoc().Document_CompareDADO(self.Ptr, intPtrdocument,authorPtr,intPtrdateTime,intPtroptions)

    @dispatch

    def ReplaceInLine(self ,matchString:str,newValue:str,caseSensitive:bool,wholeWord:bool)->int:
        """
    <summary>
        Replaces all entries of matchString text with newValue text in single-line mode.
    </summary>
    <param name="matchString">The matchString.</param>
    <param name="newValue">The newValue.</param>
    <param name="caseSensative">if it specifies case sensative newValue, set to <c>true</c>.</param>
    <param name="wholeWord">if it specifies only whole word will be replaced, set to <c>true</c>.</param>
    <returns></returns>
        """
        matchStringPtr = StrToPtr(matchString)
        newValuePtr = StrToPtr(newValue)
        GetDllLibDoc().Document_ReplaceInLine.argtypes=[c_void_p ,c_char_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Document_ReplaceInLine.restype=c_int
        ret = GetDllLibDoc().Document_ReplaceInLine(self.Ptr, matchStringPtr,newValuePtr,caseSensitive,wholeWord)
        return ret

#    @dispatch
#
#    def ReplaceInLine(self ,pattern:'Regex',newValue:str)->int:
#        """
#    <summary>
#        Replaces all entries with specified pattern with newValue text in single-line mode.
#    </summary>
#    <param name="pattern">The pattern.</param>
#    <param name="newValue">The newValue.</param>
#    <returns></returns>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_ReplaceInLinePN.argtypes=[c_void_p ,c_void_p,c_wchar_p]
#        GetDllLibDoc().Document_ReplaceInLinePN.restype=c_int
#        ret = GetDllLibDoc().Document_ReplaceInLinePN(self.Ptr, intPtrpattern,newValue)
#        return ret


    @dispatch

    def ReplaceInLine(self ,matchString:str,matchSelection:TextSelection,caseSensitive:bool,wholeWord:bool)->int:
        """
    <summary>
        Replaces the matchString text with matchSelection in single-line mode.
    </summary>
    <param name="matchString">The matchString.</param>
    <param name="matchSelection">The matchSelection.</param>
    <param name="caseSensitive">if it is case sensitive newValue, set to <c>true</c>.</param>
    <param name="wholeWord">if it replaces only whole word, set to <c>true</c>.</param>
    <returns></returns>
        """
        matchStringPtr = StrToPtr(matchString)
        intPtrmatchSelection:c_void_p = matchSelection.Ptr

        GetDllLibDoc().Document_ReplaceInLineMMCW.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool]
        GetDllLibDoc().Document_ReplaceInLineMMCW.restype=c_int
        ret = GetDllLibDoc().Document_ReplaceInLineMMCW(self.Ptr, matchStringPtr,intPtrmatchSelection,caseSensitive,wholeWord)
        return ret

#    @dispatch
#
#    def ReplaceInLine(self ,pattern:'Regex',matchSelection:TextSelection)->int:
#        """
#    <summary>
#        Replaces the matchString pattern with matchSelection in single-line mode.
#    </summary>
#    <param name="pattern">The pattern.</param>
#    <param name="matchSelection">The matchSelection.</param>
#    <returns>The number of performed replaces.</returns>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#        intPtrmatchSelection:c_void_p = matchSelection.Ptr
#
#        GetDllLibDoc().Document_ReplaceInLinePM.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().Document_ReplaceInLinePM.restype=c_int
#        ret = GetDllLibDoc().Document_ReplaceInLinePM(self.Ptr, intPtrpattern,intPtrmatchSelection)
#        return ret


    @dispatch

    def FindString(self ,start:BodyRegion,matchString:str,caseSensitive:bool,wholeWord:bool)->TextSelection:
        """
    <summary>
        Finds the next entry of matchString string, taking into consideration caseSensitive
            and wholeWord options.
    </summary>
    <param name="start">Search starts.</param>
    <param name="matchString">The string to find.</param>
    <param name="caseSensitive">if it specifies case sensitive search, set to <c>true</c> .</param>
    <param name="wholeWord">if it search for the whole word, set to <c>true</c> .</param>
    <returns></returns>
        """
        matchStringPtr = StrToPtr(matchString)
        intPtrstart:c_void_p = start.Ptr

        GetDllLibDoc().Document_FindStringSMCW.argtypes=[c_void_p ,c_void_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Document_FindStringSMCW.restype=c_void_p
        intPtr = GetDllLibDoc().Document_FindStringSMCW(self.Ptr, intPtrstart,matchStringPtr,caseSensitive,wholeWord)
        ret = None if intPtr==None else TextSelection(intPtr)
        return ret


#    @dispatch
#
#    def FindPattern(self ,start:BodyRegion,pattern:'Regex')->TextSelection:
#        """
#    <summary>
#        Finds the next entry of matchString pattern.
#    </summary>
#    <param name="start">Search starts</param>
#    <param name="pattern">The pattern.</param>
#    <returns></returns>
#        """
#        intPtrstart:c_void_p = start.Ptr
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_FindPatternSP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().Document_FindPatternSP.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_FindPatternSP(self.Ptr, intPtrstart,intPtrpattern)
#        ret = None if intPtr==None else TextSelection(intPtr)
#        return ret
#


#    @dispatch
#
#    def FindStringInLine(self ,start:BodyRegion,matchString:str,caseSensitive:bool,wholeWord:bool)->List[TextSelection]:
#        """
#    <summary>
#        Finds the next matchString text starting from specified using single-line mode.
#    </summary>
#    <param name="start">Search start.</param>
#    <param name="matchString">The matchString.</param>
#    <param name="caseSensitive">if it is case sensitive search, set to <c>true</c>.</param>
#    <param name="wholeWord">if it search for whole word, set to <c>true</c> .</param>
#    <returns></returns>
#        """
#        intPtrstart:c_void_p = start.Ptr
#
#        GetDllLibDoc().Document_FindStringInLineSMCW.argtypes=[c_void_p ,c_void_p,c_wchar_p,c_bool,c_bool]
#        GetDllLibDoc().Document_FindStringInLineSMCW.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_FindStringInLineSMCW(self.Ptr, intPtrstart,matchString,caseSensitive,wholeWord)
#        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
#        return ret


#    @dispatch
#
#    def FindPatternInLine(self ,start:BodyRegion,pattern:'Regex')->List[TextSelection]:
#        """
#    <summary>
#        Finds the text which fit the specified pattern starting from start.
#            using single-line mode.
#    </summary>
#    <param name="start">Search start.</param>
#    <param name="pattern">The pattern.</param>
#    <returns></returns>
#        """
#        intPtrstart:c_void_p = start.Ptr
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_FindPatternInLineSP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().Document_FindPatternInLineSP.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_FindPatternInLineSP(self.Ptr, intPtrstart,intPtrpattern)
#        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
#        return ret


    def ResetFindState(self):
        """
    <summary>
        Resets the FindPattern.
    </summary>
        """
        GetDllLibDoc().Document_ResetFindState.argtypes=[c_void_p]
        GetDllLibDoc().Document_ResetFindState(self.Ptr)


    def CreateParagraphItem(self ,itemType:'ParagraphItemType')->'ParagraphBase':
        """
    <summary>
        Creates new paragraph item instance.
    </summary>
    <param name="itemType">Paragraph item type</param>
    <returns></returns>
        """
        enumitemType:c_int = itemType.value

        GetDllLibDoc().Document_CreateParagraphItem.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Document_CreateParagraphItem.restype=IntPtrWithTypeName
        intPtr = GetDllLibDoc().Document_CreateParagraphItem(self.Ptr, enumitemType)
        ret = None if intPtr==None else self._createParagraphItemByType(intPtr)
        return ret

    def _createParagraphItemByType(self, intPtrWithTypeName:IntPtrWithTypeName)->ParagraphBase:
        ret= None
        if intPtrWithTypeName == None:
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Break"):
            from spire.doc import Break
            ret = Break(intPtr)
        elif(strName == "Spire.Doc.Fields.TextRange"):
            from spire.doc import TextRange
            ret = TextRange(intPtr)
        elif(strName == "Spire.Doc.Fields.DocPicture"):
            from spire.doc import DocPicture
            ret = DocPicture(intPtr)
        elif(strName == "Spire.Doc.BookmarkStart"):
            from spire.doc import BookmarkStart
            ret = BookmarkStart(intPtr)
        elif(strName == "Spire.Doc.BookmarkEnd"):
            from spire.doc import BookmarkEnd
            ret = BookmarkEnd(intPtr)
        elif(strName == "Spire.Doc.Fields.Field"):
            from spire.doc import Field
            ret = Field(intPtr)
        elif(strName == "Spire.Doc.Fields.TextBox"):
            from spire.doc import TextBox
            ret = TextBox(intPtr)
        elif(strName == "Spire.Doc.Fields.MergeField"):
            from spire.doc import MergeField
            ret = MergeField(intPtr)
        #elif(strName == "Spire.Doc.Fields.EmbedField"):
        #  ret = EmbedField(intPtr)
        elif(strName == "Spire.Doc.Fields.Symbol"):
            from spire.doc import Symbol
            ret = Symbol(intPtr)
        elif(strName == "Spire.Doc.Fields.FieldMark"):
            from spire.doc import FieldMark
            ret = FieldMark(intPtr)
        elif(strName == "Spire.Doc.Fields.CheckBoxFormField"):
            from spire.doc import CheckBoxFormField
            ret = CheckBoxFormField(intPtr)
        elif(strName == "Spire.Doc.Fields.TextFormField"):
            from spire.doc import TextFormField
            ret = TextFormField(intPtr)
        elif(strName == "Spire.Doc.Fields.DropDownFormField"):
            from spire.doc import DropDownFormField
            ret = DropDownFormField(intPtr)
        elif(strName == "Spire.Doc.Fields.Comment"):
            from spire.doc import Comment
            ret = Comment(intPtr)
        elif(strName == "Spire.Doc.Documents.CommentMark"):
            from spire.doc import CommentMark
            ret = CommentMark(intPtr)
        elif(strName == "Spire.Doc.Fields.Footnote"):
            from spire.doc import Footnote
            ret = Footnote(intPtr)
        elif(strName == "Spire.Doc.Fields.ShapeObject"):
            from spire.doc import ShapeObject
            ret = ShapeObject(intPtr)
        elif(strName == "Spire.Doc.Fields.ShapeGroup"):
            from spire.doc import ShapeGroup
            ret = ShapeGroup(intPtr)
        elif(strName == "Spire.Doc.Fields.TableOfContent"):
            from spire.doc import TableOfContent
            ret = TableOfContent(intPtr)
        elif(strName == "Spire.Doc.Fields.DocOleObject"):
            from spire.doc import DocOleObject
            ret = DocOleObject(intPtr)
        else:
            ret = ParagraphBase(intPtr)
        return ret

    def CreateParagraph(self)->'Paragraph':
        """
    <summary>
        Creates the paragraph.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Document_CreateParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Document_CreateParagraph.restype=c_void_p
        intPtr = GetDllLibDoc().Document_CreateParagraph(self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    def CreateMinialDocument(self):
        """
    <summary>
        Create a minial document,  one empty section to the document and one empty paragraph to created section.
    </summary>
        """
        GetDllLibDoc().Document_CreateMinialDocument.argtypes=[c_void_p]
        GetDllLibDoc().Document_CreateMinialDocument(self.Ptr)


    def AddSection(self)->'Section':
        """
    <summary>
        Adds new section to document.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Document_AddSection.argtypes=[c_void_p]
        GetDllLibDoc().Document_AddSection.restype=c_void_p
        intPtr = GetDllLibDoc().Document_AddSection(self.Ptr)
        ret = None if intPtr==None else Section(intPtr)
        return ret



    def AddParagraphStyle(self ,styleName:str)->'ParagraphStyle':
        """
    <summary>
        Adds new paragraph style to the document.
    </summary>
    <param name="styleName">Paragraph style name</param>
    <returns></returns>
        """
        styleNamePtr = StrToPtr(styleName)
        GetDllLibDoc().Document_AddParagraphStyle.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_AddParagraphStyle.restype=c_void_p
        intPtr = GetDllLibDoc().Document_AddParagraphStyle(self.Ptr, styleNamePtr)
        ret = None if intPtr==None else ParagraphStyle(intPtr)
        return ret



    def AddListStyle(self ,listType:'ListType',styleName:str)->'ListStyle':
        """
    <summary>
        Adds new list style to document.
    </summary>
    <param name="listType">List type</param>
    <param name="styleName">Paragraph style name</param>
    <returns></returns>
        """
        styleNamePtr = StrToPtr(styleName)
        enumlistType:c_int = listType.value

        GetDllLibDoc().Document_AddListStyle.argtypes=[c_void_p ,c_int,c_char_p]
        GetDllLibDoc().Document_AddListStyle.restype=c_void_p
        intPtr = GetDllLibDoc().Document_AddListStyle(self.Ptr, enumlistType,styleNamePtr)
        ret = None if intPtr==None else ListStyle(intPtr)
        return ret



    def GetText(self)->str:
        """
    <summary>
        Gets the document's text.
    </summary>
        """
        GetDllLibDoc().Document_GetText.argtypes=[c_void_p]
        GetDllLibDoc().Document_GetText.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Document_GetText(self.Ptr))
        return ret


#    @staticmethod
#    @dispatch
#
#    def Sign(sourceStream:Stream,certificatePath:str,securePassword:str)->List[Byte]:
#        """
#    <summary>
#         Create digitally signed word document.
#             Digital signature of documents support only DOC and DOCX formats.
#    </summary>
#    <param name="sourceStream">Source file stream</param>
#    <param name="certificatePath">Path to the file certificate</param>
#    <param name="securePassword">Password of the certificate.</param>
#    <returns>Bytes of signed word document </returns>
#        """
#        intPtrsourceStream:c_void_p = sourceStream.Ptr
#
#        GetDllLibDoc().Document_Sign.argtypes=[ c_void_p,c_wchar_p,c_wchar_p]
#        GetDllLibDoc().Document_Sign.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_Sign( intPtrsourceStream,certificatePath,securePassword)
#        ret = GetObjVectorFromArray(intPtrArray, Byte)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def Sign(sourceStream:Stream,certificateData:'Byte[]',securePassword:str)->List[Byte]:
#        """
#    <summary>
#        Create digitally signed word document.
#            Digital signature of documents support only DOC and DOCX formats.
#    </summary>
#    <param name="sourceStream">Source file stream.</param>
#    <param name="certificateData">the certificate data.</param>
#    <param name="securePassword">Password of the certificate.</param>
#    <returns>Bytes of signed word document</returns>
#        """
#        intPtrsourceStream:c_void_p = sourceStream.Ptr
#        #arraycertificateData:ArrayTypecertificateData = ""
#        countcertificateData = len(certificateData)
#        ArrayTypecertificateData = c_void_p * countcertificateData
#        arraycertificateData = ArrayTypecertificateData()
#        for i in range(0, countcertificateData):
#            arraycertificateData[i] = certificateData[i].Ptr
#
#
#        GetDllLibDoc().Document_SignSCS.argtypes=[ c_void_p,ArrayTypecertificateData,c_wchar_p]
#        GetDllLibDoc().Document_SignSCS.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_SignSCS( intPtrsourceStream,arraycertificateData,securePassword)
#        ret = GetObjVectorFromArray(intPtrArray, Byte)
#        return ret



    def Clone(self)->'Document':
        """
    <summary>
        Clones itself.
    </summary>
    <returns></returns>
        """
        GetDllLibDoc().Document_Clone.argtypes=[c_void_p]
        GetDllLibDoc().Document_Clone.restype=c_void_p
        intPtr = GetDllLibDoc().Document_Clone(self.Ptr)
        ret = None if intPtr==None else Document(intPtr)
        return ret



    def CloneDefaultStyleTo(self ,destDoc:'Document'):
        """
    <summary>
        Clones the current document default style to the destination document.
    </summary>
    <param name="destDoc">The destination document.</param>
        """
        intPtrdestDoc:c_void_p = destDoc.Ptr

        GetDllLibDoc().Document_CloneDefaultStyleTo.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_CloneDefaultStyleTo(self.Ptr, intPtrdestDoc)


    def CloneThemesTo(self ,destDoc:'Document'):
        """
    <summary>
        Clones the current document theme style to the destination document.
    </summary>
    <param name="destDoc">The destination document.</param>
        """
        intPtrdestDoc:c_void_p = destDoc.Ptr

        GetDllLibDoc().Document_CloneThemesTo.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_CloneThemesTo(self.Ptr, intPtrdestDoc)


    def CloneCompatibilityTo(self ,destDoc:'Document'):
        """
    <summary>
        Clones the current document compatibility to the destination document.
    </summary>
    <param name="destDoc">The destination document.</param>
        """
        intPtrdestDoc:c_void_p = destDoc.Ptr

        GetDllLibDoc().Document_CloneCompatibilityTo.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_CloneCompatibilityTo(self.Ptr, intPtrdestDoc)


    def ImportSection(self ,section:'ISection'):
        """
    <summary>
        Imports section into document.
    </summary>
    <param name="section">The section.</param>
        """
        intPtrsection:c_void_p = section.Ptr

        GetDllLibDoc().Document_ImportSection.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_ImportSection(self.Ptr, intPtrsection)

    @dispatch

    def ImportContent(self ,doc:IDocument):
        """
    <summary>
        Imports all content into the document.
    </summary>
    <param name="doc">The doc.</param>
        """
        intPtrdoc:c_void_p = doc.Ptr

        GetDllLibDoc().Document_ImportContent.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_ImportContent(self.Ptr, intPtrdoc)

    @dispatch

    def ImportContent(self ,doc:IDocument,importStyles:bool):
        """
    <summary>
        Imports all content into document.
    </summary>
    <param name="doc">The doc.</param>
    <param name="importStyles">If document styles which have same names will be also imported
            to the destination document,set to <c>true</c>.</param>
        """
        intPtrdoc:c_void_p = doc.Ptr

        GetDllLibDoc().Document_ImportContentDI.argtypes=[c_void_p ,c_void_p,c_bool]
        GetDllLibDoc().Document_ImportContentDI(self.Ptr, intPtrdoc,importStyles)


    def AddStyle(self ,builtinStyle:'BuiltinStyle')->'Style':
        """
    <summary>
        Adds the style to the document style.
    </summary>
    <param name="builtinStyle">The built-in style.</param>
        """
        enumbuiltinStyle:c_int = builtinStyle.value

        GetDllLibDoc().Document_AddStyle.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Document_AddStyle.restype=IntPtrWithTypeName
        intPtr = GetDllLibDoc().Document_AddStyle(self.Ptr, enumbuiltinStyle)
        ret = None if intPtr==None else self._create(intPtr)
        return ret


    def _create(self,intPtrWithTypeName:IntPtrWithTypeName)->'Style':

        ret= None
        if intPtrWithTypeName == None :
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Documents.ListStyle"):
            ret = ListStyle(intPtr)
        elif(strName == "Spire.Doc.Documents.ParagraphStyle"):
            from spire.doc import ParagraphStyle
            ret = ParagraphStyle(intPtr)
        else:
            ret = Style(intPtr)
        return ret

    def AcceptChanges(self):
        """
    <summary>
        Accepts changes tracked from the moment of last change acceptance.
    </summary>
        """
        GetDllLibDoc().Document_AcceptChanges.argtypes=[c_void_p]
        GetDllLibDoc().Document_AcceptChanges(self.Ptr)

    def RejectChanges(self):
        """
    <summary>
        Rejects changes tracked from the moment of last change acceptance.
    </summary>
        """
        GetDllLibDoc().Document_RejectChanges.argtypes=[c_void_p]
        GetDllLibDoc().Document_RejectChanges(self.Ptr)

    @dispatch

    def Protect(self ,type:ProtectionType):
        """
    <summary>
        Protects the document.
    </summary>
    <param name="type">The type of the protection.</param>
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Document_Protect.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Document_Protect(self.Ptr, enumtype)

    @dispatch

    def Protect(self ,type:ProtectionType,password:str):
        """
    <summary>
        Protects the document.
    </summary>
    <param name="type">The type of the protection</param>
    <param name="password">The password used for protection.</param>
        """
        passwordPtr = StrToPtr(password)
        enumtype:c_int = type.value

        GetDllLibDoc().Document_ProtectTP.argtypes=[c_void_p ,c_int,c_char_p]
        GetDllLibDoc().Document_ProtectTP(self.Ptr, enumtype,passwordPtr)


    def Encrypt(self ,password:str):
        """
    <summary>
        Encrypts the document.
    </summary>
    <param name="password">Password.</param>
        """
        passwordPtr = StrToPtr(password)
        GetDllLibDoc().Document_Encrypt.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_Encrypt(self.Ptr, passwordPtr)

    def RemoveEncryption(self):
        """
    <summary>
        Removes the encryption.
    </summary>
        """
        GetDllLibDoc().Document_RemoveEncryption.argtypes=[c_void_p]
        GetDllLibDoc().Document_RemoveEncryption(self.Ptr)


    def SaveToTxt(self ,fileName:str,encoding:'Encoding'):
        """
    <summary>
        Saves to text document with specified encoding.
    </summary>
    <param name="fileName">Name of the file.</param>
    <param name="encoding">The encoding.</param>
        """
        fileNamePtr = StrToPtr(fileName)
        intPtrencoding:c_void_p = encoding.Ptr

        GetDllLibDoc().Document_SaveToTxt.argtypes=[c_void_p ,c_char_p,c_void_p]
        GetDllLibDoc().Document_SaveToTxt(self.Ptr, fileNamePtr,intPtrencoding)


    def OpenOnlineBin(self ,fileName:str):
        """

        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_OpenOnlineBin.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_OpenOnlineBin(self.Ptr, fileNamePtr)

#    @dispatch
#
#    def LoadHTML(self ,reader:'TextReader',baseURL:str,validationType:XHTMLValidationType):
#        """
#    <summary>
#        Load document in html format
#    </summary>
#    <param name="reader">Reader of html code.</param>
#    <param name="baseURL">The default base URL for all links of external resource,
#                                   it should be a absolute and well formed uri string, for example:
#                                   http://www.e-iceblue.com/ or file:///C:/mywebsite/docs/
#                                   If it's null, use the href attribute of base tag in html instead;
#                                   Otherwise, it will overwrite the href attribute of base tag.</param>
#    <param name="validationType">XHTML validation type.</param>
#        """
#        intPtrreader:c_void_p = reader.Ptr
#        enumvalidationType:c_int = validationType.value
#
#        GetDllLibDoc().Document_LoadHTML.argtypes=[c_void_p ,c_void_p,c_wchar_p,c_int]
#        GetDllLibDoc().Document_LoadHTML(self.Ptr, intPtrreader,baseURL,enumvalidationType)


#    @dispatch
#
#    def LoadHTML(self ,reader:'TextReader',validationType:XHTMLValidationType):
#        """
#    <summary>
#        Load document in html format
#    </summary>
#    <param name="reader">Reader of html code.</param>
#    <param name="validationType">XHTML validation type.</param>
#        """
#        intPtrreader:c_void_p = reader.Ptr
#        enumvalidationType:c_int = validationType.value
#
#        GetDllLibDoc().Document_LoadHTMLRV.argtypes=[c_void_p ,c_void_p,c_int]
#        GetDllLibDoc().Document_LoadHTMLRV(self.Ptr, intPtrreader,enumvalidationType)


    @dispatch

    def LoadText(self ,fileName:str):
        """
    <summary>
        Opens the text document from a file with default encoding utf-8.
    </summary>
    <param name="fileName">Name of the file.</param>
        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_LoadText.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_LoadText(self.Ptr, fileNamePtr)

    @dispatch

    def LoadText(self ,stream:Stream):
        """
    <summary>
        Opens the text document from a stream with default encoding utf-8.
    </summary>
    <param name="stream">The stream.</param>
        """
        intPtrstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_LoadTextS.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_LoadTextS(self.Ptr, intPtrstream)

    @dispatch

    def LoadText(self ,fileName:str,encoding:Encoding):
        """
    <summary>
        Opens the text document with specified encoding from a file.
    </summary>
    <param name="fileName">Name of the file.</param>
    <param name="encoding">The encoding</param>
        """
        fileNamePtr = StrToPtr(fileName)
        intPtrencoding:c_void_p = encoding.Ptr

        GetDllLibDoc().Document_LoadTextFE.argtypes=[c_void_p ,c_char_p,c_void_p]
        GetDllLibDoc().Document_LoadTextFE(self.Ptr, fileNamePtr,intPtrencoding)

    @dispatch

    def LoadText(self ,stream:Stream,encoding:Encoding):
        """
    <summary>
        Opens the text document with specified encoding from a stream.
    </summary>
    <param name="stream">The text document stream.</param>
    <param name="encoding">The encoding</param>
        """
        intPtrstream:c_void_p = stream.Ptr
        intPtrencoding:c_void_p = encoding.Ptr

        GetDllLibDoc().Document_LoadTextSE.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().Document_LoadTextSE(self.Ptr, intPtrstream,intPtrencoding)

#    @dispatch
#
#    def LoadText(self ,reader:'TextReader'):
#        """
#    <summary>
#        Opens the rtf document with specified encoding from a reader.
#    </summary>
#    <param name="reader">The rtf document reader</param>
#        """
#        intPtrreader:c_void_p = reader.Ptr
#
#        GetDllLibDoc().Document_LoadTextR.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().Document_LoadTextR(self.Ptr, intPtrreader)


    @dispatch

    def LoadFromFile(self ,fileName:str):
        """
    <summary>
        Opens doc file.
    </summary>
    <param name="fileName"></param>
        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_LoadFromFile.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_LoadFromFile(self.Ptr, fileNamePtr)

    @dispatch

    def LoadFromFile(self ,fileName:str,fileFormat:FileFormat):
        """
    <summary>
        Opens the document from file in Xml or Microsoft Word format.
    </summary>
    <param name="fileName"></param>
    <param name="formatType"></param>
        """
        fileNamePtr = StrToPtr(fileName)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_LoadFromFileFF.argtypes=[c_void_p ,c_char_p,c_int]
        GetDllLibDoc().Document_LoadFromFileFF(self.Ptr, fileNamePtr,enumfileFormat)

    @dispatch

    def LoadFromFile(self ,fileName:str,fileFormat:FileFormat,validationType:XHTMLValidationType):
        """
    <summary>
        Opens the HTML document from stream .
    </summary>
    <param name="fileName">Name of the file.</param>
    <param name="formatType">Type of the format.</param>
    <param name="validationType">Type of the validation.</param>
        """
        fileNamePtr = StrToPtr(fileName)

        enumfileFormat:c_int = fileFormat.value
        enumvalidationType:c_int = validationType.value

        GetDllLibDoc().Document_LoadFromFileFFV.argtypes=[c_void_p ,c_char_p,c_int,c_int]
        GetDllLibDoc().Document_LoadFromFileFFV(self.Ptr, fileNamePtr,enumfileFormat,enumvalidationType)

    @dispatch

    def LoadFromFile(self ,fileName:str,fileFormat:FileFormat,password:str):
        """
    <summary>
        Opens the document from file in Xml or Microsoft Word format.
    </summary>
    <param name="fileName">Name of the file.</param>
    <param name="formatType">Type of the format.</param>
    <param name="password">The password.</param>
        """
        fileNamePtr = StrToPtr(fileName)
        passwordPtr = StrToPtr(password)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_LoadFromFileFFP.argtypes=[c_void_p ,c_char_p,c_int,c_char_p]
        GetDllLibDoc().Document_LoadFromFileFFP(self.Ptr, fileNamePtr,enumfileFormat,passwordPtr)


    def LoadFromFileInReadMode(self ,strFileName:str,fileFormat:'FileFormat'):
        """
    <summary>
        LoadFromStream new document in read-only mode.
    </summary>
    <param name="strFileName">File to open.</param>
    <param name="formatType">Type of the format.</param>
        """
        strFileNamePtr = StrToPtr(strFileName)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_LoadFromFileInReadMode.argtypes=[c_void_p ,c_char_p,c_int]
        GetDllLibDoc().Document_LoadFromFileInReadMode(self.Ptr, strFileNamePtr,enumfileFormat)

    @dispatch

    def LoadRtf(self ,fileName:str):
        """
    <summary>
        Opens the rtf document from a file.
    </summary>
    <param name="fileName">Name of the file.</param>
        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_LoadRtf.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_LoadRtf(self.Ptr, fileNamePtr)

    @dispatch

    def LoadRtf(self ,stream:Stream):
        """
    <summary>
        Opens the rtf document from a stream.
    </summary>
    <param name="stream">The stream.</param>
        """
        intPtrstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_LoadRtfS.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_LoadRtfS(self.Ptr, intPtrstream)

    @dispatch

    def LoadRtf(self ,fileName:str,encoding:Encoding):
        """
    <summary>
        Opens the rtf document with specified encoding from a file.
    </summary>
    <param name="fileName">Name of the file.</param>
    <param name="encoding">The encoding</param>
        """
        fileNamePtr = StrToPtr(fileName)
        intPtrencoding:c_void_p = encoding.Ptr

        GetDllLibDoc().Document_LoadRtfFE.argtypes=[c_void_p ,c_char_p,c_void_p]
        GetDllLibDoc().Document_LoadRtfFE(self.Ptr, fileNamePtr,intPtrencoding)

    @dispatch

    def LoadRtf(self ,stream:Stream,encoding:Encoding):
        """
    <summary>
        Opens the rtf document with specified encoding from a stream.
    </summary>
    <param name="stream">The rtf document stream.</param>
    <param name="encoding">The encoding</param>
        """
        intPtrstream:c_void_p = stream.Ptr
        intPtrencoding:c_void_p = encoding.Ptr

        GetDllLibDoc().Document_LoadRtfSE.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().Document_LoadRtfSE(self.Ptr, intPtrstream,intPtrencoding)

#    @dispatch
#
#    def LoadRtf(self ,reader:'TextReader'):
#        """
#    <summary>
#        Opens the rtf document with specified encoding from a reader.
#    </summary>
#    <param name="reader">The rtf document reader</param>
#        """
#        intPtrreader:c_void_p = reader.Ptr
#
#        GetDllLibDoc().Document_LoadRtfR.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().Document_LoadRtfR(self.Ptr, intPtrreader)


    @dispatch

    def SaveToFile(self ,fileName:str):
        """
    <summary>
        Saves to file in Microsoft Word format.
    </summary>
    <param name="fileName"></param>
        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_SaveToFileF.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_SaveToFileF(self.Ptr, fileNamePtr)

    @dispatch

    def SaveToFile(self ,fileName:str,paramList:ToPdfParameterList):
        """
    <summary>
        Saves the document to PDF file.
    </summary>
    <param name="fileName">File name</param>
    <param name="paramList">Parameter list</param>
        """
        fileNamePtr = StrToPtr(fileName)
        intPtrparamList:c_void_p = paramList.Ptr

        GetDllLibDoc().Document_SaveToFileFP.argtypes=[c_void_p ,c_char_p,c_void_p]
        GetDllLibDoc().Document_SaveToFileFP(self.Ptr, fileNamePtr,intPtrparamList)

    @dispatch

    def SaveToEpub(self ,fileName:str,coverImage:DocPicture):
        """
    <summary>
        Saves the EPUB document.
    </summary>
    <param name="fileName">The file name.</param>
    <param name="coverImage">The cover image.</param>
        """
        fileNamePtr = StrToPtr(fileName)
        intPtrcoverImage:c_void_p = coverImage.Ptr

        GetDllLibDoc().Document_SaveToEpub.argtypes=[c_void_p ,c_char_p,c_void_p]
        GetDllLibDoc().Document_SaveToEpub(self.Ptr, fileNamePtr,intPtrcoverImage)

    @dispatch

    def SaveToEpub(self ,stream:Stream,coverImage:DocPicture):
        """
    <summary>
        Saves the EPUB document.
    </summary>
    <param name="stream">The stream.</param>
    <param name="coverImage">The cover image.</param>
        """
        intPtrstream:c_void_p = stream.Ptr
        intPtrcoverImage:c_void_p = coverImage.Ptr

        GetDllLibDoc().Document_SaveToEpubSC.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().Document_SaveToEpubSC(self.Ptr, intPtrstream,intPtrcoverImage)


    def InsertTextFromFile(self ,fileName:str,fileFormat:'FileFormat'):
        """
    <summary>
        Insert text from a file.
    </summary>
    <param name="fileName">File name</param>
    <param name="fileFormat">Type of the format</param>
        """
        fileNamePtr = StrToPtr(fileName)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_InsertTextFromFile.argtypes=[c_void_p ,c_char_p,c_int]
        GetDllLibDoc().Document_InsertTextFromFile(self.Ptr, fileNamePtr,enumfileFormat)


    def InsertTextFromStream(self ,stream:'Stream',fileFormat:'FileFormat'):
        """
    <summary>
        Insert text from stream.
    </summary>
    <param name="stream">The stream.</param>
    <param name="fileFormat">Type of the format</param>
        """
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_InsertTextFromStream.argtypes=[c_void_p ,c_void_p,c_int]
        GetDllLibDoc().Document_InsertTextFromStream(self.Ptr, intPtrstream,enumfileFormat)

    @dispatch

    def SaveToFile(self ,fileName:str,fileFormat:FileFormat):
        """
    <summary>
        Saves the document to file in Xml or Microsoft Word format.
    </summary>
    <param name="fileName">File name</param>
    <param name="formatType">Type of the format</param>
        """
        fileNamePtr = StrToPtr(fileName)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_SaveToFileFF.argtypes=[c_void_p ,c_char_p,c_int]
        GetDllLibDoc().Document_SaveToFileFF(self.Ptr, fileNamePtr,enumfileFormat)

    @dispatch

    def SaveToSVG(self ,fileName:str):
        """
    <summary>
        Saves the SVG.
    </summary>
    <param name="fileName">The file name.</param>
        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_SaveToSVG.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_SaveToSVG(self.Ptr, fileNamePtr)

#    @dispatch
#
#    def SaveToSVG(self)->Queue1:
#        """
#    <summary>
#        Saves the SVG.
#    </summary>
#        """
#        GetDllLibDoc().Document_SaveToSVG1.argtypes=[c_void_p]
#        GetDllLibDoc().Document_SaveToSVG1.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_SaveToSVG1(self.Ptr)
#        ret = None if intPtr==None else Queue1(intPtr)
#        return ret
#


    @property
    def PageCount(self)->int:
        """
    <summary>
        Gets total number of pages for document.
    </summary>
        """
        GetDllLibDoc().Document_get_PageCount.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_PageCount.restype=c_int
        ret = GetDllLibDoc().Document_get_PageCount(self.Ptr)
        return ret

    @property
    def IsContainMacro(self)->bool:
        """
    <summary>
        Indicates whether the document has macros.
    </summary>
        """
        GetDllLibDoc().Document_get_IsContainMacro.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_IsContainMacro.restype=c_bool
        ret = GetDllLibDoc().Document_get_IsContainMacro(self.Ptr)
        return ret

    @property
    def KeepSameFormat(self)->bool:
        """
    <summary>
        Gets or sets a value that indicates whether to keep same formatting when this document is merged to other document.
    </summary>
        """
        GetDllLibDoc().Document_get_KeepSameFormat.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_KeepSameFormat.restype=c_bool
        ret = GetDllLibDoc().Document_get_KeepSameFormat(self.Ptr)
        return ret

    @KeepSameFormat.setter
    def KeepSameFormat(self, value:bool):
        GetDllLibDoc().Document_set_KeepSameFormat.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_KeepSameFormat(self.Ptr, value)

    @property
    def UseNewEngine(self)->bool:
        """
    <summary>
        Gets a value indicating whether the new engine layout is enabled.
            The Spire.Doc product conversion feature has enabled the new engine way layout by default.
            If you want to switch to the old engine layout, use the Document constructor
            with the \"useNewEngine\" parameter and set the parameter \"useNewEngine\" to false.
    </summary>
        """
        GetDllLibDoc().Document_get_UseNewEngine.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_UseNewEngine.restype=c_bool
        ret = GetDllLibDoc().Document_get_UseNewEngine(self.Ptr)
        return ret


    def add_EvalInformation(self ,value:'SpireDocEvalInfo'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_add_EvalInformation.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_add_EvalInformation(self.Ptr, intPtrvalue)


    def remove_EvalInformation(self ,value:'SpireDocEvalInfo'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_remove_EvalInformation.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_remove_EvalInformation(self.Ptr, intPtrvalue)


    def add_BookmarkLayout(self ,value:'BookmarkLevelHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_add_BookmarkLayout.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_add_BookmarkLayout(self.Ptr, intPtrvalue)


    def remove_BookmarkLayout(self ,value:'BookmarkLevelHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_remove_BookmarkLayout.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_remove_BookmarkLayout(self.Ptr, intPtrvalue)


    def add_PageLayout(self ,value:'PageLayoutHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_add_PageLayout.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_add_PageLayout(self.Ptr, intPtrvalue)


    def remove_PageLayout(self ,value:'PageLayoutHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_remove_PageLayout.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_remove_PageLayout(self.Ptr, intPtrvalue)


    def add_UpdateFields(self ,value:'UpdateFieldsHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_add_UpdateFields.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_add_UpdateFields(self.Ptr, intPtrvalue)


    def remove_UpdateFields(self ,value:'UpdateFieldsHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_remove_UpdateFields.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_remove_UpdateFields(self.Ptr, intPtrvalue)

    @property

    def TOC(self)->'TableOfContent':
        """
    <summary>
        Gets or sets the TOC element of the word document.
    </summary>
        """
        GetDllLibDoc().Document_get_TOC.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_TOC.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_TOC(self.Ptr)
        ret = None if intPtr==None else TableOfContent(intPtr)
        return ret


    @TOC.setter
    def TOC(self, value:'TableOfContent'):
        GetDllLibDoc().Document_set_TOC.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().Document_set_TOC(self.Ptr, value.Ptr)

    @property
    def EmbedFontsInFile(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether save fonts that are used in the document in the file.
            Only support for the DOCX file format.
    </summary>
        """
        GetDllLibDoc().Document_get_EmbedFontsInFile.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_EmbedFontsInFile.restype=c_bool
        ret = GetDllLibDoc().Document_get_EmbedFontsInFile(self.Ptr)
        return ret

    @EmbedFontsInFile.setter
    def EmbedFontsInFile(self, value:bool):
        GetDllLibDoc().Document_set_EmbedFontsInFile.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_EmbedFontsInFile(self.Ptr, value)

    @property

    def PrivateFontList(self)->List[PrivateFontPath]:
        """
    <summary>
        Gets the private font list.
    </summary>
        """
        GetDllLibDoc().Document_get_PrivateFontList.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_PrivateFontList.restype=IntPtrArray
        intPtr = GetDllLibDoc().Document_get_PrivateFontList(self.Ptr)
        ret = GetVectorFromArray(intPtr,PrivateFontPath)
        return ret



    @property
    def EmbedSystemFonts(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether save system fonts that are used in the document in the file.
    </summary>
        """
        GetDllLibDoc().Document_get_EmbedSystemFonts.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_EmbedSystemFonts.restype=c_bool
        ret = GetDllLibDoc().Document_get_EmbedSystemFonts(self.Ptr)
        return ret

    @EmbedSystemFonts.setter
    def EmbedSystemFonts(self, value:bool):
        GetDllLibDoc().Document_set_EmbedSystemFonts.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_EmbedSystemFonts(self.Ptr, value)

    @property

    def HtmlBaseUrl(self)->str:
        """
    <summary>
        Gets or sets the Base path which is used to convert the relative path to absolute path.
    </summary>
        """
        GetDllLibDoc().Document_get_HtmlBaseUrl.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HtmlBaseUrl.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().Document_get_HtmlBaseUrl(self.Ptr))
        return ret


    @HtmlBaseUrl.setter
    def HtmlBaseUrl(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Document_set_HtmlBaseUrl.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().Document_set_HtmlBaseUrl(self.Ptr, valuePtr)

    @property
    def HTMLTrackChanges(self)->bool:
        """
<summary>
  <para>Gets or sets a value specifying whether parsing and writing custom Change_Tracking HTML Tags are supported.</para>
  <para>Supported HTML Tag : insert / delete.</para>
  <para>Supported HTML Tag Attribytes : data-username / data-time.</para>
</summary>
        """
        GetDllLibDoc().Document_get_HTMLTrackChanges.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HTMLTrackChanges.restype=c_bool
        ret = GetDllLibDoc().Document_get_HTMLTrackChanges(self.Ptr)
        return ret

    @HTMLTrackChanges.setter
    def HTMLTrackChanges(self, value:bool):
        GetDllLibDoc().Document_set_HTMLTrackChanges.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_HTMLTrackChanges(self.Ptr, value)

    @property
    def HTMLSentenceIdentifier(self)->bool:
        """
<summary>
  <para>Gets or sets a value specifying whether to add identifier to a sentence when writing to HTML.</para>
  <para>Writed HTML Attribyte : sentence.</para>
  <para>Writed HTML Value Of Attribyte : start / end / (start,end).</para>
</summary>
        """
        GetDllLibDoc().Document_get_HTMLSentenceIdentifier.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HTMLSentenceIdentifier.restype=c_bool
        ret = GetDllLibDoc().Document_get_HTMLSentenceIdentifier(self.Ptr)
        return ret

    @HTMLSentenceIdentifier.setter
    def HTMLSentenceIdentifier(self, value:bool):
        GetDllLibDoc().Document_set_HTMLSentenceIdentifier.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_HTMLSentenceIdentifier(self.Ptr, value)

    @property
    def HTMLCustomComment(self)->bool:
        """
<summary>
  <para>Gets or sets a value specifying whether parsing and writing comment of document in HTML.</para>
  <para>Supported HTML Tag : span ,when the value of class attribute is comment</para>
  <para>Supported HTML Tag Attribytes : data-comment / data-user / data-cid / data-date.</para>
</summary>
        """
        GetDllLibDoc().Document_get_HTMLCustomComment.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HTMLCustomComment.restype=c_bool
        ret = GetDllLibDoc().Document_get_HTMLCustomComment(self.Ptr)
        return ret

    @HTMLCustomComment.setter
    def HTMLCustomComment(self, value:bool):
        GetDllLibDoc().Document_set_HTMLCustomComment.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_HTMLCustomComment(self.Ptr, value)

#    @property
#
#    def HTMLIdentifierPunctuations(self)->'List1':
#        """
#    <summary>
#        Set the custom punctuation as sentence indentifier.
#            Full stop, qusetion mark, exclamatory mark are default values.
#    </summary>
#        """
#        GetDllLibDoc().Document_get_HTMLIdentifierPunctuations.argtypes=[c_void_p]
#        GetDllLibDoc().Document_get_HTMLIdentifierPunctuations.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_get_HTMLIdentifierPunctuations(self.Ptr)
#        ret = None if intPtr==None else List1(intPtr)
#        return ret
#


#    @HTMLIdentifierPunctuations.setter
#    def HTMLIdentifierPunctuations(self, value:'List1'):
#        GetDllLibDoc().Document_set_HTMLIdentifierPunctuations.argtypes=[c_void_p, c_void_p]
#        GetDllLibDoc().Document_set_HTMLIdentifierPunctuations(self.Ptr, value.Ptr)


#    @property
#
#    def Footnotes(self)->'List1':
#        """
#    <summary>
#        Gets document footnotes.
#    </summary>
#        """
#        GetDllLibDoc().Document_get_Footnotes.argtypes=[c_void_p]
#        GetDllLibDoc().Document_get_Footnotes.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_get_Footnotes(self.Ptr)
#        ret = None if intPtr==None else List1(intPtr)
#        return ret
#


#    @property
#
#    def Endnotes(self)->'List1':
#        """
#    <summary>
#        Gets document endnotes.
#    </summary>
#        """
#        GetDllLibDoc().Document_get_Endnotes.argtypes=[c_void_p]
#        GetDllLibDoc().Document_get_Endnotes.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_get_Endnotes(self.Ptr)
#        ret = None if intPtr==None else List1(intPtr)
#        return ret
#


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
    <summary>
        Gets the type of the document object.
    </summary>
        """
        GetDllLibDoc().Document_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_DocumentObjectType.restype=c_int
        ret = GetDllLibDoc().Document_get_DocumentObjectType(self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def BuiltinDocumentProperties(self)->'BuiltinDocumentProperties':
        """
    <summary>
        Gets document built-in properties object.
    </summary>
        """
        GetDllLibDoc().Document_get_BuiltinDocumentProperties.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_BuiltinDocumentProperties.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_BuiltinDocumentProperties(self.Ptr)
        ret = None if intPtr==None else BuiltinDocumentProperties(intPtr)
        return ret


    @property

    def CustomDocumentProperties(self)->'CustomDocumentProperties':
        """
    <summary>
        Gets document custom properties object.
    </summary>
        """
        GetDllLibDoc().Document_get_CustomDocumentProperties.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_CustomDocumentProperties.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_CustomDocumentProperties(self.Ptr)
        ret = None if intPtr==None else CustomDocumentProperties(intPtr)
        return ret


    @property

    def Sections(self)->SectionCollection:
        """
    <summary>
        Gets document sections.
    </summary>
        """
        GetDllLibDoc().Document_get_Sections.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Sections.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_Sections(self.Ptr)
        ret = None if intPtr==None else SectionCollection(intPtr)
        return ret


    @property

    def Styles(self)->'StyleCollection':
        """
    <summary>
        Gets document styles.
    </summary>
        """
        GetDllLibDoc().Document_get_Styles.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Styles.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_Styles(self.Ptr)
        from spire.doc import StyleCollection
        ret = None if intPtr==None else StyleCollection(intPtr)
        return ret


    @property

    def ListStyles(self)->'ListStyleCollection':
        """
    <summary>
        Gets document list styles.
    </summary>
        """
        GetDllLibDoc().Document_get_ListStyles.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ListStyles.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_ListStyles(self.Ptr)
        from spire.doc import ListStyleCollection
        ret = None if intPtr==None else ListStyleCollection(intPtr)
        return ret


    @property

    def Bookmarks(self)->'BookmarkCollection':
        """
    <summary>
        Gets document bookmarks.
    </summary>
        """
        GetDllLibDoc().Document_get_Bookmarks.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Bookmarks.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_Bookmarks(self.Ptr)
        ret = None if intPtr==None else BookmarkCollection(intPtr)
        return ret


    @property

    def Fields(self)->'FieldCollection':
        """
    <summary>
        Gets fields of the documnet.
    </summary>
        """
        GetDllLibDoc().Document_get_Fields.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Fields.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_Fields(self.Ptr)
        from spire.doc import FieldCollection
        ret = None if intPtr==None else FieldCollection(intPtr)
        return ret


    @property

    def Comments(self)->'CommentsCollection':
        """
    <summary>
        Gets comments item of the document.
    </summary>
        """
        GetDllLibDoc().Document_get_Comments.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Comments.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_Comments(self.Ptr)
        ret = None if intPtr==None else CommentsCollection(intPtr)
        return ret


    @property

    def TextBoxes(self)->'TextBoxCollection':
        """
    <summary>
        Get/set textbox items of main document
    </summary>
        """
        GetDllLibDoc().Document_get_TextBoxes.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_TextBoxes.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_TextBoxes(self.Ptr)
        from spire.doc import TextBoxCollection
        ret = None if intPtr==None else TextBoxCollection(intPtr)
        return ret


    @TextBoxes.setter
    def TextBoxes(self, value:'TextBoxCollection'):
        GetDllLibDoc().Document_set_TextBoxes.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().Document_set_TextBoxes(self.Ptr, value.Ptr)

    @property

    def LastSection(self)->'Section':
        """
    <summary>
        Gets last section of the document.
    </summary>
        """
        GetDllLibDoc().Document_get_LastSection.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_LastSection.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_LastSection(self.Ptr)
        ret = None if intPtr==None else Section(intPtr)
        return ret


    @property

    def LastParagraph(self)->'Paragraph':
        """
    <summary>
        Gets last section object.
    </summary>
        """
        GetDllLibDoc().Document_get_LastParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_LastParagraph.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_LastParagraph(self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @property

    def EndnoteOptions(self)->'FootEndnoteOptions':
        """
    <summary>
        Gets or sets options that control numbering and positioning of endnotes in this document. 
    </summary>
        """
        GetDllLibDoc().Document_get_EndnoteOptions.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_EndnoteOptions.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_EndnoteOptions(self.Ptr)
        ret = None if intPtr==None else FootEndnoteOptions(intPtr)
        return ret


    @property

    def FootnoteOptions(self)->'FootEndnoteOptions':
        """
    <summary>
         Gets or sets options that control numbering and positioning of footnotes in this document. 
    </summary>
        """
        GetDllLibDoc().Document_get_FootnoteOptions.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_FootnoteOptions.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_FootnoteOptions(self.Ptr)
        ret = None if intPtr==None else FootEndnoteOptions(intPtr)
        return ret


    @property

    def Watermark(self)->'WatermarkBase':
        """
    <summary>
        Gets or sets document's watermark.
    </summary>
        """
        GetDllLibDoc().Document_get_Watermark.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Watermark.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_Watermark(self.Ptr)
        ret = None if intPtr==None else WatermarkBase(intPtr)
        return ret


    @Watermark.setter
    def Watermark(self, value:'WatermarkBase'):
        GetDllLibDoc().Document_set_Watermark.argtypes=[c_void_p, c_void_p]
        if value == None:
            GetDllLibDoc().Document_set_Watermark(self.Ptr, None)
        else: 
            GetDllLibDoc().Document_set_Watermark(self.Ptr, value.Ptr)

    @property

    def Background(self)->'Background':
        """
    <summary>
        Gets document's background
    </summary>
        """
        GetDllLibDoc().Document_get_Background.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Background.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_Background(self.Ptr)
        ret = None if intPtr==None else Background(intPtr)
        return ret


    @property

    def MailMerge(self)->'MailMerge':
        """
    <summary>
        Gets mail merge engine.
    </summary>
        """
        GetDllLibDoc().Document_get_MailMerge.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_MailMerge.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_MailMerge(self.Ptr)
        ret = None if intPtr==None else MailMerge(intPtr)
        return ret



    def GetProtectionType(self)->'ProtectionType':
        """
    <summary>
        Gets or sets the type of protection of the document.
    </summary>
        """
        GetDllLibDoc().Document_get_ProtectionType.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ProtectionType.restype=c_int
        ret = GetDllLibDoc().Document_get_ProtectionType(self.Ptr)
        objwraped = ProtectionType(ret)
        return objwraped

    def SetProtectionType(self, value:'ProtectionType'):
        GetDllLibDoc().Document_set_ProtectionType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Document_set_ProtectionType(self.Ptr, value.value)

    @property

    def ViewSetup(self)->'ViewSetup':
        """
    <summary>
        Gets view setup options in Microsoft word.
    </summary>
        """
        GetDllLibDoc().Document_get_ViewSetup.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ViewSetup.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_ViewSetup(self.Ptr)
        from spire.doc import ViewSetup
        ret = None if intPtr==None else ViewSetup(intPtr)
        return ret


    @property
    def QuiteMode(self)->bool:
        """
    <summary>
        Get / sets whether is quite mode.
    </summary>
        """
        GetDllLibDoc().Document_get_QuiteMode.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_QuiteMode.restype=c_bool
        ret = GetDllLibDoc().Document_get_QuiteMode(self.Ptr)
        return ret

    @QuiteMode.setter
    def QuiteMode(self, value:bool):
        GetDllLibDoc().Document_set_QuiteMode.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_QuiteMode(self.Ptr, value)

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
    <summary>
        Gets the child entities.
    </summary>
<value>The child entities.</value>
        """
        GetDllLibDoc().Document_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ChildObjects.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_ChildObjects(self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def XHTMLValidateOption(self)->'XHTMLValidationType':
        """
    <summary>
        Gets or sets the HTML validate option.the default value is None.
    </summary>
<value>The HTML validate option.</value>
        """
        GetDllLibDoc().Document_get_XHTMLValidateOption.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_XHTMLValidateOption.restype=c_int
        ret = GetDllLibDoc().Document_get_XHTMLValidateOption(self.Ptr)
        objwraped = XHTMLValidationType(ret)
        return objwraped

    @XHTMLValidateOption.setter
    def XHTMLValidateOption(self, value:'XHTMLValidationType'):
        GetDllLibDoc().Document_set_XHTMLValidateOption.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Document_set_XHTMLValidateOption(self.Ptr, value.value)

    @property

    def Variables(self)->'VariableCollection':
        """
    <summary>
        Gets or sets the document variables.
    </summary>
    <value>The variables.</value>
        """
        GetDllLibDoc().Document_get_Variables.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Variables.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_Variables(self.Ptr)
        from spire.doc import VariableCollection
        ret = None if intPtr==None else VariableCollection(intPtr)
        return ret


    @property

    def Properties(self)->'DocumentProperties':
        """
    <summary>
        Gets the document properties.
    </summary>
<value>The properties.</value>
        """
        GetDllLibDoc().Document_get_Properties.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Properties.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_Properties(self.Ptr)
        ret = None if intPtr==None else DocumentProperties(intPtr)
        return ret


    @property
    def HasChanges(self)->bool:
        """
    <summary>
        Gets a value indicating whether the document has tracked changes.
    </summary>
<value>
            	if the document has tracked changes, set to <c>true</c>.
            </value>
        """
        GetDllLibDoc().Document_get_HasChanges.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HasChanges.restype=c_bool
        ret = GetDllLibDoc().Document_get_HasChanges(self.Ptr)
        return ret

    @property
    def TrackChanges(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether tracking changes is turn on.
    </summary>
<value>if track changes in on, set to <c>true</c>.</value>
        """
        GetDllLibDoc().Document_get_TrackChanges.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_TrackChanges.restype=c_bool
        ret = GetDllLibDoc().Document_get_TrackChanges(self.Ptr)
        return ret

    @TrackChanges.setter
    def TrackChanges(self, value:bool):
        GetDllLibDoc().Document_set_TrackChanges.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_TrackChanges(self.Ptr, value)

    @property
    def AutoUpdateStylesByTemplate(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether updating the styles in this document to match
            the styles in the attached template each time you open .
    </summary>
<value>if update document styles automatically, set to <c>true</c>.</value>
        """
        GetDllLibDoc().Document_get_AutoUpdateStylesByTemplate.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_AutoUpdateStylesByTemplate.restype=c_bool
        ret = GetDllLibDoc().Document_get_AutoUpdateStylesByTemplate(self.Ptr)
        return ret

    @AutoUpdateStylesByTemplate.setter
    def AutoUpdateStylesByTemplate(self, value:bool):
        GetDllLibDoc().Document_set_AutoUpdateStylesByTemplate.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_AutoUpdateStylesByTemplate(self.Ptr, value)

    @property
    def ReplaceFirst(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether need first replacing.
    </summary>
<value>True indciates need first replacing.</value>
        """
        GetDllLibDoc().Document_get_ReplaceFirst.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ReplaceFirst.restype=c_bool
        ret = GetDllLibDoc().Document_get_ReplaceFirst(self.Ptr)
        return ret

    @ReplaceFirst.setter
    def ReplaceFirst(self, value:bool):
        GetDllLibDoc().Document_set_ReplaceFirst.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_ReplaceFirst(self.Ptr, value)

    @property

    def HtmlExportOptions(self)->'HtmlExportOptions':
        """
    <summary>
        Gets the save options.
    </summary>
<value>The save options.</value>
        """
        GetDllLibDoc().Document_get_HtmlExportOptions.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HtmlExportOptions.restype=c_void_p
        intPtr = GetDllLibDoc().Document_get_HtmlExportOptions(self.Ptr)
        ret = None if intPtr==None else HtmlExportOptions(intPtr)
        return ret


    @property
    def IsUpdateFields(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to update fields in the document.
    </summary>
        """
        GetDllLibDoc().Document_get_IsUpdateFields.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_IsUpdateFields.restype=c_bool
        ret = GetDllLibDoc().Document_get_IsUpdateFields(self.Ptr)
        return ret

    @IsUpdateFields.setter
    def IsUpdateFields(self, value:bool):
        GetDllLibDoc().Document_set_IsUpdateFields.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().Document_set_IsUpdateFields(self.Ptr, value)

    @property

    def DetectedFormatType(self)->'FileFormat':
        """
    <summary>
        Returns the detected format type of the document which was loaded. .
    </summary>
        """
        GetDllLibDoc().Document_get_DetectedFormatType.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_DetectedFormatType.restype=c_int
        ret = GetDllLibDoc().Document_get_DetectedFormatType(self.Ptr)
        objwraped = FileFormat(ret)
        return objwraped

    @property
    def JPEGQuality(self)->int:
        """
    <summary>
        Gets/sets the quality (Q%) of the image of JPEG format, this property
            is only used for doc to pdf. The default value is 80. 
    </summary>
        """
        GetDllLibDoc().Document_get_JPEGQuality.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_JPEGQuality.restype=c_int
        ret = GetDllLibDoc().Document_get_JPEGQuality(self.Ptr)
        return ret

    @JPEGQuality.setter
    def JPEGQuality(self, value:int):
        GetDllLibDoc().Document_set_JPEGQuality.argtypes=[c_void_p, c_int]
        GetDllLibDoc().Document_set_JPEGQuality(self.Ptr, value)

