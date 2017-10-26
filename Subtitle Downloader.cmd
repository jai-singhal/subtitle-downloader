@echo off
cls
echo Executing...
IF EXIST C:\ProgramData\Anaconda3\python.exe\ SET PATH=%PATH%;C:\ProgramData\Anaconda3\python.exe\
:my_loop
IF %1=="" GOTO completed
  python "E:\G drive\Python\subtitle_downloader.py" %1
  SHIFT
  GOTO my_loop
:completed