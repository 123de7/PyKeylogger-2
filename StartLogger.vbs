Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run "<BATCH FILE PATH>", 0
Set WinScriptHost = Nothing
