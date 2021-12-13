@echo off
:: if running as vbscript, goto executing python
if "%1" == "vbs" goto begin

:: show *.json files which are candidate maps
for %%f in (*.json) do (
    echo %%f
)
echo please enter file name:
set /p file=

:: restart as vbscript, and close current cmd window
mshta vbscript:createobject("wscript.shell").run("%~nx0 vbs",0)(window.close)&&exit

:begin
python D:\code\github\topology-graph-view-python\main.py %file%