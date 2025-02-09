import bisect

def count_occurrences(arr, target):
    left = bisect.bisect_left(arr, target)  # target이 처음 등장하는 위치
    right = bisect.bisect_right(arr, target)  # target보다 큰 값이 처음 등장하는 위치
    
    # target이 배열에 없으면 0 반환
    if left == right:
        return 0
    return right - left  # target의 개수 계산

# 입력
N = int(input())  # 배열 크기
arr = list(map(int, input().split()))  # 정렬된 배열
M = int(input())
search = list(map(int,input().split()))

# 정렬 필수 (이진 탐색 조건)
arr.sort()
ans = []
# 개수 찾기
for i in search:
    ans.append(count_occurrences(arr,i))

print(" ".join(map(str,ans)))