"""
https://www.acmicpc.net/problem/1934
"""

"""
function Minimum common multiple
ex input
3
1 45000
6 10
13 17

ex output
45000
30
221
"""
import sys


def minimum_common_multiple():
    T = int(input())

    for _ in range(T):
        a, b = map(int, sys.stdin.readline().strip().split())
        A, B = a, b
        while a % b != 0:
            a, b = b, a % b

        print(A * B // b)


if __name__ == '__main__':
    minimum_common_multiple()
