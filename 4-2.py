import random
while True:
  num=random.randint(0,100)
  if (num%2==0):
    print("{0} is an even number".format(num))
    break;
  if (num%2 != 0):
    print("{0} is an odd number".format(num))





import random
i=0
while (i>=0 and i<=100):
  num=random.randint(0,100)
  i += num
  print(i)
  if (i>100):
    print("The summation {0} is greater than 100".format(i))