#code
#import collections
t = int(input())
a = -1
for i in range(t):
    freq = {}
    n = int(input())
    flag = 0
    arr = list(map(int,input().split()))
    for item in arr:
        if item in freq:
            freq[item]+=1
        else:
            freq[item] = 1
    for key in freq:
        if freq[key] > n/2:
            flag = 1
            print(key)
            break
    if flag == 0:
        print(a)