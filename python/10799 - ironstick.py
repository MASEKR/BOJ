sticks = input()
stack = []
res = 0

for i in range(len(sticks)):
    if sticks[i] == '(':
        stack.append('(')
    else:
        if sticks[i-1] == '(':
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1

print(res)