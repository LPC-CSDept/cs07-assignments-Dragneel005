import random
r = int(input("Enter row amount: "))
c = int(input("Enter column amount: "))
list1 = []
for i in range(r):
  row = []
  for j in range(c):
    row.append(random.randint(0, 100))
  list1.append(row)
for i in range(r):
  for j in range(c):
    print(list1[i][j], end = " ")
  print()
mr = 0
mc = 0
for i in range(r):
  sum1 = sum(list1[i])
  if sum1 > mr:
    ms = sum1
for i in range(c):
  sum2 = 0
  for j in range(r):
    sum2 += list1[j][i]
  if sum2 > mc:
    mc = sum2
print("{0} has the greate4s sum of all the rows and {1} has the greates sum of all the columns".format(ms,mc))