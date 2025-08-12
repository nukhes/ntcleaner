@echo off
pip install --quiet pyinstaller

pyinstaller --onefile --strip --clean --name ntcleaner src\main.py

echo.
echo ===== Build finished. =====
echo.

dist\ntcleaner.exe -h

pause