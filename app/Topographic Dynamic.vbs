Option Explicit

Dim fso, shell, appFolder, repository, pythonw, script
Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")

appFolder = fso.GetParentFolderName(WScript.ScriptFullName)
repository = fso.GetParentFolderName(appFolder)
pythonw = shell.ExpandEnvironmentStrings("%USERPROFILE%") & "\Documents\Program buatan\.venv\Scripts\pythonw.exe"
script = repository & "\topographic.py"

If Not fso.FileExists(pythonw) Then
    MsgBox "Could not find the virtual environment Python executable:" & vbCrLf & pythonw, vbCritical, "Topographic Dynamic"
    WScript.Quit 1
End If

If Not fso.FileExists(script) Then
    MsgBox "Could not find the Python script:" & vbCrLf & script, vbCritical, "Topographic Dynamic"
    WScript.Quit 1
End If

shell.CurrentDirectory = repository
shell.Run """" & pythonw & """ """ & script & """", 0, False
