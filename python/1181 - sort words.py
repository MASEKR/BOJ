# https://www.acmicpc.net/problem/1181


import sys
input = sys.stdin.readline

words = list(set([input().rstrip() for _ in range(int(input().rstrip()))]))
words.sort()
words.sort(key=len)
for i in words:
    print(i)