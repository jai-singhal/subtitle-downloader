# Any Subtitle Downloader
This is a simple Python Script to download subtitle of any video(tv show/ movies) in English in single click.

This scripts uses and API http://thesubdb.com/api/, to get the hash code of the given file

## Usage
This is currently available for windows users only

Step 1: Change the `Subtitle Downloader.cmd` according to your path. For example

Channge the `python.exe` path in `SET PATH` and location of `subtitle_downloader.py`

```
@echo off
cls
echo "Executing..."
IF EXIST C:\ProgramData\Anaconda3\python.exe\ SET PATH=%PATH%;C:\ProgramData\Anaconda3\python.exe\
:my_loop
IF %1=="" GOTO completed
  python "<location of the subtitle_downloader.py>" %1
  SHIFT
  GOTO my_loop
:completed
```

Step 2: Copy the `Subtitle Downloader.cmd` to `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\SendTo` or you can navigate to this 
folder by writing in address bar `shell:sendto` 

Step 3: Finish

## Screenshots
![1](https://user-images.githubusercontent.com/17959450/32063307-74505210-ba94-11e7-8dbf-aa60b0883c27.png)

![2](https://user-images.githubusercontent.com/17959450/32063308-747d1944-ba94-11e7-9265-f09685cf9169.png)

![3](https://user-images.githubusercontent.com/17959450/32063309-74b2501e-ba94-11e7-8a48-dfb0897f3a1b.png)


