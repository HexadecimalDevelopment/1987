# main.py

# 1987
# https://github.com/HexadecimalDevelopment/1987/\n\nCopyright 
# (C) 2026 Hunt Burke (Hexadecimal Development)
# Licensed under the GPL 3.0 (https://raw.githubusercontent.com/HexadecimalDevelopment/1987/refs/heads/main/LICENSE)
# This program and/or its authors are NOT affilliated with CISA in any way.

try:

    import os, sys, tempfile

    try:

        base = sys._MEIPASS

    except:

        base = os.getcwd()

    if os.path.exists(f'{tempfile.gettempdir()}/1987.lock'):

        sys.exit(1)

    else:

        open(f'{tempfile.gettempdir()}/1987.lock', 'w').close()

    import subprocess
    import zipfile
    import webbrowser
    import shutil

    if sys.platform == 'linux':

        linux = True
        filename = os.path.join(base, 'vlc_port')

    elif sys.platform == 'win32':

        linux = False
        filename = os.path.join(base, 'vlc.zip')

    if linux:

        subprocess.run(('chmod', '+x', f'{filename}'))

    else:

        with zipfile.ZipFile(filename, 'r') as file:
            file.extractall(tempfile.gettempdir())
        filename = os.path.join(tempfile.gettempdir(), file.namelist()[0], 'vlc.exe')

    subprocess.run((
                    f'{filename}',
                    '--no-qt-privacy-ask',
                    '--qt-minimal-view',
                    '--fullscreen',
                    '--no-video-title-show',
                    '--repeat',
                    '--meta-title=Oops, you downloaded a (fake) payload!',
                    os.path.join(base, 'rick.webm')),
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                    )

    if not linux:

        try:

            subprocess.run((os.path.join(base, 'text.exe')))

        except KeyboardInterrupt: pass

    webbrowser.open('https://www.cisa.gov/secure-our-world')

    os.remove(f'{tempfile.gettempdir()}/1987.lock')

    if not linux:
        try:
            shutil.rmtree(os.path.join(tempfile.gettempdir(), 'vlc'))
        except FileNotFoundError:
            pass

    sys.exit()

except KeyboardInterrupt:

    os.remove(f'{tempfile.gettempdir()}/1987.lock')

    if not linux:
        try:
            shutil.rmtree(os.path.join(tempfile.gettempdir(), 'vlc'))
        except FileNotFoundError:
            pass

    webbrowser.open('https://www.cisa.gov/secure-our-world')
    
    sys.exit()