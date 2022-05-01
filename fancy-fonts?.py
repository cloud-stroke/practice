from rich import print
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.50)

print("Hello!",)