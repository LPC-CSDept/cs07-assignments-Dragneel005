i = 1
while ( i<11):
	print (i, end=',')
	i += 1



i=input('Enter a value= ')
print ("You have entered {0}".format(i))
while (i!= 'q'):
  i=input('Enter a value= ')
  print ("You have entered {0}".format(i))
print("You have entered q the loop is now over")





import random
pre=random.randint(0,100)
flag=1
while (flag):
  cn=random.randint(0,100)
  print("The prevous number is {0} and the current number is {1}" .format (pre, cn))
  if (pre <= cn):
    print ('The current number {0} is greater than the prevous number {1}' .format(cn, pre))
    flag=0





i=int(input('Enter number '))
while (i<0 or i>100):
  print("Your number is invalid")
  i=int(input('Enter another number '))
  break
if (i>0 or i<101):
  print("Your number is valid")
  