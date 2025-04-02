def average(array):
    st = set()
    for i in array:
        st.add(i)
        
    totalsum = 0
    avgres = 0
    for i in st:
        totalsum += i
    avgres = totalsum/len(st)
    return avgres
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)