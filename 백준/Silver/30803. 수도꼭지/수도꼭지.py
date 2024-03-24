import sys
input = sys.stdin.readline    

N = int(input())
arr = list(map(int, input().split()))
arr1 = [True] * len(arr)
Q = int(input())

# 초기 상태에서 활성화된 요소들의 합을 계산
total_sum = sum(arr)
print(total_sum)
for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        idx, new_value = query[1]-1, query[2]
        if arr1[idx]:  # 해당 인덱스가 활성화 상태인 경우에만 전체 합에 반영
            total_sum += new_value - arr[idx]  # 변경된 값의 차이만큼만 합에 반영
        arr[idx] = new_value
    else:
        idx = query[1]-1
        if arr1[idx]:  # 해당 인덱스가 활성화 상태였다면, 비활성화하고 합에서 빼기
            total_sum -= arr[idx]
        else:  # 비활성화 상태였다면, 활성화하고 합에 더하기
            total_sum += arr[idx]
        arr1[idx] = not arr1[idx]
    
    print(total_sum)
