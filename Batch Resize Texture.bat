@ECHO OFF
set /P c=Enter New Hight: 
set /P d=Enter New Width: 
set /P t=Nearest = 0, Lanczos = 1, Bilinear = 2, Bicubic = 3, Box = 4, Hamming = 5,: 
for %%Y in (*.png) do Resize_Textures.py "%%Y" %c% %d% %t%
pause
Exit
