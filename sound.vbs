Set WshShell = WScript.CreateObject("WScript.Shell")
Do
for i = 0 to 50
WshShell.SendKeys(chr(175))
next
Loop
