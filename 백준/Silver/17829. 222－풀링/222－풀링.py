
def poling(size,x,y):
    mid = size//2
    if size ==2:
        ans = [arr[x][y],arr[x+1][y],arr[x][y+1],arr[x+1][y+1]]
        ans.sort()
        return ans[-2]
    lt = poling(mid,x,y)
    rt = poling(mid,x+mid,y)
    lb = poling(mid,x,y+mid)
    rb = poling(mid,x+mid,y+mid)
    ans = [lt,rt,lb,rb]
    ans.sort()
    return ans[-2]

N = int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))


print(poling(N,0,0))