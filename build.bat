@echo off

IF NOT EXIST "yt-dlp" (
    mkdir yt-dlp
)

IF NOT EXIST "yt-dlp\yt-dlp.exe" (
    echo Downloading yt-dlp...
    curl -L "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe" --output "yt-dlp\yt-dlp.exe"
)

IF NOT EXIST "rick.webm" (
    echo Downloading video...
    yt-dlp.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o "rick.webm"
)

IF NOT EXIST "vlc" (
    mkdir vlc
)

IF NOT EXIST "vlc\vlc.zip" (
    echo Downloading vlc...
    curl -L "https://get.videolan.org/vlc/3.0.23/win32/vlc-3.0.23-win32.zip" --output "vlc\vlc.zip"
)

IF NOT EXIST "binaries" (
    mkdir binaries
)

::Be sure to change these icons to what you want!

echo Building executables...

pyinstaller --noconfirm --onefile --console --icon=icons\icon.ico text.py
rmdir /S /Q build
del text.spec
move dist\text.exe .\binaries
rmdir /Q dist

pyinstaller --noconfirm --onefile --noconsole --icon=icons\icon.ico --add-data "rick.webm;." --add-data "binaries\text.exe;." --add-data "vlc\vlc.zip;." main.py
rmdir /S /Q build
del main.spec
move dist\main.exe .\binaries
rmdir /Q dist

del .\binaries\text.exe

echo Finished build!