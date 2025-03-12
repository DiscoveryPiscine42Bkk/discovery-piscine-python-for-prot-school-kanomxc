import re
import sys

array = sys.argv
dele = array.pop(0)

if len(array) > 1:
    print(len(re.findall(sys.argv[0],sys.argv[1])))
else:
    print("none")