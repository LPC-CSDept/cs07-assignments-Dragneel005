#Assignment 7-1
print("Enter user value")
value=[]
while True:
  user_input=int(input())
  value.append(user_input)
  print(value)
  if (user_input<0):
    minval=min(value)
    maxval=max(value)
    value.remove(minval)
    value.remove(maxval)
    min=min(value)
    value.remove(min)
    sum=sum(value)
    print("The summation is",sum)
    print("The average is ",sum / len(value))



#Assignmnet 7-2
value=[]
for i in range(int(input('Enter length of list'))):
  print("Enter value")
  user_input=int(input())
  value.append(user_input)
  print(value)
sum=sum(value)
for num in value:
  print(abs(num-(sum / len(value))))





#Assignment 7-3
value=[]
for i in range(int(input('Enter length of list'))):
  print("Enter value")
  user_input=int(input())
  value.append(user_input)
  print(value)
num2=[]
for t in range(int(input('Enter length of list'))):
  print("Enter value")
  userinput=int(input())
  num2.append(userinput)
  print(num2)
flag = 0
if(set(num2).issubset(set(value))):
    flag = 1
if (flag):
    print("True")
else:
    print("False")

#Assignmnet 7-4
value=[]
for i in range(5):
  print("Enter value")
  user_input=int(input())
  value.append(user_input)
ins=value.insert(i,int(input('Enter value you want to insert')))
val = sorted(value)
print(val)

#Assignmnet 7~5
import random
U=20
rando=[]
for i in range (U):
  rando.insert(i, random.randint(0,10))
print(rando)
delete=int(input('Enter value you want to remove'))
rando.remove(delete)
print(rando)