@echo off
setlocal
pushd "%~dp0"

set /p yn="Build edic.sqlite (Y)es/(N)o : 
if /i "%yn%"=="y"   goto:_rebuild
if /i "%yn%"=="yes" goto:_rebuild
exit /b

:_rebuild
if exist edic.sqlite (
    del /f /q edic.sqlite || (
        echo ERROR: Cannot delete edic.sqlite
        exit /b 1
    )
)
"PyEmbed\python.exe" dic2sqlite.py
exit /b
