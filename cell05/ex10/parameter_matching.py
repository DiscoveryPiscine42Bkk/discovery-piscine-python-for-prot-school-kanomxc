import sys

array = sys.argv
dele = array.pop(0)

if len(array) <= 0:
    print("none")
    exit()

prompt = input("What was the parameter? ")
Ans = []
Ans.append(prompt)

if len(array) > 0 and Ans == array:
    print("Good job!")
else:
    print("Nope, sorry...")
