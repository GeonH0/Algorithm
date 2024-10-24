
T = 10

for test_case in range(1,T+1):
    _ = int(input())
    arr =[]
    for i in range(100):
        # 범위 확인을 줄이기 위해 양 옆으로 0을 추가한다.
        arr.append([0] + list(map(int, input().split())) + [0])        
    
    ci = 99    
    #시작 지점 탐색
    for j in range(100):
        if arr[ci][j] == 2:
            cj = j
            break

    # 0 행 까지 올라가면서 좌 -> 우 -> 위로 이동한다.
    while ci > 0:
        arr[ci][cj] = 0
        # 왼쪽에 길이 있다면
        if arr[ci][cj-1] == 1:
            cj -=1
        #오른쪽에 길이 있다면
        elif arr[ci][cj+1] == 1:
            cj +=1
        #좌/우 확인후 없으면 위로 올라가기
        else:
            ci -=1
    print(f'#{test_case} {cj-1}')