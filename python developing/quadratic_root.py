# Python program to find roots of a quadratic equation
#i = √-1
import math

def findRoots(a, b, c):

	# If a is 0, then equation is
	# not quadratic, but linear
	if a == 0:
		print("Invalid")
		return -1
	d = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(d))

	if d > 0:
		print("Roots are real and different ")
		print((-b + sqrt_val)/(2 * a))
		print((-b - sqrt_val)/(2 * a))
	elif d == 0:
		print("Roots are real and same")
		print(-b / (2*a))
	else:  # d<0
		print("Roots are complex")
		print(- b / (2*a), " + i", sqrt_val / (2 * a))
		print(- b / (2*a), " - i", sqrt_val / (2 * a))



if  __name__ == '__main__':
	a = float(input('Please input digits for "a": '))
	b = float(input('Please input digits for "b": '))
	c = float(input('Please input digits for "c": '))
	# Function call
	findRoots(a, b, c)

