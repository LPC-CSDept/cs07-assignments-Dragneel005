import random
U=10
rand=[]
for i in range (U):
  rand.insert(i, random.randint(0,10))

print('The original list is')
print (rand)

print('The list with the first and minimum value swapped')
minval=min(rand)
y=rand[0]
a=rand.index(y)
t=rand.index(minval)
rand[a], rand[t]=rand[t], rand[a]
print(rand)

print('List with second and second minimum value switched')
rand.pop(0)
q=min(rand)
w=rand[0]
e=rand.index(w)
r=rand.index(q)
rand[e], rand[r]=rand[r], rand[e]
asd=rand.insert(0, minval)
print(rand)