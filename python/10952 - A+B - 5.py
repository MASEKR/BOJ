"""
https://www.acmicpc.net/problem/10952
"""


while True:
    a, b = input().split()
    if a == "0" and b == "0":
        break
    else:
        print(int(a) + int(b))