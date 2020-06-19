" This code suppresses the output of any line desired"

from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

print ("You can see this")
with suppress_stdout():
    os.system('git clone https://github.com/SarthakNarayan/VScode-Settings.git')
    print ("You cannot see this")
print ("And you can see this again")