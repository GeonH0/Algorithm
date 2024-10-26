T = int(input())

for test_case in range(1,T+1):
    N,M,K = map(int,input().split())
    people = list(map(int,input().split()))    
    people.sort()
    flag = True
    cnt = 0
    for i in people:
        cnt += 1
        if (i//M) *K <cnt:
            flag = False
            break        
    if flag:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')