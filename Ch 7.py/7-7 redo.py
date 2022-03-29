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

if (num1 >num2):
  print (num1+num2)
else:
  print(num2+num1)