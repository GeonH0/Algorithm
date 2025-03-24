import sys
input = sys.stdin.readline

N, K = map(int, input().split())
countries = []

for _ in range(N):
    num, gold, silver, bronze = map(int, input().split())
    countries.append((num, gold, silver, bronze))

# 금, 은, 동 내림차순 정렬
countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1  # 현재 순위
for i in range(N):
    if i > 0:
        # 이전 나라와 메달 수가 다르면 순위 업데이트
        if countries[i][1:] != countries[i - 1][1:]:
            rank = i + 1  # 0-indexed → 등수는 i+1

    # 찾고자 하는 국가 번호일 때 출력
    if countries[i][0] == K:
        print(rank)
        break