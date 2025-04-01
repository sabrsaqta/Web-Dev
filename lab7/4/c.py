import math

x = int(input())
num = 0
while num < x:
    num *= 2
    if num == 0:
        print(1)
        num += 1
        continue
    if num <= x:
        print(num)
    
    