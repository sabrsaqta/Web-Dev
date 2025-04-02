n = int(input())
lst = list(map(int, input().split()))
flag = False

for i in range(1, len(lst)):
    if (lst[i] > 0 and lst[i-1] > 0) or (lst[i] < 0 and lst[i-1] < 0):
        flag = True
        print("YES")
        exit()
if not flag:
    print("NO")

