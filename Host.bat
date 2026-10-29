@echo off
set output_dir=%cd%\output

for /f %%f in ('dir "%output_dir%\*.zip" /b /a-d /o-d /tc') do (
    echo %%f
    set filename=%output_dir%\%%f
    goto runserver
)

:runserver
python MultiServer.py "%filename%"
pause