h = int(input('Enter x Value '))
u = int(input('Enter y Value '))
if h>0 and u>0:
  print ("Quadrant 1")
elif h>0 and u<0:
  print ("Quadrant 4")
elif h<0 and u<0:
  print ("Quadrant 3")
elif h<0 and u>0:
  print ("Quadrant 2")
elif h==0 or u==0:
  print ("N/A")





import random
n = random.randint(0, 100)
print (n)
u= random.randint(0, 100)
print (u)
m= random.randint(0, 100)
print (m)
if m==n==u:
  print ("All Same", n,u,m)

# in the case of two same values, you should figure out which two values are same.
# For example, m and n are same or so on.
elif m==n or n==u or m==u:
  print ("Two are the same", m, n, u)
elif m!=n or n!=u or m!=u:
  print ("None are the same", m, n, u)




import random
n = random.randint(0, 100)
print (n)
u= random.randint(0, 100)
print (u)
m= random.randint(0, 100)
print (m)
if n<u and n<m:
  print ("The Smallest Number is ", n)

# when we find the smallest number, I think we do not need to consider the same values
# just two more cases like your line 45
# if u<n and u<m:

# if m<u and m<n:

  if n==u and n<m:
    print ("The Smallest Numbers are ", n,u)
  if n==m and n<u:
    print ("The Smallest Numbers are ", n, m)
if u<n and u<m:
  print ("The Smallest Number is ", u)
  if u==m and u<n:
    print("The Smallest Numbers are ", u, m)
if m<n and m<u:
  print ("The Smallest Number is ", m)

#=