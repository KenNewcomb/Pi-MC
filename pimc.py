import random
import sys
import math

# Get number of steps
steps = int(sys.argv[1])

# Generate a 1X1 Square with a circle within it
# d = l = 1

point_list = []

# Randomly populate the point list

for point in range(0, steps):
	x = random.random()
	y = random.random()
	point_list.append((x,y))

# Count how many points are within circle
incount = 0.0

for point in point_list:
	if point[0]**2 + point[1]**2 <= 1:
		incount += 1 

pi_approx = 4*(incount/len(point_list))
print("Pi approximation = " + str(pi_approx))
print("Deviation from real value = " + str(abs(pi_approx-math.pi)))
