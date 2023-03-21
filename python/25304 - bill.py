total = int(input())
n = int(input())
price = 0

for i in range(n):
    obj, obj_price = input().split()
    price += int(obj)*int(obj_price)

if price == total:
    print("Yes")
else:
    print("No")
