@ECHO OFF
set /P c=Enter Red Value: 
set /P d=Enter Green Value: 
set /P e=Enter Blue Value: 
set /P f=Enter Alpha Value: 
Channel_Choose.py "%~nx1" %c% %d% %e% %f%
pause...
exit