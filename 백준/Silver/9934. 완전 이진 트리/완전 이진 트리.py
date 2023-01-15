n = int(input())
arr = list(map(int,input().split()))
t = [[]for _ in range(n)]

def tree(arr,x):
    mid = (len(arr)//2)
    t[x].append(arr[mid])
    if(len(arr)==1):
        return
    tree(arr[:mid],x+1)
    tree(arr[mid+1:],x+1)

tree(arr,0)
for i in range(n):
    print(*t[i])


