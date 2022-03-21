#7-6
value=[]
for i in range(int(input('Enter length of first list'))):
  print("Enter value")
  user_input=int(input())
  value.append(user_input)
num2=[]
for t in range(int(input('Enter length of second list'))):
  print("Enter value")
  userinput=int(input())
  num2.append(userinput)
flag = 0
if(set(value).issubset(set(num2))):
    flag = 1
if (flag):
    print("True")
else:
    print("False")



#7-7
print('Enter first list length')
N = int(input())
print('Enter list values')
num1 = [0] * N
for i in range(N):
	num1[i] = int(input())
print (num1)
print('Enter second list length')
M = int(input())
print('Enter list values')
num2 = [0] * M
for i in range(M):
	num2[i] = int(input())
print (num2)
print (num1+num2)


#7-8
N=int(input())
num1= [0]*N
for i in range (N):
  num1[i]= int(input())
print(num1)
M=int(input())
num2 = [0]*M
for i in range (M):
  num2[i]= int(input())
print(num2)
minlen= N if N<M else M
num3=[0]*(minlen*2)
for i in range(minlen):
  num3[2*i]=num1[i]
  num3[2*i+1] = num2[i]
if minlen==N:
  num3 += num2[minlen:]
else:
  num3 += num1[minlen:]
print(num3)




#7-9
keyword = input('Enter keyword')
N = int(input("Enter list value amount"))
input_list = []
for i in range(N):
  input_list.append(input("Enter input"))
  if keyword in input_list:
    print("True")
  else:
    print("False")