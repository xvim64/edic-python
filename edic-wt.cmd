@echo off
setlocal
pushd "%~dp0"

set wt="%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\wt.exe"
set py="Py3Embed\python.exe"

if exist %wt% (
    %wt% -F -p "��� ������Ʈ" -d . %py% edic.py
) else (
    %py% edic.py
)
exit /b
