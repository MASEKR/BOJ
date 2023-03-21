n = int(input())

for i in range(n):
    num, s = input().split()
    res = ""
    for i in s:
        res += int(num)*i
    print(res)
