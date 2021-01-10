import random

num1= random.randrange(100)
num2= random.randrange(100)

sum= num1+num2
answer = input(f"{num1}+{num2}=")

if int(answer)==sum:
    print("correct answer")

else:
    print('wrong!')
