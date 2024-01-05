pyrcc5 -o Resources_rc.py Resources.qrc

@echo off
setlocal enabledelayedexpansion

set "file_path=Resources_rc.py"
set "old_word=PyQt5"
set "new_word=PySide6"

set "temp_file=temp.txt"

(for /f "delims=" %%i in (%file_path%) do (
    set "line=%%i"
    set "line=!line:%old_word%=%new_word%!"
    echo !line!
)) > %temp_file%

xcopy /y %temp_file% %file_path%
del /q %temp_file%
