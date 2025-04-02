# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

ans = list()
for i in a:
    if i not in b:
        ans.append(i)
for i in b:
    if i not in a:
        ans.append(i)
    
ans.sort()
for x in ans:
    print(x)