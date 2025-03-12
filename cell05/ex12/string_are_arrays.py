import sys

array = sys.argv
dele = array.pop(0)
j = 0

if len(array) <= 0:
    print("none")
    exit()

str_array = []
for i in array:
    str_array += i

for i in str_array:
    if i == "z":
        j += 1

for i in range(j):
    print("z", end="")