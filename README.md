# 1987

1987 is a program designed to educate people about the dangers of downloading random files from the internet. When executed, it plays the official music video of "Never Gonna Give You Up" by Rick Astley, opens a terminal window with messages about the dangers of malware, and opens to [CISA's Secure Our World.](https://cisa.gov/secure-our-world/) It is named after the year the aforementioned music video was released.


*Disclaimer: This program and/or its authors are not affiliated with CISA in any way.*

## Build Instructions

### Windows

1. Make sure [Python](https://python.org/) is installed.

2. Download and extract the repository, and then open a terminal in it.

    **Optional but recommended:** Create and activate a clean virtual enviroment.

    ```
    python -m venv venv
    venv\scripts\activate.bat
    ```

    This is so when you build it, it does not bundle a bunch of uneeded libraries and bloat the exe.

3. Install pyinstaller.

    ```
    pip install pyinstaller
    ```

4. Build the script.

    ```
    build.bat
    ```
    **Note:** You may want to update the icon in the build script.

You now should have `main.exe` under `binaries`.


### Linux

1. Download and extract the repository, and then open a terminal in it.

    **Optional but recommended:** Create and activate a clean virtual enviroment.

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

    This is so when you build it, it does not bundle a bunch of uneeded libraries and bloat the file.

2. Install pyinstaller.

    ```
    pip3 install pyinstaller
    ```

3. Build the script.

    ```
    chmod +x build.sh
    ./build.sh
    ```

You now should have `main` under `binaries`.

