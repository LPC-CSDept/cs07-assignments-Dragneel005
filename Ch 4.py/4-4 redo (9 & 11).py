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


  