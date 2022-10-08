cd c:\temp

python -m nuitka ^
    --onefile ^
    --disable-ccache ^
    --plugin-enable=pyside6 ^
    --windows-disable-console ^
    --windows-icon-from-ico=telescope.ico ^
    apod_program.py
pause