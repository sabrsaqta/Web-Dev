# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
st = set()
for i in range(n):
    string = input()
    st.add(string)
print(len(st))