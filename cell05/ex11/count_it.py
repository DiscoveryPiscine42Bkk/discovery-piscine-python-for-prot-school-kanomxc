import sys

array = sys.argv
dele = array.pop(0)

if len(array) <= 0:
    print("none")
    exit()

print(f"parameters: {len(array)}")
for i in array:
    print(f"{i}: {len(i)}")