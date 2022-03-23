import matplotlib.pyplot as plt
import numpy as np

label = ['Bill', 'Jim', 'Joe']
width=0.15
x=np.arange(3)
math = [100, 100, 100]
english = [90, 90, 80]
physics = [90, 80, 90]
computer = [90, 80, 90]


fig, ax = plt.subplots()
p = ax.bar(x-width*1.5, math, width, label = 'Math')
r = ax.bar(x-width*0.5, english, width, label = 'English')
q = ax.bar(x+width*0.5, physics, width, label = 'Physics')
s = ax.bar(x+width*1.5, computer, width, label = 'Computer')

ax.legend(loc = 'lower center')
ax.set_title('Graph of scores')
ax.set_xticks(x)
ax.set_xticklabels(label)
ax.bar_label(p, padding=1)
ax.bar_label(r, padding=4)
ax.bar_label(q, padding=4)
ax.bar_label(s, padding=4)
plt.show()