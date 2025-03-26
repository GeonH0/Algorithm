import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lights = list(map(int, input().split()))

def is_possible(h):
    # 스위핑 구간 방식
    covered = 0
    for light in lights:
        left = light - h
        right = light + h

        # 밝히지 못한 구간이 있으면 실패
        if left > covered:
            return False
        covered = max(covered, right)

    return covered >= N  # 끝까지 도달했는지 확인

start = 0
end = N
answer = N

while start <= end:
    mid = (start + end) // 2
    if is_possible(mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)