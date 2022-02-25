i = input('Enter String Value=')
while (i!="stop"):
  i= input('Enter String Value=')
if ("p" in i):
    q = str(i.count('p'))
    print(q)


import random
i=0
while True:
  num = random.randint(0,100)
  hum = random.randint(0,100)
  print(num, hum)
  if (num%2==0 and hum%2==0):
    print (hum, num)
    break
