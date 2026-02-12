import cbc, sys

try:

    cbc.out('You could have been hacked...', terminator='')
    print(' Press enter to continue:', end='')
    input()
    cbc.out('This was just a harmless script designed as a prank, but next time might not be...', terminator='')
    input()
    cbc.out('Online security is IMPORTANT.', terminator='')
    input()
    cbc.out('In 2023, there were over 6 billion malware attacks globally.', terminator='')
    input()
    cbc.out('In 2021, a business or individual fell victim to a ransomware attack roughly every 11 seconds.', terminator='')
    input()
    cbc.out('https://www.cisa.gov/secure-our-world')
    input('Press enter to exit.')
    sys.exit()

except KeyboardInterrupt: sys.exit()