"""
https://www.acmicpc.net/problem/1026
"""


def tresure():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    S = 0
    A.sort()
    for i in range(N):
        S += A[i] * B.pop(B.index(max(B)))
    return S


if __name__ == "__main__":
    print(tresure())