@echo off
setlocal
pushd "%~dp0"

set py="PyEmbed\python.exe"

%py% edic.py
exit /b
