@echo off
REM Build the RPG engine as a standalone executable using PyInstaller
pip install pyinstaller
pyinstaller --onefile --name RPGEngine --icon game_icon.ico main_game.py
pause