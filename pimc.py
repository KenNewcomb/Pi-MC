import random
import sys
import math

# Get tolerance from first command line parameter
tol = float(sys.argv[1])

# Initialize various variables
pi_approx = 0
in_count = 0
step = 0

print("Approximating pi..."),
sys.stdout.flush()

# While pi is not within given tolerance
while(abs(pi_approx - math.pi) >= tol):

	step += 1
	# Generate random values for x,y coordinates
	x = random.random()
	y = random.random()
	
	# if (x,y) is within a circle of radius 1
	if x**2 + y**2 <= 1:
		in_count += 1
	
	# Ratio of square to circle area = pi/4
	pi_approx = 4*(float(in_count) / step)

print("done.")
print("Approximate value of pi: " + str(pi_approx))
print("Number of iterations: " + str(step))
