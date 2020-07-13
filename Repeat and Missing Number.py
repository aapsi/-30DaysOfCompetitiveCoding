#Day1: (Arrays)

#Repeat and Missing Number

# time complexity = O(NlogN) and space complexity O(N)
def misrep(arr):
    n = len(arr)
    newarr = sorted(arr)
    setarr = list(set(newarr))
    repeating = 0
    missing = int(n * (n + 1) / 2) - (sum(setarr))
    for i in range(n-1):
        if newarr[i] == newarr[i+1]:
            repeating = newarr[i]
    print('repeating :', repeating)
    print('missing :', missing)

# time complexity = O(N) and space complexity O(N)
def misrep2(arr):
    n = len(arr)
    temp = [0]*(n+1)
    repeating = 0
    missing = 0
    for i in range(n):
        if temp[arr[i]] == 0:
            temp[arr[i]] = 1
        else:
            repeating = arr[i]
    for i in range(1,len(temp)):
        if temp[i] == 0:
            missing = i
    print('repeating :', repeating)
    print('missing :', missing)

# time complexity O(n) and space complexity O(1)
def misrep3(arr):
    n = len(arr)
    repeating = 0
    missing = 0
    for i in range(n):
        if arr[arr[i]] <0:
            repeating = arr[i]
        if arr[arr[i]] >0:
            arr[arr[i]] *= -1
    for i in range(n):
        if arr[i] > 0:
            missing = arr[i]
    print('repeating :', repeating)
    print('missing :', missing)

arr = list(map(int,input().split()))
misrep(arr)
misrep2(arr)
misrep3(arr)
