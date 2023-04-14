import sys
from math import gcd

def lcm(x, y):
    return x*y // gcd(x, y)

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))



# import sys

# n = int(sys.stdin.readline())

# for _ in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     for i in range(max(a,b), (a*b)+1):
#         if i % a == 0 and i % b == 0:
#             print(i)
