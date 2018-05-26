import ctypes
from ctypes import wintypes
import time


while True:

    class SYSTEM_POWER_STATUS(ctypes.Structure):
        _fields_ = [
            ('ACLineStatus', wintypes.BYTE),
            ('BatteryFlag', wintypes.BYTE),
            ('BatteryLifePercent', wintypes.BYTE),
            ('Reserved1', wintypes.BYTE),
            ('BatteryLifeTime', wintypes.DWORD),
            ('BatteryFullLifeTime', wintypes.DWORD),
    ]

    SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

    GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
    GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
    GetSystemPowerStatus.restype = wintypes.BOOL

    status = SYSTEM_POWER_STATUS()
    if not GetSystemPowerStatus(ctypes.pointer(status)):
            raise ctypes.WinError()
    #print ('ACLineStatus', status.ACLineStatus)
    #print ('BatteryFlag', status.BatteryFlag)
    #print ('BatteryLifePercent', status.BatteryLifePercent)
    #print ('BatteryLifeTime', status.BatteryLifeTime)
    #print ('BatteryFullLifeTime', status.BatteryFullLifeTime)
    
    var = str(status.ACLineStatus)


    text_file = open("C:\Python\Projects\BatteryOrAC\status.txt", "w")
    if (var == '1'):
        text_file.write("AC")
        print ("AC")
    if (var == '0'):
        text_file.write("BATTERY")
        print ("BATTERY")
    text_file.close()
    time.sleep(5)