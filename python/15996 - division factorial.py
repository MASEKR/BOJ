n, a = map(int, input().split())
m = n // a
cnt = m

while m >= a:
    m //= a
    cnt += m

print(cnt)
