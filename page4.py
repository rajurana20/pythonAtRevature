# Nested loops finish in O(n^2)

T = [['O', 'O', 'X'], ['O', 'X','O'], ['X', 'O', 'O']]
for r in T:
    for c in r:
        print(c,end = " ")
    print()

persons = ["John", "Marissa", "Pete", "Dayton"]

for x in persons:
  for y in persons:
    if x != y:
        print(x, " meet ", y)

# Slices
pizzas = ['Hawai','Pepperoni','Fromaggi','Napolitana','Diavoli']

pizzaSlice = slice(3)

print(pizzas[pizzaSlice])

py_string = 'Python'

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3) 
print(py_string[slice_object])  

text = "Hello World"
slice_object = slice(6,11) 
print(text[slice_object])

# This function returns a list --------------------

def func(): 
    a = 5
    b = 20   
    c = 6
    d = 9
    return [a, b, a+b, c, d];   
  
# Driver code to test above method 
list = func()  
print(list)

# Scope -------------------------------------------

def withdraw(bal, amt):
    newBal = bal - amt

    return newBal

print( withdraw(100, 30) )

# print the date

import datetime

now = datetime.datetime.now()
print ("Today is ", now.strftime("%Y-%m-%d"))

# Try Except questions

# You CAN use the try-except block to do keyboard input validation.
# You CAN use the try-except block for file validation
# The except block should only catch exceptions you are prepared to handle. If you handle an unexpected error, your code may do the wrong thing and hide bugs
