h = int(input('Enter x Value '))
u = int(input('Enter y Value '))
if h>0 and u>0:
print ("Quadrant 1")
elif h>0 and u<0:
print ("Quadrant 4")
elif h<0 and u<0:
print ("Quadrant 3")
elif h<0 and u>0:
print ("Quadrant 2")
elif h==0:
print ("N/A")
elif u==0:
print ("N/A")