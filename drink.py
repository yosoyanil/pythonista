import random

names = ['Shubham', 'Manan', 'Dishant', 'Dhruv', 'Harman']
ages = [random.randint(10, 35) for _ in range(5)]

can_drink = []

for age in list(ages):
    if int(age)>=21:
        can_drink.append(f'[names], grab a beer')

    else:
        can_drink.append(f'[names], dudh peeyo biscuit khao')

print(can_drink)
