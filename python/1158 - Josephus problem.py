from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N+1))
res = []

for _ in range(N):
    for i in range(K-1):
        queue.append(queue.popleft())
    res.append(queue.popleft())
print('<', end='')
print(*res, sep=', ', end='')
print('>')
