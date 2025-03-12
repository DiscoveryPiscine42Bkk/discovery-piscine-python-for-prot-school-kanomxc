import sys

array = sys.argv
dele = array.pop(0)

if len(array) <= 0:
    print("none")
    exit()

print(array)
strings = ''

for i in array:
    if not "ism" in i:
        strings = i+"ism"
        print(strings)