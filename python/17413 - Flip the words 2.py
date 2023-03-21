import sys

S = list(sys.stdin.readline().rstrip())

flag = False
res = ""
stack = ""

for i in S:
    if flag == False:
        if i == "<":
            flag = True
            stack += i
        elif i == " ":
            stack += i
            res += stack
            stack = ""
        else:
            stack = i + stack
    elif flag == True:
        stack += i
        if i == ">":
            flag = False
            res += stack
            stack = ""
print(res+stack)
