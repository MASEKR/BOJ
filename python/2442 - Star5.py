"""
https://www.acmicpc.net/problem/2442
"""


n = int(input())
for i in range(1, n+1):
    a = " "*(n-i) + "*"*((2*i) - 1)
    print(a)