#9
import random
pre=random.randint(0,100)
while True:
  cn=random.randint(0,100)
  print("The prevous number is {0} and the current number is {1}" .format (pre, cn))
  if (pre <= cn):
    print ('The current number {0} is greater than the prevous number {1}' .format(cn, pre))
    break
  pre = cn


#11
for i in range(1):
    for a in range(1):
        print(i , a , end=' | ')
    print( )
for i in range(1, 2):
    for a in range(2):
        print(i , a , end=' | ')
    print( )
for i in range(2 , 3):
    for a in range(0 , 3):
        print(i , a , end=' | ')
    print( )