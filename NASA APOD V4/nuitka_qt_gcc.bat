cd c:\temp

python -m nuitka ^
    --lto=no ^
    --mingw64 ^
    --onefile ^
    --disable-ccache ^
    --enable-plugin=tk-inter ^
    --plugin-enable=pyside6 ^
    --windows-disable-console ^
    --windows-icon-from-ico=telescope-icon.ico ^
    -o apod_viewer.exe ^
    apod_program.py
pause