# Lists -------------------------------------------

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana','Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana','Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
  
# initializing check letter 
check = 'M'
  
# printing original list 
print("The states : " + str(states)) 
  
# Words starting with specific letter 
res = [idx for idx in states if idx[0].lower() == check.lower()] 
  
# print result 
print("The list of matching first letter : " + str(res)) 
# List Operations ----------------------------------

y = [6,4,2] 

y.append(12)
y.append(8)
y.append(4)

y[1] = 3

print("The updated list of values: ", y)

# sorting list -------------------------------------

x = [(3,6), (4,7), (5,9), (8,4), (3,1)]

x.sort()
print(x)

# take second element for sort
def takeSecond(elem):
    return elem[1]

x.sort(key=takeSecond)
print(x)

# range function ----------------------------------
import random
nums = [0]

for x in range(1001):
  val = random.randint(1, 1000)
  nums.append(x)

print(nums)

nums.sort()

print("The smallest number: ", nums[0])
print("The largest number: ", nums[1000])

even = [0]

for x in range(2,100, 2):
  even.append(x)

odd = [1]

for x in range(3,100, 2):
  odd.append(x)

print("The Even List:")
print(even)

print("The Odd List:")
print(odd)

# Dictionary, state codes are just for testing, not actual codes

mapper = {
  "Alabama": "Al", 
  "Alaska":"Ak", 
  'Arizona':'Az', 
  'Arkansas':'Ar', 
  'California':'Ca', 
  'Colorado':'Co', 
  'Connecticut':'Cn', 
  'Delaware':'Dw', 
  'Florida':'Fl', 
  'Georgia':'Ga', 
  'Hawaii':'Hw', 
  'Idaho':'Id', 
  'Illinois':'Il', 
  'Indiana':'Id', 
  'Iowa':'Io', 
  'Kansas':'Ks', 
  'Kentucky':'Kt', 
  'Louisiana':'La',
  'Maine':'Ma', 
  'Maryland':'Mr', 
  'Massachusetts':'Ms', 
  'Michigan':'Mi', 
  'Minnesota':'Mn', 
  'Mississippi':'Mp', 
  'Missouri':'Mo', 
  'Montana':'Mo',
  'Nebraska':'Nb', 
  'Nevada':'Nv', 
  'New Hampshire':'Nh', 
  'New Jersey':'Nj', 
  'New Mexico':'Nm', 
  'New York':'Ny', 
  'North Carolina':'Nc', 
  'North Dakota':'Nd', 
  'Ohio':'Oh', 
  'Oklahoma':'Ok', 
  'Oregon':'Or', 
  'Pennsylvania':'Pn',
'Rhode Island':'Ri', 
'South Carolina':'Sc', 
'South Dakota':'Sd', 
'Tennessee':'Tn', 
'Texas':'Tx', 
'Utah':'Ut', 
'Vermont':'Vt', 
'Virginia':'Vi', 
'Washington':'Wa', 
'West Virginia':'Wv', 
'Wisconsin':'Wi', 
'Wyoming':'Wy'}

print(mapper)

# Read File. If the file doesn't exist there is a FileNotFoundError message

print("Lyrics from https://www.youtube.com/watch?v=n4RjJKxsamQ")
f = open("song.txt", "r")
count = 1
for x in f:
  print(count,". ",x)
  count +=1

  # Write File

file = open("outfile.txt", "w")
file.write("Take it Easy!")
file.close()

file = open("outfile.txt", "a")
file.write('open(“text.txt”)')
file.close()
