def check():
    for i in range(3):
        if arr[i]==arr[i+1]:
            return i

max,cost=-1,0

n = int(input())
for _ in range(n):
    arr=list(map(int,input().split()))
    arr.sort()

    s = len(set(arr))

    if s==1:
        cost= 50000+arr[0]*5000
    elif s==2:
        if arr[0]==arr[1] and arr[2]== arr[3]:
            cost = 2000+arr[0]*500+arr[3]*500
        else:
            cost = 10000+arr[1]*1000
    elif s==3:
        cost = 1000 + arr[check()]*100
    else:
        cost = arr[3]*100
    if cost > max:
        max = cost

print(max)