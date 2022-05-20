def getinput(T, Q):
  id_list = []
  name_list = []
  scores_list = []
  for i in range(T):
    id_list.append(input("Enter ID: "))
    name_list.append(input("Enter name: "))
    scores = []
    for j in range(Q):
      scores.append(int(input("Enter score: ")))
    scores_list.append(scores)
  return id_list, name_list, scores_list
  
def findHighest(total_list, id_list, name_list):
  high = max(total_list)
  idx = total_list.index(high)
  print("Highest Total Score:", high, 'from', id_list[idx], name_list[idx])

def findLowest(id_list, name_list, scores_list):
  for i in range(Q):
    low_list = []
    for j in range(T):
      low_list.append(scores_list[j][i])
    lowscore = min(low_list)
    count = low_list.count(lowscore)
    print("S{} lowest score:".format(i+1), lowscore)
    idx = low_list.index(lowscore)
    if count == 1:
      print('from:', id_list[idx], name_list[idx])
    else:
      print('from:')
      for k in range(count):
        idx = low_list.index(lowscore)
        print(id_list[idx], name_list[idx])
        low_list.insert(idx, lowscore + 10) 
        low_list.remove(lowscore)

def printAll(id_list, name_list, scores_list):
  total_list = []
  for i in range(T):
    total = sum(scores_list[i])
    avg = total / Q    
    print(id_list[i], name_list[i], scores_list[i], "Total:", total, "Avg:", avg)
    total_list.append(total)
  return total_list


T= int(input("Enter number of students: "))
Q = int(input("Enter number of scores for each student: "))
id_list, name_list, scores_list = getinput(T, Q)
total_list = printAll(id_list, name_list, scores_list)
findHighest(total_list, id_list, name_list)
findLowest(id_list, name_list, scores_list)