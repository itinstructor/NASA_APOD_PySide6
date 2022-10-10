cd c:\temp

python -m nuitka ^
    --onefile ^
    --disable-ccache ^
    --plugin-enable=pyside6 ^
    --windows-disable-console ^
    --windows-icon-from-ico=telescope-icon-24300-Windows.ico ^
    apod_program.py
pause