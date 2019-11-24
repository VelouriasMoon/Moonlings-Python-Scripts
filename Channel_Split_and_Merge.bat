@ECHO OFF
set /P c=Split Channels or Merge?: 
Channel_Split_and_Merge.py %c% "%~nx1" "%~nx2"
