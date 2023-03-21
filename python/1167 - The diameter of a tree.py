from sys import stdin
from collections import deque

readline = stdin.readline
V = int(readline())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, readline().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))

def bfs(start):
    visit = [False] * (V + 1)
    que = deque()
    que.append(start)
    visit[start] = True
    max = [0,0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visit[e] == False:
                visit[e] = visit[t] + w
                que.append(e)
                if visit[e] > max[0]:
                    max = visit[e], e
    return max


dis, node = bfs(1)
dis, node = bfs(node)
print(dis-1)
