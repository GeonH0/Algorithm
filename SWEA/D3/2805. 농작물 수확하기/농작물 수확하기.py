T = int(input())


for test_case in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input())))
    
    cnt = N//2
    ans = 0
    for i in range(N):
        if i <= cnt:        
            for j in range(cnt-i,cnt+i+1):
                ans += arr[i][j]
        else:
            for j in range(i-cnt,N-(i-cnt)):
                ans += arr[i][j]

    print(f'#{test_case} {ans}')


    
