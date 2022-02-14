import random
n = random.randint(0, 100)
print (n)
u= random.randint(0, 100)
print (u)
m= random.randint(0, 100)
print (m)
if n<u and n<m:
  print ("The Smallest Number is ", n)
elif n==u and n<m:
  print ("The Smallest Numbers are ", n,u)
elif n==m and n<u:
  print ("The Smallest Numbers are ", n, m)
if u<n and u<m:
  print ("The Smallest Number is ", u)
elif u==n and u<m:
  print ("The Smallest Numbers are ", u, n)
elif u==m and u<n:
  print("The Smallest Numbers are ", u, m)
if m<n and m<u:
  print ("The Smallest Number is ", m)
elif m==n and m<u:
  print("The Smallest Numbers are", m, n)
elif m==u and m<n:
  print("The Smallest Numbers are ", m, u)