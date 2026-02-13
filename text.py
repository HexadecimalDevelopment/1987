# text.py

import cbc, sys, os

try:

    cbc.out('You could have been hacked...', terminator='')
    print(' Press enter to continue:', end='')
    input()
    cbc.out('This was just a harmless script designed as an educational tool, but next time might not be...', terminator='')
    input()
    cbc.out('Online security is IMPORTANT.', terminator='')
    input()
    cbc.out('In 2021, a business or individual fell victim to a ransomware attack roughly every 11 seconds.', terminator='')
    input()
    cbc.out('In 2023, there were over 6 billion malware attacks globally.', terminator='')
    input()
    cbc.out('These numbers are rising rapidly.', terminator='')
    input()
    cbc.out('Over 90% of these attacks started with a user downloading what seemed like an innocent file... Like this one.....', terminator='')
    input()
    cbc.out('https://www.cisa.gov/secure-our-world/')
    input('Press enter to exit.')

    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')

    cbc.out('1987\n\nhttps://github.com/HexadecimalDevelopment/1987/\n\nCopyright (C) 2026 Hunt Burke (Hexadecimal Development)\n\nLicensed under the AGPL 3.0 (https://raw.githubusercontent.com/HexadecimalDevelopment/1987/refs/heads/main/LICENSE)\n\nThis program and/or its authors are NOT affilliated with CISA in any way.', 0.005)

    sys.exit()

except KeyboardInterrupt: sys.exit()