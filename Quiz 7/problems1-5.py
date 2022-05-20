import xlrd
from functools import reduce

#Quiz 7-1
wb = xlrd.open_workbook('student.xls')
ws = wb.sheet_by_index(0)
header =[]
id = []
name = []
scores = []

header = ws.row_values(0)[:3]
print(header)


for i in range (1,ws.nrows):
  
  id.append(ws.cell_value(i,0))
  name.append(ws.cell_value(i,1))
  temp =[]
  for t in range (2,6):
    temp.append(ws.cell_value(i,t))
  scores.append(temp)
    
print(id)
print(name)
print(scores)


#7-2
zipped = zip(id, name, scores)
list1 = []
for k in zipped:
  dict1 = dict(zip(header, k))
  list1.append(dict1)
print(list1)

#7-3
for value in filter(lambda x: sum(x['Scores']) > 280, list1):
  print(value)

#7-4
for n in range(ws.nrows-1):
  print(list1[n]['ID'], list1[n]['Name'], reduce(lambda a, b: a + b, list1[n]['Scores']))

#7-5
n = 0
for value in map(lambda x: 10000000 + x['ID'], list1):
  print(value, list1[n]['Name'], reduce(lambda a, b: a + b, list1[n]['Scores']))
  n += 1