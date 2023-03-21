import sys

s1 = list(sys.stdin.readline().rstrip())
s2 = []

n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'L' and s1:
        s2.append(s1.pop())
    elif cmd[0] == 'D' and s2:
        s1.append(s2.pop())
    elif cmd[0] == 'B' and s1:
        s1.pop()
    elif cmd[0] == 'P':
        s1.append(cmd[1])

print("".join(s1 + list(reversed(s2))))

# 시간 초과
# temp = list(input())
# cursor = len(temp)

# for _ in range(int(input())):
# 	cmd = list(input().split())
# 	if cmd[0] == "P":
# 		temp.insert(cursor, cmd[1])
# 		cursor += 1
# 	elif cmd[0] == "L":
# 		if cursor > 0:
# 			cursor -= 1
# 	elif cmd[0] == "D":
# 		if cursor < len(temp):
# 			cursor += 1
# 	else:
# 		if cursor > 0:
# 			temp.remove(temp[cursor-1])
# print("".join(temp))