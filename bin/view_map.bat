@echo off
:: show *.json files which are candidate maps
for %%f in (*.json) do (
    echo %%f
)
python D:\code\github\topology-graph-view-python\main.py

