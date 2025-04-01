import math

x = int(input())
num = 2
while True:
    if x % num == 0:
        print(num)
        break
    num += 1
    