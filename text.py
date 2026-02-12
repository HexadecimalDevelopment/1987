import cbc, sys

try:

    cbc.out('You have been hacked...', terminator='')
    print(' Press enter to continue:', end='')
    input()
    cbc.out('You got lucky... This time.....', terminator='')
    input()
    cbc.out('This was just a harmless script, but next time might not be...', terminator='')
    input()
    cbc.out("So secure your system... Before it's too late.....", terminator='')
    input()
    cbc.out('Goodbye... For now.....')
    input()
    sys.exit()

except KeyboardInterrupt: sys.exit()