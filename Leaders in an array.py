for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    l = []
    flag = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                break
        if j == n-1:
            print(arr[i],end = ' ')
    print()        