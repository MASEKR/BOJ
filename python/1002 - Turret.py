"""
https://www.acmicpc.net/problem/1002
"""


import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0)

"""
원의 방정식을 이용해서 풀었고
조규현(x1, y1)과 백승환(x2, y2)의 좌표를 기점으로 두개의 원을 그렸고 그 사이의 거리를 distance로 잡았다.
그 이후 케이스를 나누어서 풀었다.
1. 두원이 동심원이고 반지름(distance)의 길이가 같을때
2. 내접, 외접일 때
3. 두 원이 두 점에서 만날때
"""