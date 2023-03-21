import sys

n = int(sys.stdin.readline())
chk = 1
stack = []
pm = []

for _ in range(n):
	m = int(sys.stdin.readline())
	for j in range(chk, m+1):
		stack.append(j)
		pm.append("+")
		chk += 1
	if stack[-1] == m:
		stack.pop()
		pm.append("-")
if len(stack) != 0:
	print("NO")
else:
	for i in pm:
		print(i)
