import sys

n = int(sys.stdin.readline())

for i in range(n):
    a = sys.stdin.readline().split()
    for j in a:
        print(j[::-1] + " ", end="")
    print()
    