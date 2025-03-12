A = int(input("Give me the first number: "))
B = int(input("Give me the second number: "))

print("Thank you!")

C = ["+","-","/","*"]

for i in range(1,5):
  print(f"{A} {C[i-1]} {B} = {eval(f'{A} {C[i-1]} {B}')}")