clist = ['Canada','USA','Mexico','Australia'] 
for c in clist: 
 print(c) 


for x in range(1,101):
  print(x)

number=6


for x in range(10,0,-1):
  print(x)

for x in range(1,11):
  if x%2==0:
    print(x)

mysum=0
for x in range(100,201):
  mysum+=x
print("sum is: %d "%mysum)

number2=1;
while number2<=10:
  for x in range(1,11):
    print("%d * %d = %d" %(number2,x,x*number2))
  number2+=1

def sum(list): 
 sum = 0 
 for e in list: 
  sum = sum + e 
 return sum 
mylist = [1,2,3,4,5] 
print(sum(mylist))


def multiplicationTable(number2):
  for x in range(1,11):
    print("%d * %d = %d" %(number2,x,x*number2))

def tables(list):
  for x in list:
    multiplicationTable(x)

numberList=[20,32,47]
tables(numberList)

def sumRecursive(n):
  if n==0:
    return 0
  else:
    return n+sumRecursive(n-1)
print(sumRecursive(10))
