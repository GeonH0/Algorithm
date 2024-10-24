


T = 10
for test_case in range(1,T+1):
    _  = int(input())
    arr = []
    for i in range(100):
        arr.append([0] + list(map(int,input().split())) + [0])

    mn = 100*100

    for sj in range(1,101):
        if arr[0][sj] == 0:
            continue

        cj = sj
        cnt = dr = ci = 0

        while ci < 99:
            #먼저 이동
            cnt +=1
            # 방향 전환
            if dr == 0:
                ci +=1
                # 왼쪽에 길이 있다면
                if arr[ci][cj-1] == 1:
                    dr = -1
                # 오른쪽에 길이 있다면
                elif arr[ci][cj+1] == 1:
                    dr = 1
            # 방향이 좌/우로 셋팅 되어 있을경우
            else:                
                cj += dr
                if arr[ci][cj+dr] == 0:
                    dr = 0
        if mn >= cnt:
            mn,ans = cnt,sj-1

    print(f'#{test_case} {ans}')

        
        
    
