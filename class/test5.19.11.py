import math

k = int(input())

e = sum(1 / math.factorial(i) for i in range(k+1))

print("{:.10f}".format(e))
