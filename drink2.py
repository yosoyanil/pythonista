names = ['Shubham', 'Manan', 'Dishant', 'Dhruv', 'Harman']
ages = [random.randint(10, 35) for _ in range(5)]

new = []
for n in alist:
    if n == 5:
        continue
    else:
        new.append(n+1)

print(new)
