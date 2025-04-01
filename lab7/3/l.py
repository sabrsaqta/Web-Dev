import math
n = int(input())
length = len(str(n))
power = -1
ans = 0
for i in range(length):
    x = n % 10
    power += 1
    if x == 1:
        ans += 2**power
    n //= 10
    
print(ans)