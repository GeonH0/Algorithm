def find_max_budget_limit(requests, total_budget):
    start, end = 1, max(requests)  # 상한선 범위
    best_limit = 0  # 최적의 상한값 저장

    while start <= end:
        mid = (start + end) // 2  # 중간값을 상한으로 설정
        total = sum(min(req, mid) for req in requests)  # 상한선 적용 후 예산 총합

        if total <= total_budget:  # 예산 범위 내면 상한선을 올려본다
            best_limit = mid  # 최적의 상한값 업데이트
            start = mid + 1  # 더 높은 값 탐색
        else:
            end = mid - 1  # 예산 초과 → 상한선 낮춤

    return best_limit  # 최적의 상한값 반환


# 입력 처리
N = int(input())  # 지방의 수
requests = list(map(int, input().split()))  # 각 지방의 예산 요청
M = int(input())  # 총 예산

# 최적의 상한액 찾기
print(find_max_budget_limit(requests, M))