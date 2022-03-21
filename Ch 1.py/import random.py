import random
n = random.randint(0, 100)
print (n)
u= random.randint(0, 100)
print (u)
m= random.randint(0, 100)
print (m)
if m==n==u:
print ("All Same", n,u,m)
elif m==n or n==u or m==u:
print ("Two are the same", m, n, u)
elif m!=n or n!=u or m!=u:
print ("None are the same", m, n, u)