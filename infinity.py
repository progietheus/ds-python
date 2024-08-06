# Infinity is useful when you want to initialize a variable that is greater or smaller than any value that your algorithm may want to compare with. There are 2 ways to represent infinity as an integer in Python. The first one is to use float values:

positive_inf = float('inf')
negative_inf = float('-inf')

print(positive_inf)
print(negative_inf)

# Since Python 3.5, we can also use the math module to represent infinite integers:
import math

positive_inf = math.inf
negative_inf = -math.inf

print("using import math: " + str(positive_inf))
print("using import math: " + str(negative_inf))