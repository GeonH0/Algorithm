import sys
input = sys.stdin.readline


a,p = map(int,input().split())

arr=[]
arr.append(a)
i = 1

while True:
    tmp = 0
    for s in str(arr[-1]):
        tmp += int(s)** p
    
    if tmp in arr:
        break

    arr.append(tmp)
print(arr.index(tmp))
