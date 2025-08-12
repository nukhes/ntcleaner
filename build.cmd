@echo off
pip install pyinstaller
pyinstaller --onefile --noconsole --strip --clean --name ntcleaner src\main.py
dist\ntcleaner.exe -h
