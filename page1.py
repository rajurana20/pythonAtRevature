# Make a Python program that prints your name.
print("Raju Rana")

#Make a program that displays the lyrics of a song.
lyrics ="Tale as old as time \
True as it can be \
Barely even friends \
Then somebody bends \
Unexpectedly \
Just a little change \
Small, to say the least \
Both a little scared \
Neither one prepared \
Beauty and the Beast \
Ever just the same \
Ever a surprise \
Ever as before \
And ever just as sure \
As the sun will rise, oh woah \
Ever just the same \
And ever a surprise, yeah \
Ever as before \
And ever just as sure \
As the sun will rise \
Oh, oh, oh"

print(lyrics)

# Make a program that displays several numbers.

numbers = {4,5.5,20,4.8}
print(numbers)

#Make a program that solves and shows the summation of 64 + 32.
x = 64 + 32
print(x)

#Do the same as in 2, but make it sum x + y.
x = 3
y = 4
z = x + y
print(z)

actor ="Allu Arjun"
print(actor)

s = "My lucky number is %d, what is yours?" % 7
print(s[3:8])

s = "The date is %d/%d/%d" % (7, 7, 2016)
print(s)

import random
x = random.randrange(0,10)
print(x)

import random as r
print(r.randrange(0,10))
print(r.randrange(0,10))
print(r.randrange(0,10))

s = "Hello world!"
s2=s.replace("world", "Conor")
print(s2.replace("Hello", ""))

str = "this is string example....wow!!! this is really string"
print(str.replace("is", "was", 3))


words = ["Messi", "is", "the", "best", "soccer", "player"]
sentence = " ".join(words)
print(sentence) 
print(sentence.replace(" ","_"))

s = "Its to easy"
words = s.split()
print(words)

s= "World,Earth,America,Canada";
words = s.split(",")
print(words)

s= "He really needs to get his priorities in order.";
words = s.split("to get his priorities in order")
print(words)

s = "That I ever did see. Dusty as the handle on the door. Dusty Dusty"

index = s.find("Dusty")
print(index)

s = "That I ever did see. Dusty as the handle on the door. Dusty Dusty"

if "Dusty" in s:
  print("query found")
