ControlFocus("打开","","Edit1")
;识别windows窗口
WinWait("[CLASS:#32770]","",10)
;窗口等待十秒
ControlSetText("打开", "", "Edit1", "C:\Cnstrong\file\lesson\auto_paike\最新选修班.xls")
;想输入框中输入需要上传的地址
Sleep(2000)
ControlClick("打开", "","Button1");
;点击[打开】按钮