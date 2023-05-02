import math

vx, vy, y0, h = input().split(" ")
vx = float(vx)
vy = float(vy)
y0 = float(y0)
h = float(h)

delta = vy * vy + 20*(y0-h)

if(delta < 0):
	print("impossible")
	exit()

t1 = (-1*vy-math.sqrt(delta))/-10
t2 = (-1*vy+math.sqrt(delta))/-10

Range1 = min(vx*t1, vx*t2)
Range2 = max(vx*t1, vx*t2)

if (Range1 >= 0 and Range1 != Range2):
	print('%.2f'%Range1, sep = " ")

if Range2 >= 0:
	print('%.2f'%Range2)
else: print("impossible")
