

N,M = map(int,input().split())
arr={}
for _ in range(N):
    S,P = input().split()
    arr[S] = P 
for _ in range(M):
    print(arr[input().rstrip()])