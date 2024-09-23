def bombCheck(x, y):
    cnt = 0
    # 8방향 체크
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:  # 범위를 벗어나지 않는지 체크
            if bomb[nx][ny] == '*':  # 주변에 지뢰가 있으면 카운트 증가
                cnt += 1

    return cnt  # 지뢰의 개수를 반환


N = int(input())

bomb = [list(input().strip()) for _ in range(N)]
ans = [list(input().strip()) for _ in range(N)]

# 상 하 좌 우 우상대각 우하대각 좌상대각 좌하대각
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

result = [["."] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if bomb[i][j] == '.' and ans[i][j] == 'x':  # 지뢰가 없으면서 열림
            result[i][j] = str(bombCheck(i, j))            
        if bomb[i][j] == '*' and ans[i][j] == 'x':  # 지뢰가 열렸으면 모든 지뢰를 표시
            for a in range(N):
                for b in range(N):
                    if bomb[a][b] == '*':
                        result[a][b] = '*'

for row in result:
    print("".join(map(str, row)))

