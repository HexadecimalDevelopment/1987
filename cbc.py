# cbc.py

import time

def out(input: str, delay: float=0.1, terminator: str='\n'):
    input = list(input)
    for c in input:
        print(c, end='', flush=True)
        time.sleep(delay)
    print(terminator, end='', flush=True)