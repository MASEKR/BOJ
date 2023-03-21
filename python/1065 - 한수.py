# solution 1
n = int(input())
print(sum([(n < 100) or (n // 100 + n%10 == 2*(n//10 % 10)) for n in range(1, n+1)]))

# solution 2
# def hansoo(n):
#     cnt = 0
#     if n == 0:
#         return False
#     elif n == 1000:
#         n = 999
#         cnt = 99
#     else:
#         cnt = 99
#         if n < 100:
#             cnt = n
#
#     if 100 <= n < 1000:
#         for i in range(100, n + 1):
#             num = list(map(int, str(i)))
#             if num[0] - num[1] == num[1] - num[2]:
#                 cnt += 1
#             else:
#                 continue
#
#     return cnt
#
#
# print(hansoo(int(input())))
