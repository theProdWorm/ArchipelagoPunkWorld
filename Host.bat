@echo off
setlocal
pushd "%~dp0"

set output_dir=%cd%\output

echo %output_dir%

for %%F in ("%output_dir%\*.zip") do (
    echo %%F

    set filename=%%F
    goto runserver
)

:runserver
python MultiServer.py "%filename%"