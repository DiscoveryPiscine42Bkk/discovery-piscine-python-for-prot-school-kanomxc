import sys


array = sys.argv
dele = array.pop(0)
rev = array[::-1]

for i in rev:
    if len(rev) > 1:
        print(i)
    else:
        print("none")