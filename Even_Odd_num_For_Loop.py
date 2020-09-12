print("\n____________________* Even and Odd Number with For Loop *___________________\n")

e_n = 1
for number in range(e_n,100 + 1):
    if number % 2 ==0:
        print(number, "is even number")
    elif number % 2 != 0:
        print(number, "is odd number")