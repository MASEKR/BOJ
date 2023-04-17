n = num = int(input())
cnt = 0
while True:
    ten = n//10
    one = n % 10
    total = ten + one
    cnt += 1
    n = int(str(n % 10) + str(total % 10))
    if num == n: break

print(cnt)