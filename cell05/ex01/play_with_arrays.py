array = [2,8,9,48,8,22,-12,2]
new_array = []

for i in array:
    i += 2
    new_array.append(i)
    
print(f"Original array: {array}")
print(f"New array: {new_array}")