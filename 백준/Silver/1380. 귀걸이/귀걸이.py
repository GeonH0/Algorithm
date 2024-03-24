
ans = []
while True:
    arr= []    
    N = int(input())
    if N == 0:
        break
    for _ in range(N):
        arr.append(input())
    arr1 = [0] * N

    for _ in range((2*N)-1):
        name,al = map(str,input().split())
        arr1[int(name)-1] += 1

        
    for i in range(len(arr1)):
        if arr1[i] == 1:
            ans.append(arr[i])

for i in range(len(ans)):
    print(i+1,ans[i])
    

