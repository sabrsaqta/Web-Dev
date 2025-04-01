import math
x = int(input())
rx = 0

for i in range(len(str(x))):
    rx = rx*10 + x%10
    x //= 10

print(rx)