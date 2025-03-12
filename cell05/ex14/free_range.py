import sys

array = sys.argv
dele = array.pop(0)

if len(array) <= 0:
    print("none")
    exit()

new_array = list(map(int,array))
ans_array = []

for i in range(new_array[0], new_array[1]+1):
    ans_array.append(i)

print(ans_array)