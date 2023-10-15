a = int(input())
x = 0
for i in range(2, a // 2 + 1):
    if int(a % i == 0):
        x = x + 1
if int(x <= 0):
    print("YES")
else:
    print("NO")