#7-11
import matplotlib.pyplot as plt
fig, ax=plt.subplots()

subjects=['Math', 'English', 'Physics', 'Computer']
x = [1, 2, 3, 4]

Bill=[100, 90, 80, 60]
Mary = [90, 80, 70, 100]

ax.bar(subjects, Bill, label='Bill')
ax.bar(subjects, Mary, bottom=Bill, label='Mary')

ax.set_title('Stacked Graph of Scores')
ax.legend()

plt.show()



#7-12
import matplotlib.pyplot as plt
import numpy as np

labels = ['Bill', 'Mary']
maths = [100,90]
englishs = [90,80]
physicss = [80,70]
computers = [60,100]

x = np.arange(2)
width = 0.15

fig, ax = plt.subplots()
Math = ax.bar(x-width*1.5, maths, width,label='Math')
English = ax.bar(x-width*.5,englishs, width,label='English')
Physics = ax.bar(x+width*.5, physicss, width,label='Physics')
Computer = ax.bar(x+width*1.5, computers, width,label='Computer')

ax.set_title("Grouped Graph for Scores")
ax.set_xticks(x);ax.set_xticklabels(labels)
ax.legend( )

ax.bar_label(Math)
ax.bar_label(English)
ax.bar_label(Physics)
ax.bar_label(Computer)