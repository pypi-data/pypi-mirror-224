from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from ctypes import *
import abc

class License (SpireObject) :
    """

    """
    @staticmethod
    def SetLicenseFileFullPathByDLLHander(dllhander, licenseFileFullPath:str):
        licenseFileFullPathPtr = StrToPtr(licenseFileFullPath)
        if dllhander != None:
            dllhander.LISetLicenseFileFullPath.argtypes=[ c_char_p]
            dllhander.LISetLicenseFileFullPath(licenseFileFullPathPtr)
    @staticmethod
    def SetLicenseFileFullPath(licenseFileFullPath:str):
        """
        <summary>
            Provides a license by a license file path, which will be used for loading license.
        </summary>
		<param name="licenseFileFullPath">License file full path.</param>
        """
        licenseFileFullPathPtr = StrToPtr(licenseFileFullPath)
        License.SetLicenseFileFullPathByDLLHander(GetDllLibDoc(), licenseFileFullPathPtr)

    @staticmethod
    def SetLicenseKey(key:str):
        """
		<summary>    
    		Provides a license by a license key, which will be used for loading license.
		</summary>
		<param name="key">The value of the Key attribute of the element License of you license xml file.</param> 
        """
        keyPtr = StrToPtr(key)
        License.SetLicenseKeyByDLLHander(GetDllLibDoc(), keyPtr)

    @staticmethod
    def SetLicenseFileStream(stream:Stream):
        """
		<summary>
    		Provides a license by a license stream, which will be used for loading license.
		</summary>
		<param name="licenseFileStream">License data stream.</param>
        """
        License.SetLicenseFileStreamByDLLHander(GetDllLibDoc(), stream)
        
    @staticmethod
    def SetLicenseFileName(licenseFileName:str):
        """
		<summary>
		    Gets the current license file name.
		</summary>
		<returns>The license file name, the default license file name is [license.elic.xml].</returns>
        """
        licenseFileNamePtr = StrToPtr(licenseFileName)
        License.SetLicenseFileNameByDLLHander(GetDllLibDoc(), licenseFileNamePtr)

    @staticmethod
    def SetLicenseFileNameByDLLHander(dllhander, licenseFileName:str):
        licenseFileNamePtr = StrToPtr(licenseFileName)
        if dllhander != None:
            dllhander.LISetLicenseFileName.argtypes=[ c_char_p]
            dllhander.LISetLicenseFileName(licenseFileNamePtr)

    

    @staticmethod
    def SetLicenseFileStreamByDLLHander(dllhander, stream:Stream):
        if dllhander != None:
            intPtrobj:c_void_p = stream.Ptr
            dllhander.LISetLicenseFileStream.argtypes=[ c_void_p]
            dllhander.LISetLicenseFileStream( intPtrobj)

    

    @staticmethod
    def SetLicenseKeyByDLLHander(dllhander, key:str):
        keyPtr = StrToPtr(key)
        if dllhander != None:
            dllhander.LISetLicenseKey.argtypes=[ c_char_p]
            dllhander.LISetLicenseKey(keyPtr)

    @staticmethod
    def ClearLicense():
        """
		<summary>
		    Clear all cached license.
		</summary>
        """
        License.ClearLicenseByDLLHander(GetDllLibDoc())

    @staticmethod
    def ClearLicenseByDLLHander(dllhander):
        if dllhander != None:
            dllhander.LIClearLicense( )


    @staticmethod
    def LoadLicense():
        """
		<summary>
		    Load the license provided by current setting to the license cache.
		</summary>
        """
        License.LoadLicenseByDLLHander(GetDllLibDoc())

    @staticmethod
    def LoadLicenseByDLLHander(dllhander):
        if dllhander != None:
            dllhander.LILoadLicense( )
  #  @staticmethod
  #  def GetLicenseFileName()->str:
  #      """
		#<summary>
		#    Gets the current license file name.
		#</summary>
		#<returns>The license file name, the default license file name is [license.elic.xml].</returns>
  #      """
  #      ret = License.GetLicenseFileNameByDLLHander(GetDllLibDoc())
  #      if ret == None:
  #          ret = License.GetLicenseFileNameByDLLHander(GetDllLibPdf())
  #      if ret == None:
  #          ret = License.GetLicenseFileNameByDLLHander(GetDllLibXls())
  #      if ret == None:
  #          ret = License.GetLicenseFileNameByDLLHander(GetDllLibPpt())
  #      return ret
    @staticmethod
    def GetLicenseFileNameByDLLHander(dllhander)->str:
        if dllhander != None:
            dllhander.LIGetLicenseFileName.argtypes=[c_void_p]
            return dllhander.LIGetLicenseFileName( )
        return None