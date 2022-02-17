@echo off
setlocal
pushd "%~dp0"

set py="Py3Embed\python.exe"

%py% edic.py
exit /b
