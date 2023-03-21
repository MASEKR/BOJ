import sys

L = int(sys.stdin.readline())
ad = sys.stdin.readline().rstrip()

# KMP 알고리즘
pi = [0] * L
j = 0
for i in range(1, L):
    while j > 0 and ad[i] != ad[j]:
        j = pi[j - 1]
    if ad[i] == ad[j]:
        j += 1
        pi[i] = j

print(L - pi[L - 1])

# 시간초과
# import sys
#
# L = int(sys.stdin.readline())
# s = sys.stdin.readline().rstrip()
#
# for length in range(1, len(s)+1):
#     possible = True
#     for i in range(length, len(s)):
#         if s[i] != s[i % length]:
#             possible = False
#             break
#     if possible:
#         print(length)
#         break
# else:
#     print(1)
