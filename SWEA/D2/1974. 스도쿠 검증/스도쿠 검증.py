
def check(arr):
    for lst in arr:
        if len(set(lst)) != N:
            return 0
    
    # 전치 행렬 -> 행
    arr1 = list(zip(*arr))
    for n in arr1:
        if len(set(n)) != N:
            return 0
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            lst = []
            lst += arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(lst)) != N:
                return 0
    return 1

T = int(input())


for test_case in range(1,T+1):
    N = 9
    arr =[]
    for _ in range(N):
        arr.append(list(map(int,input().split())))    
    
    print(f"#{test_case} {check(arr)}")
    