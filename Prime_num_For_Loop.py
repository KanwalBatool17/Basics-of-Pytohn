print("\n____________________* Even and Odd Number with While Loop *___________________\n")
print("Prime numbers between", 1, "and","100 :\n")

for num in range(1,100 + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)