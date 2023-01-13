n = int(input())
arr=list(map(int,input().split()))
cnt = list(dict.fromkeys(arr))
cnt.sort()
for i in cnt:
    print(i,end=" ")
    