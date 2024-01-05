python -m PyQt6.uic.pyuic -o ui_form.py -x form.ui

@echo off
setlocal enabledelayedexpansion

set "file_path=ui_form.py"
set "old_word=PyQt6"
set "new_word=PySide6"

set "temp_file=temp.txt"

(for /f "delims=" %%i in (%file_path%) do (
    set "line=%%i"
    set "line=!line:%old_word%=%new_word%!"
    echo !line!
)) > %temp_file%

xcopy /y %temp_file% %file_path%
del /q %temp_file%

@REM echo Word '%old_word%' replaced with '%new_word%' in %file_path% successfully.
