def turn90(arr):
    # 90도
    newlist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newlist[i][j] = arr[j][i]
        newlist[i] = newlist[i][::-1]
    return newlist
    
    # 180도
def turn180(arr):
    newlist = [[]* N for _ in range(N)]
    for i in range(N):                
        newlist[i] = arr[-i-1][::-1]
    return newlist
    # 270도
def turn270(arr):
    newlist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newlist[-1-i][j] = arr[j][i]        
    return newlist
         

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    
    arr90 = turn90(arr)
    arr180 = turn180(arr)
    arr270 = turn270(arr)
    
    print(f'#{test_case}')
    for i in range(N):
        # 90도, 180도, 270도 회전한 결과를 한 줄에 출력
        print(''.join(map(str, arr90[i])), ''.join(map(str, arr180[i])), ''.join(map(str, arr270[i])))
