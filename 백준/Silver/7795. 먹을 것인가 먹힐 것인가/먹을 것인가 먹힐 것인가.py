t= int(input())



def binary_search(tar,data):
    start = 0
    end = len(data)-1
    res = -1
    while start<=end:
        mid = (start+end)//2
        if data[mid]<tar:
            res = mid
            start = mid+1
        else:
            end = mid-1
    return res
for i in range(t):
    n,m = map(int,input().split())
    a=list((map(int,input().split())))
    b=list((map(int,input().split())))
    cnt =0
    a.sort()
    b.sort()

    for i in a:
        cnt += binary_search(i,b)+1
    print(cnt)