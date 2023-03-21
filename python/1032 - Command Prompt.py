# baekjoon 1032

"""
https://www.acmicpc.net/problem/1032
"""
n = int(input())
wordlist = list(input())

for i in range(n - 1):
    compare = list(input())
    for j in range(len(wordlist)):
        if wordlist[j] != compare[j]:
            wordlist[j] = '?'
print(''.join(wordlist))