import re
import sys

T = int(sys.stdin.readline())
res = []

for _ in range(T):
    c = sys.stdin.readline().replace('\n', '')
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(c)
    if m:
        res.append("YES")
    else: res.append("NO")

for r in res:
    sys.stdout.write(str(r) + '\n')