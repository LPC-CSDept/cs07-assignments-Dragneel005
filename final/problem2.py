import random as rand

lst=[]
dict1={}

for i in range(10):
  inpu = rand.randint(0,4)
  lst.append(inpu)
  
print("List of random numbers")
print(lst)

from collections import Counter

dict1=dict(Counter(lst))
print('The dictionary')
print(dict1)

count= max(dict1, key=lambda t: dict1[t])
counts = dict1[count]

print("Digit:", count, '(', counts, 'number ocurred )')