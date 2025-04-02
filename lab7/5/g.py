n = int(input())
lst = list(map(int, input().split()))
count = 0

for i in range(len(lst)//2):
    temp = lst[len(lst) - 1 - i]
    lst[len(lst) - 1 - i] = lst[i]
    lst[i] = temp

for i in range(len(lst)):
    print(lst[i], end=" ")


