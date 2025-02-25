Set oWSH = CreateObject("WScript.Shell")
oWSH.Run "#INSERTCOMMANDTORUNPYTHONSCRIPTHERE",0,False

oWSH.Run "tailscale serve --bg 5000",0,False
