import random

questions= []

for num in range(100):
    num1= random.randint(100,1000)
    num2= random.randint(100,1000)
    questions.append(f'{num1}*{num2}')

print(questions)
