import random
pre=random.randint(0,100)
while True:
  cn=random.randint(0,100)
  print("The prevous number is {0} and the current number is {1}" .format (pre, cn))
  if (pre <= cn):
    print ('The current number {0} is greater than the prevous number {1}' .format(cn, pre))
    break




import random
i=0
num=0
while (i<10):
  nums=random.randint(0,100)
  print(nums)
  num+=nums
  if (num>100):
    print("The total is {0}".format(num))
    break
  i += 1
else:
    print("The total {0} is <= 100".format(num))


for i in range(0,3):
	for j in range(i,3):
		print (j, i)