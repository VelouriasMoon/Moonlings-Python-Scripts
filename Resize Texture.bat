@ECHO OFF
set /P c=Enter New Hight: 
set /P d=Enter New Width: 
set /P t=Nearest = 0, Lanczos = 1, Bilinear = 2, Bicubic = 3, Box = 4, Hamming = 5,: 
Resize_Textures.py "%~nx1" %c% %d% %t%
pause
Exit
