
T = 10

for t in range(1,T+1):
    n = int(input())
    arr = []        
    for _ in range(100):        
        arr.append(list(map(int,input().split())))
    ans,s3,s4  = 0,0,0
    for i in range(100):
        s1,s2 = 0,0
        for j in range(100):
            s1 += arr[i][j]
            s2 += arr[j][i]
        ans = max(ans, s1, s2)
        s3 += arr[i][i]
        s4 += arr[i][99-i]
    ans = max(ans, s3, s4)
    print(f'#{t} {ans}')

        

