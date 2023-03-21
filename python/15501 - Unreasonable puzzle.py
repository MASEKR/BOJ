"""
https://www.acmicpc.net/problem/15501
"""


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 밀기
idx = b.index(a[0])
compare_1 = b[idx:] + b[:idx]
# 뒤집기
b = b[::-1]
idx = b.index(a[0])
compare_2 = b[idx:] + b[:idx]

if a == compare_1 or a == compare_2:
    print("good puzzle")
else:
    print("bad puzzle")