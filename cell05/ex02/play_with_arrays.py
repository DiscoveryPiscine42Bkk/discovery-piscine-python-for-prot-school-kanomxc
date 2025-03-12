array = [2,8,9,48,8,22,-12,2]
new_array = []

for i in array:
    if i > 5:
        i += 2
        new_array.append(i)

print(array)
print(new_array)