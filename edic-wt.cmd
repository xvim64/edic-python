@echo off
setlocal
pushd "%~dp0"

set wt="%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\wt.exe"
set py="PyEmbed\python.exe"

if exist %wt% (
    %wt% -F -d . %py% edic.py
) else (
    %py% edic.py
)
exit /b
