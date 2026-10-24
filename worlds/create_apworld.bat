@echo off
setlocal
pushd "%~dp0"

set game=punk

if not exist "%game%\" (
    echo Error: the %game% directory was not found.
    popd
    pause
    exit /b 1
)

if exist "%game%.apworld" (
    del /f /q "%game%.apworld"
)

powershell.exe -NoProfile -Command "$ErrorActionPreference = 'Stop'; Compress-Archive -Path '.\%game%' -DestinationPath '.\%game%.zip'"
powershell.exe -NoProfile -Command "$ErrorActionPreference = 'Stop'; Rename-Item -Path '.\%game%.zip' -NewName '%game%.apworld'"
set "exitCode=%ERRORLEVEL%"

popd

if not "%exitCode%"=="0" (
    echo Error: failed to compress the %game% directory.
    pause
    exit /b %exitCode%
)

start "" "%game%.apworld"

echo Created worlds\%game%.apworld.