import random
e = False
f = random.randint(0, 100)
while True:
  print(f)
  if f % 2 == 0:
    e = True
  s = random.randint(0, 100)
  print(s)
  if s % 2 == 0 and e:
    print("Two even numbers {0} and {1} were generated" .format(f, s))
    break
  e = False
  f = s





i = input('Enter String Value=')
q = 0
while (i!="stop"):
	i= input('Enter String Value=')
	if("p" in i):
		# q = str(i.count('p'))
		q += 1
print(q)