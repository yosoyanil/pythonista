# something(something_inside) --> Function

name = 'Anil'
age = 574

string = f'My name is {name}. My age is {age} & I know how to do 29 + 40 = {29+40}'

# End parameter

print('name', end='\n\n') # by default it's \n
print('age', end='_')

logged_in = True
admin = True

if logged_in or admin:
    print('ACCESS GRANTED')

else:
    print('ACCESS DENIED')  # \= escape character
