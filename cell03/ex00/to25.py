A = int(input("Enter a number less than 25\n"))

if A < 25:
  for i in range(A,26):
    print(f"Inside the loop, my variable is {i}")
else :
  print("Error")